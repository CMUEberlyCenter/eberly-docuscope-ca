import streamlit as st

# NLP Pkgs
import spacy
import docuscospacy.corpus_analysis as ds

import re
import string
from collections import Counter

st.title("Load and manage your corpus")

if 'corpus' not in st.session_state:
	st.session_state.corpus = ''

if 'docids' not in st.session_state:
	st.session_state.docids = ''

if 'tags_pos' not in st.session_state:
	st.session_state.tags_pos = ''

if 'tags_ds' not in st.session_state:
	st.session_state.tags_ds = ''

if 'words' not in st.session_state:
	st.session_state.words = 0

if 'tokens' not in st.session_state:
	st.session_state.tokens = 0

if 'ndocs' not in st.session_state:
	st.session_state.ndocs = 0

if 'doccats' not in st.session_state:
	st.session_state.doccats = ''

if 'reference' not in st.session_state:
	st.session_state.reference = ''


nlp = spacy.load('en_docusco_spacy')

def pre_process(txt):
	txt = re.sub(r'\bits\b', 'it s', txt)
	txt = re.sub(r'\bIts\b', 'It s', txt)
	txt = " ".join(txt.split())
	return(txt)

def process_corpus(corp):
	doc_ids = [doc.name for doc in corp]
	doc_ids = [doc.replace(" ", "") for doc in doc_ids]
	if len(doc_ids) > len(set(doc_ids)):
		dup_ids = [x for x in doc_ids if doc_ids.count(x) >= 2]
		st.write("Your documents contain duplicate names: ", dup_ids)
	else:
		is_punct = re.compile("[{}]+\s*$".format(re.escape(string.punctuation)))
		is_digit = re.compile("\d[\d{}]*\s*$".format(re.escape(string.punctuation)))
		tp = {}
		for doc in corp:	
			doc_txt = doc.getvalue().decode("utf-8")
			doc_id = doc.name.replace(" ", "")
			doc_txt = pre_process(doc_txt)
			doc_taged = nlp(doc_txt)
			token_list = [token.text for token in doc_taged]
			ws_list = [token.whitespace_ for token in doc_taged]
			token_list = list(map(''.join, zip(token_list, ws_list)))
			iob_list = [token.ent_iob_ for token in doc_taged]
			ent_list = [token.ent_type_ for token in doc_taged]
			iob_ent = list(map('-'.join, zip(iob_list, ent_list)))
			tag_list = [token.tag_ for token in doc_taged]
			tag_list = ['Y' if bool(is_punct.match(token_list[i])) else v for i, v in enumerate(tag_list)]
			tag_list = ['MC' if bool(is_digit.match(token_list[i])) and tag_list[i] != 'Y' else v for i, v in enumerate(tag_list)]
			tp.update({doc_id: (list(zip(token_list, tag_list, iob_ent)))})
		return tp
	
if st.session_state.ndocs > 0:
	st.write('Number of tokens in corpus: ', str(st.session_state.tokens))
	st.write('Number of word tokens in corpus: ', str(st.session_state.words))
	st.write('Number of documents in corpus: ', str(st.session_state.ndocs))
	with st.expander("Documents:"):
		st.write(st.session_state.docids)
	
	if st.session_state.doccats != '':
		with st.expander("Counts of document categories:"):
			st.write(Counter(st.session_state.doccats))
	else:
		load_cats = st.radio("Do you have categories in your file names to process?", ("No", "Yes"), horizontal=True)
		if load_cats == 'Yes':
			if st.button("Process Document Metadata"):
				with st.spinner('Processing metadata...'):
					if all(['_' in item for item in st.session_state.docids]):
						doc_cats = [re.sub(r"_\S+$", "", item, flags=re.UNICODE) for item in st.session_state.docids]
						if min([len(item) for item in doc_cats]) > 0 and len(set(doc_cats)) > 1:
							st.session_state.doccats = doc_cats
							st.success('Processing complete!')
							st.experimental_rerun()
						else:
							st.markdown(":no_entry_sign: Your categories don't seem to be formatted correctly or your data contain only a single category. You can either proceed without assigning categories, or reset the corpus, fix your file names, and try again.")
					else:
						st.markdown(":no_entry_sign: Your categories don't seem to be formatted correctly. You can either proceed without assigning categories, or reset the corpus, fix your file names, and try again.")


	
	st.markdown(":warning: Using the **reset** button will cause all files, tables, and plots to be cleared.")
	if st.button("Reset Corpus"):
		for key in st.session_state.keys():
			del st.session_state[key]
		st.experimental_singleton.clear()
		st.experimental_rerun()
else:

	st.markdown("From this page you can load a corpus from a selection of text (**.txt**) files or reset a corpus once one has been processed.")
	st.markdown(":warning: Be sure that all file names are unique.")

	corp_files = st.file_uploader("Upload your corpus", type=["txt"], accept_multiple_files=True)
	
	if len(corp_files) > 0:
		if st.button("Process Corpus"):
			with st.spinner('Processing corpus data...'):
				corp = process_corpus(corp_files)
			if corp == None:
				st.success('Fix or remove duplicate file names before processing corpus.')
			else:
				st.success('Processing complete!')
				tok = list(corp.values())
				#get pos tags
				tags_pos = []
				for i in range(0,len(tok)):
					tags = [x[1] for x in tok[i]]
					tags_pos.append(tags)
				tags_pos = [x for xs in tags_pos for x in xs]
				#get ds tags
				tags_ds = []
				for i in range(0,len(tok)):
					tags = [x[2] for x in tok[i]]
					tags_ds.append(tags)
				tags_ds = [x for xs in tags_ds for x in xs]
				tags_ds = [x for x in tags_ds if x.startswith('B-')]
				#assign session states
				st.session_state.tokens = len(tags_pos)
				st.session_state.words = len([x for x in tags_pos if not x.startswith('Y')])
				st.session_state.corpus = corp
				st.session_state.docids = list(corp.keys())
				st.session_state.ndocs = len(list(corp.keys()))
				#tagsets
				tags_ds = set(tags_ds)
				tags_ds = sorted(set([re.sub(r'B-', '', i) for i in tags_ds]))
				tags_pos = set(tags_pos)
				tags_pos = sorted(set([re.sub(r'\d\d$', '', i) for i in tags_pos]))
				st.session_state.tags_ds = tags_ds
				st.session_state.tags_pos = tags_pos
				st.experimental_rerun()
