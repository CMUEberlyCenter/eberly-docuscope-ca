# Copyright (C) 2023 David West Brown

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pathlib
from importlib.machinery import SourceFileLoader

# set paths
HERE = pathlib.Path(__file__).parents[1].resolve()
OPTIONS = str(HERE.joinpath("options.toml"))
IMPORTS = str(HERE.joinpath("utilities/handlers_imports.py"))

# import options
_imports = SourceFileLoader("handlers_imports", IMPORTS).load_module()
_options = _imports.import_options_general(OPTIONS)

modules = ['categories', 'streamlit']
import_params = _imports.import_parameters(_options, modules)

for module in import_params.keys():
	object_name = module
	short_name = import_params[module][0]
	context_module_name = import_params[module][1]
	if not short_name:
		short_name = object_name
	if not context_module_name:
		globals()[short_name] = __import__(object_name)
	else:
		context_module = __import__(context_module_name, fromlist=[object_name])
		globals()[short_name] = getattr(context_module, object_name)

CATEGORY = _categories.HELP
TITLE = "Togging between Tagsets"
KEY_SORT = 14

def main():
	st.markdown("### Linguistically-informed and rhetorically-informed tagging")
	
	st.markdown("""
		The application is designed to bridge traditional linguistically-informed corpus analysis with
		rhetorically-informed corpus analysis (or computational rhetoric). 
		Users can generate data that organize tokens into conventional lexical classes or 
		that organize tokens into rhetorical categories like **Narrative** or **Public Terms**.\n
		The application allows users to toggle easily between both allowing them to explore and
		find patterns they find have explanatory power.
		""")
	st.markdown("---")
	
	st.markdown("##### Toggling between tagsets")
	st.markdown("""
			The application produces outputs of the data with tokens identified by parts-of-speech and DocuScope.
			For example, part of a frequency can appear like this:
			
			| Token     | Tag  | AF  | RF       | Range |
			|-----------|------|-----|----------|-------|
			| was       | VBDZ | 594 | 4421.15  | 92%   |
			| can       | VM   | 423 | 3148.39  | 94%   |
			| students  | NN2  | 149 | 1109.014 | 20%   |
			| community | NN1  | 141 | 1049.46  | 30%   |
			""")
	st.markdown("")					
	st.markdown("""
			Or like this:
			
			| Token        | Tag                    | AF  | RF      | Range |
			|--------------|------------------------|-----|---------|-------|
			| , but        | Metadiscourse Cohesive | 193 | 1259.53 | 68%   |
			| can be       | Confidence Hedged      | 118 | 770.07  | 62%   |
			| will be      | Future                 | 113 | 737.44  | 52%   |
			| participants | Character              | 103 | 672.18  | 14%   |
			""")
	st.markdown("")					
	st.markdown("""
			You can toggle between the tagsets within each tool.
			In this way, the tool invites you to explore linguistic structure and variation from multiple perspectives.
			""")
				
	st.markdown("---")
	
	st.markdown("##### Multi-word (or multi-token) units")
	st.markdown("""Unlike most tokenizers and concordancers,
			this application aggregates multi-word sequences into a single token.
			This most commonly happens with DocuScope as it identifies many phrasal units (as in the table above).
			But this also occurs with part-of-speech tagging in tokens like:
			
			
			in spite of, for example, in addition to
			""")
	
	st.markdown("---")
	
	st.markdown("##### The model vs. the tools")
	st.markdown("""
			Importantly, this application uses neither the CLAWS7 tagger nor DocuScope.
			Rather, it relies on a spaCy model trained on those tagsets.
	
			If you are using this application for research, that distinction is important to make in your methodology.
			And those whose work upon which this application is based should always be appropriately cited.
			""")
	
	st.markdown("""
			CLAWS should be attribed to Leech et al.:\n\n
			>*Leech, G., Garside, R., & Bryant, M. (1994). CLAWS4: the tagging of the British National Corpus. In COLING 1994 Volume 1: The 15th International Conference on Computational Linguistics.*
			""")
	
	st.markdown("""
			And DocuScope to Kaufer and Ishizaki:\n\n
			>*Ishizaki, S., & Kaufer, D. (2012). Computer-aided rhetorical analysis. In Applied natural language processing: Identification, investigation and resolution (pp. 276-296). IGI Global.*
			""")
	
	st.markdown("---")
	
	st.markdown("""
		##### Limitations and warnings
		""")
	
	st.markdown("""
		The model that produces the tags was trained on American English.
		How it would perform on other varieties is unknown at this point.
		The model was also trained on roughly 100,000,000 words. 
		There are plans for a more rigorously trained model, but the preparation of training data is time-consuming.\n
		Also note, that part-of-speech tagging is, on the whole, more accurate that the rhetorical tagging (92.50% vs. 74.87%).
		As with any tagging system, what is generated by the model may not match the reader experience at the token- or text-level.
		Their potential lies in what they can reveal at scale.
		""")

if __name__ == "__main__":
    main()