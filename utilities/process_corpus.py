# Copyright (C) 2024 David West Brown

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from collections import OrderedDict
import math
import os
import polars as pl
import random
import re
import string
import unidecode

def check_language(text_str, detect_model, detect_language):
	doc_len = len(text_str)
	predictions = []
	if doc_len > 5000:
		idx_a = random.randint(0, doc_len - 1500)
		idx_b = random.randint(0, doc_len - 1500)
		idx_c = random.randint(0, doc_len - 1500)
		sample_a = text_str[idx_a:idx_a + 1000]
		sample_a = " ".join(sample_a.split())
		sample_b = text_str[idx_b:idx_b + 1000]
		sample_b = " ".join(sample_b.split())
		sample_c = text_str[idx_c:idx_c + 1000]
		sample_c = " ".join(sample_c.split())
		text_sample = [sample_a, sample_b, sample_c]
		#get prediction for each chunk
		for chunk in text_sample:  # Language predict each sampled chunk
			value = detect_model.compute_language_confidence(chunk, detect_language)
			predictions.append(value)
	else:
		text_str = " ".join(text_str.split())
		value = detect_model.compute_language_confidence(text_str, detect_language)
		predictions.append(value)
		
	confidence = sum(predictions) / len(predictions)

	# Only want to know if this is english or not.
	return confidence > .9

def pre_process(txt):
	txt = re.sub(r'\bits\b', 'it s', txt)
	txt = re.sub(r'\bIts\b', 'It s', txt)
	txt = " ".join(txt.split())
	return(txt)

def process_corpus(corp, nlp_model):
	is_punct = re.compile("[{}]+\s*$".format(re.escape(string.punctuation)))
	is_digit = re.compile("\d[\d{}]*\s*$".format(re.escape(string.punctuation)))
	tp = {}
	exceptions = []
	for doc in corp:
		try:
			doc_txt = doc.getvalue().decode('utf-8')
		except:
			exceptions.append(doc.name)
		else:
			doc_txt = unidecode.unidecode(doc_txt)
			doc_id = doc.name.replace(" ", "")
			doc_id = str(os.path.splitext(doc_id)[0])
			doc_txt = pre_process(doc_txt)
			doc_len = len(doc_txt)
			if doc_len > 1000000:
				n_chunks = math.ceil(doc_len/750000)
				chunk_idx = [math.ceil(i/n_chunks*doc_len) for i in range(1, n_chunks)]
				try:
					split_idx = [re.search('[\.\?!] [A-Z]', doc_txt[idx:]).span()[1] + (idx-1) for idx in chunk_idx]
				except:
					try:
						split_idx = [re.search(' ', doc_txt[idx:]).span()[0] + idx for idx in chunk_idx]
					except:
						exceptions.append(doc.name)
				else:
					split_idx.insert(0, 0)
					doc_chunks = [doc_txt[i:j] for i, j in zip(split_idx, split_idx[1:]+[None])]
					token_list = []
					tag_list = []
					iob_ent = []
					for chunk in doc_chunks:
						chunk_taged = nlp_model(chunk)
						token_chunk = [token.text for token in chunk_taged]
						ws_chunk = [token.whitespace_ for token in chunk_taged]
						token_chunk = list(map(''.join, zip(token_chunk, ws_chunk)))
						iob_chunk = [token.ent_iob_ for token in chunk_taged]
						ent_chunk = [token.ent_type_ for token in chunk_taged]
						iob_ent_chunk = list(map('-'.join, zip(iob_chunk, ent_chunk)))
						tag_chunk = [token.tag_ for token in chunk_taged]
						tag_chunk = ['Y' if bool(is_punct.match(token_chunk[i])) else v for i, v in enumerate(tag_chunk)]
						tag_chunk = ['MC' if bool(is_digit.match(token_chunk[i])) and tag_chunk[i] != 'Y' else v for i, v in enumerate(tag_chunk)]
						token_list.append(token_chunk)
						tag_list.append(tag_chunk)
						iob_ent.append(iob_ent_chunk)
					token_list = [item for sublist in token_list for item in sublist]
					tag_list = [item for sublist in tag_list for item in sublist]
					iob_ent = [item for sublist in iob_ent for item in sublist]
					tp.update({doc_id: (list(zip(token_list, tag_list, iob_ent)))})
			else:
				doc_taged = nlp_model(doc_txt)
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
				tp = dict(sorted(tp.items()))
	return tp, exceptions

def process_corpus_detect(corp, nlp_model, detect_model, detect_language):
	is_punct = re.compile("[{}]+\s*$".format(re.escape(string.punctuation)))
	is_digit = re.compile("\d[\d{}]*\s*$".format(re.escape(string.punctuation)))
	tp = {}
	exceptions = []
	for doc in corp:
		try:
			doc_txt = doc.getvalue().decode('utf-8')
		except:
			exceptions.append(doc.name)
		else:
			doc_txt = unidecode.unidecode(doc_txt)
			is_english = check_language(doc_txt, detect_model, detect_language)
			if is_english == False:
				exceptions.append(doc.name)
			else:
				doc_id = doc.name.replace(" ", "")
				doc_id = str(os.path.splitext(doc_id)[0])
				doc_txt = pre_process(doc_txt)
				doc_len = len(doc_txt)
				if doc_len > 1000000:
					n_chunks = math.ceil(doc_len/750000)
					chunk_idx = [math.ceil(i/n_chunks*doc_len) for i in range(1, n_chunks)]
					try:
						split_idx = [re.search('[\.\?!] [A-Z]', doc_txt[idx:]).span()[1] + (idx-1) for idx in chunk_idx]
					except:
						try:
							split_idx = [re.search(' ', doc_txt[idx:]).span()[0] + idx for idx in chunk_idx]
						except:
							exceptions.append(doc.name)
					else:
						split_idx.insert(0, 0)
						doc_chunks = [doc_txt[i:j] for i, j in zip(split_idx, split_idx[1:]+[None])]
						token_list = []
						tag_list = []
						iob_ent = []
						for chunk in doc_chunks:
							chunk_taged = nlp_model(chunk)
							token_chunk = [token.text for token in chunk_taged]
							ws_chunk = [token.whitespace_ for token in chunk_taged]
							token_chunk = list(map(''.join, zip(token_chunk, ws_chunk)))
							iob_chunk = [token.ent_iob_ for token in chunk_taged]
							ent_chunk = [token.ent_type_ for token in chunk_taged]
							iob_ent_chunk = list(map('-'.join, zip(iob_chunk, ent_chunk)))
							tag_chunk = [token.tag_ for token in chunk_taged]
							tag_chunk = ['Y' if bool(is_punct.match(token_chunk[i])) else v for i, v in enumerate(tag_chunk)]
							tag_chunk = ['MC' if bool(is_digit.match(token_chunk[i])) and tag_chunk[i] != 'Y' else v for i, v in enumerate(tag_chunk)]
							token_list.append(token_chunk)
							tag_list.append(tag_chunk)
							iob_ent.append(iob_ent_chunk)
						token_list = [item for sublist in token_list for item in sublist]
						tag_list = [item for sublist in tag_list for item in sublist]
						iob_ent = [item for sublist in iob_ent for item in sublist]
						tp.update({doc_id: (list(zip(token_list, tag_list, iob_ent)))})
				else:
					doc_taged = nlp_model(doc_txt)
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
					tp = dict(sorted(tp.items()))
	return tp, exceptions

def get_corpus_features(ibis_conn):
	df = ibis_conn.table('ds_tokens').to_polars()
	tags_pos = df["pos_tag"].unique().to_list().remove("Y")
	tags_ds = df["ds_tag"].unique().to_list().remove("Untagged")
	return tags_pos, tags_ds

def check_corpus(docs, check_size=False, check_ref=False, target_docs=None):
	if len(docs) > 0:
		all_files = []
		if check_size:
			for file in docs:
				bytes_data = file.getvalue()
				file_size = len(bytes_data)
				all_files.append(file_size)
			corpus_size = sum(all_files)
		#check for duplicates
		doc_ids = [str(os.path.splitext(doc.name)[0]) for doc in docs]
		doc_ids = [doc.replace(" ", "") for doc in doc_ids]
		if len(doc_ids) > len(set(doc_ids)):
			dup_ids = [x for x in doc_ids if doc_ids.count(x) >= 2]
			dup_ids = list(set(dup_ids))
		else:
			dup_ids = []
		if check_ref and target_docs is not None:
			dup_docs = list(set(target_docs).intersection(doc_ids))
	else:
		corpus_size = 0
		dup_ids = []
		dup_docs = []
	if check_ref and check_size:
		return(dup_ids, dup_docs, corpus_size)
	elif check_ref and not check_size:
		return(dup_ids, dup_docs)
	elif check_size and not check_ref:
		return(dup_ids, corpus_size)
	else:
		return(dup_ids)

def check_schema(tok_pl):
	validation = OrderedDict([('doc_id', pl.String), ('token', pl.String), ('pos_tag', pl.String), ('ds_tag', pl.String), ('pos_id', pl.UInt32), ('ds_id', pl.UInt32)])
	return tok_pl.schema == validation

def check_corpus_pl(tok_pl, check_size=False, check_ref=False, target_docs=None):
	is_valid = check_schema(tok_pl)
	if check_size:
		corpus_size = tok_pl.estimated_size()
	#check for duplicates
	doc_ids = tok_pl.get_column("doc_id").unique().to_list()
	if check_ref and target_docs is not None:
		dup_docs = list(set(target_docs).intersection(doc_ids))
	else:
		dup_docs = []
	if check_ref and check_size:
		return(is_valid, dup_docs, corpus_size)
	elif check_ref and not check_size:
		return(is_valid, dup_docs)
	elif check_size and not check_ref:
		return(is_valid, corpus_size)
	else:
		return(is_valid)
	
def check_reference_pl(tok_pl, target_docs):
	doc_ids = tok_pl.get_column("doc_id").unique().to_list()
	dup_docs = list(set(target_docs).intersection(doc_ids))
	return(dup_docs)

def check_reference(ibis_conn):
	target = ibis_conn.table("ds_tokens", database="target")
	reference = ibis_conn.table("ds_tokens", database="reference")
	target_docs = sorted(target.get_column("doc_id").unique().to_list())
	reference_docs = sorted(reference.get_column("doc_id").unique().to_list())
	dup_docs = list(set(target_docs).intersection(reference_docs))
	if len(dup_docs) > 0:
		df = reference_docs.filter(pl.col("doc_id").is_in(dup_docs).not_())
		ibis_conn.create_table()
	return df, dup_docs

def get_doc_cats(doc_ids):
	if all(['_' in item for item in doc_ids]):
		doc_cats = [re.sub(r"_\S+$", "", item, flags=re.UNICODE) for item in doc_ids]
		if min([len(item) for item in doc_cats]) == 0:
			doc_cats = []
	else:
		doc_cats = []
	return doc_cats

def tokens_to_pl(tok):
    data = [[k, *v] for k, lst in tok.items() for v in lst]
    df = (
        pl.DataFrame(data, schema =["doc_id", "token", "pos_tag", "ds_tag"], orient="row")
        # assign unique ids to part-of-speech tags for grouping
        .with_columns(
            pl.when(
                pl.col("pos_tag").str.contains("\d\d$") & pl.col("pos_tag").str.contains("[^1]$")
            )
            .then(None)
            .otherwise(True)
            .alias('pos_id')
        )
        .with_columns(
            pl.when(
                pl.col("pos_id") == True)
            .then(pl.cum_sum("pos_id"))
            .otherwise(None)
            .forward_fill()
        )
        # ensure that ids and base tags are the same (e.g., II21, II22, etc. render as II)
        .with_columns(
            pl.when(
                pl.col("pos_tag").str.contains("\d\d$") & pl.col("pos_tag").str.contains("[^1]$")
            )
            .then(None)
            .otherwise(pl.col("pos_tag").str.replace("\d\d$", ""))
            .forward_fill() 
            .name.keep()
        )
        # assign unique ids to DocuScope tags for grouping
        .with_columns(
            pl.when(
                pl.col("ds_tag").str.starts_with("B-") | pl.col("ds_tag").str.starts_with("O-")
            )
            .then(True)
            .otherwise(False)
            .alias('ds_id')
        )
        .with_columns(
            pl.when(
                pl.col("ds_id") == True
            )
            .then(pl.cum_sum("ds_id"))
            .otherwise(None)
            .forward_fill()
        )
        # ensure that ids and base tags are the same (e.g., B-ConfidenceHigh, I-ConfidenceHigh are rendered as ConfidenceHigh)
        .with_columns(
            pl.when(
                pl.col("ds_tag").str.starts_with("B-") | pl.col("ds_tag").str.starts_with("O-")
            )
            .then(pl.col("ds_tag").str.strip_chars_start("B-"))
            .otherwise(None)
            .forward_fill()
        )
        .with_columns(
            pl.when(
                pl.col("ds_tag") == "O-"
            )
            .then(pl.col("ds_tag").str.replace("O-", "Untagged"))
            .otherwise(pl.col("ds_tag"))
        )
    )
    return(df)

