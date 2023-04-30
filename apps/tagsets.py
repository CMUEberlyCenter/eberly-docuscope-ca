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
TITLE = "Tags Explained"
KEY_SORT = 13

def main():
	st.markdown("Below are tables detailing each of tagsets.")
	
	st.markdown("##### Parts-of-Speech (CLAWS7)")
	st.markdown("""
	Note that lexical categories all begin with the same letter (e.g., *V* for verb).
	This is useful for filtering.
	""")
	st.markdown("""
			|**Tag**| **Description**                                                      | **Examples**                                             |
			|-------|----------------------------------------------------------------------|----------------------------------------------------------|
			| APPGE | possessive pronoun, pre-nominal                                      | *my*, *your*, *our*                                      |
			| AT    | article                                                              | *the*, *no*                                              |
			| AT1   | singular article                                                     | *a*, *an*, *every*                                       |
			| BCL   | before-clause marker                                                 | *in order* (that), *in order* (to)                       |
			| CC    | coordinating conjunction                                             | *and*, *or*                                              |
			| CCB   | adversative coordinating conjunction                                 | *but*                                                    |
			| CS    | subordinating conjunction                                            | *if*, *because*, *unless*, *so*, *for*                   |
			| CSA   | as as conjunction                                                    | *as*                                                     |
			| CSN   | than as conjunction                                                  | *than*                                                   |
			| CST   | that as conjunction                                                  | *that*                                                   |
			| CSW   | whether as conjunction                                               | *whether*                                                |
			| DA    | after-determiner or post-determiner capable of pronominal   function | *such*, *former*, *same*                                 |
			| DA1   | singular after-determiner                                            | *little*, *much*                                         |
			| DA2   | plural after-determiner                                              | *few*, *several*, *many*                                 |
			| DAR   | comparative after-determiner                                         | *more*, *less*, *fewer*                                  |
			| DAT   | superlative after-determiner                                         | *most*, *least*, *fewest*                                |
			| DB    | before determiner or pre-determiner capable of pronominal   function | *all*, *half*                                            |
			| DB2   | plural before-determiner                                             | *both*                                                   |
			| DD    | determiner (capable of pronominal function)                          | *any*, *some*                                            |
			| DD1   | singular determiner                                                  | *this*, *that*, *another*                                |
			| DD2   | plural determiner                                                    | *these,those*                                            |
			| DDQ   | wh-determiner                                                        | *which*, *what*                                          |
			| DDQGE | wh-determiner, genitive                                              | *whose*                                                  |
			| DDQV  | wh-ever determiner                                                   | *whichever*, *whatever*                                  |
			| EX    | existential there                                                    | *there* (is), *there* (are)                              |
			| FO    | formula                                                              |                                                          |
			| FU    | unclassified word                                                    |                                                          |
			| FW    | foreign word                                                         |                                                          |
			| GE    | germanic genitive marker                                             | *'*, *'s*                                                |
			| IF    | for (as preposition)                                                 | *for*                                                    |
			| II    | general preposition                                                  | *about*, *on*                                            |
			| IO    | of (as preposition)                                                  | *of*                                                     |
			| IW    | with, without (as prepositions)                                      | *with*, *without*                                        |
			| JJ    | general adjective                                                    | *nice*, *new*                                            |
			| JJR   | general comparative adjective                                        | *older*, *better*, *stronger*                            |
			| JJT   | general superlative adjective                                        | *oldest*, *best*, *strongest*                            |
			| JK    | catenative adjective (able in be able to, willing in be   willing to | *able* (in *be able to*), *willing* (in *be willing to*) |
			| MC    | cardinal number,neutral for number                                   | *two*, *three*                                           |
			| MC1   | singular cardinal number                                             | *one*                                                    |
			| MC2   | plural cardinal number                                               | *sixes*, *sevens*                                        |
			| MCGE  | genitive cardinal number, neutral for number                         | *two's*, *100's*                                         |
			| MCMC  | hyphenated number                                                    | *40-50*, *1770-1827*                                     |
			| MD    | ordinal number                                                       | *first*, *second*, next, *last*                          |
			| MF    | fraction,neutral for number                                          | *quarters*, *two-thirds*                                 |
			| ND1   | singular noun of direction                                           | *north*, *southeast*                                     |
			| NN    | common noun, neutral for number                                      | *sheep*, *cod*, *headquarters*                           |
			| NN1   | singular common noun                                                 | *book*, *girl*                                           |
			| NN2   | plural common noun                                                   | *books*, *girls*                                         |
			| NNA   | following noun of title                                              | *M.A.*                                                   |
			| NNB   | preceding noun of title                                              | *Mr.*, *Prof.*                                           |
			| NNL1  | singular locative noun                                               | *Island*, *Street*                                       |
			| NNL2  | plural locative noun                                                 | *Islands*, *Streets*                                     |
			| NNO   | numeral noun, neutral for number                                     | *dozen*, *hundred*                                       |
			| NNO2  | numeral noun, plural                                                 | *hundreds*, *thousands*                                  |
			| NNT1  | temporal noun, singular                                              | *day*, *week*, *year*                                    |
			| NNT2  | temporal noun, plural                                                | *days*, *weeks*, *years*                                 |
			| NNU   | unit of measurement, neutral for number                              | *in*, *cc*                                               |
			| NNU1  | singular unit of measurement                                         | *inch*, *centimetre*                                     |
			| NNU2  | plural unit of measurement                                           | *ins.*, *feet*                                           |
			| NP    | proper noun, neutral for number                                      | *IBM*, *Andes*                                           |
			| NP1   | singular proper noun                                                 | *London*, *Jane*, *Frederick*                            |
			| NP2   | plural proper noun                                                   | *Browns*, *Reagans*, *Koreas*                            |
			| NPD1  | singular weekday noun                                                | *Sunday*                                                 |
			| NPD2  | plural weekday noun                                                  | *Sundays*                                                |
			| NPM1  | singular month noun                                                  | *October*                                                |
			| NPM2  | plural month noun                                                    | *Octobers*                                               |
			| PN    | indefinite pronoun, neutral for number                               | *none*                                                   |
			| PN1   | indefinite pronoun, singular                                         | *anyone*, *everything*, *nobody*, *one*                  |
			| PNQO  | objective wh-pronoun                                                 | *whom*                                                   |
			| PNQS  | subjective wh-pronoun                                                | *who*                                                    |
			| PNQV  | wh-ever pronoun                                                      | *whoever*                                                |
			| PNX1  | reflexive indefinite pronoun                                         | *oneself*                                                |
			| PPGE  | nominal possessive personal pronoun                                  | *mine*, *yours*                                          |
			| PPH1  | 3rd person sing. neuter personal pronoun                             | *it*                                                     |
			| PPHO1 | 3rd person sing. objective personal pronoun                          | *him*, *her*                                             |
			| PPHO2 | 3rd person plural objective personal pronoun                         | *them*                                                   |
			| PPHS1 | 3rd person sing. subjective personal pronoun                         | *her*, *she*                                             |
			| PPHS2 | 3rd person plural subjective personal pronoun                        | *they*                                                   |
			| PPIO1 | 1st person sing. objective personal pronoun                          | *me*                                                     |
			| PPIO2 | 1st person plural objective personal pronoun                         | *us*                                                     |
			| PPIS1 | 1st person sing. subjective personal pronoun                         | *I*                                                      |
			| PPIS2 | 1st person plural subjective personal pronoun                        | *we*                                                     |
			| PPX1  | singular reflexive personal pronoun                                  | *yourself*, *itself*                                     |
			| PPX2  | plural reflexive personal pronoun                                    | *yourselves*, *themselves*                               |
			| PPY   | 2nd person personal pronoun                                          | *you*                                                    |
			| RA    | adverb, after nominal head                                           | *else*, *galore*                                         |
			| REX   | adverb introducing appositional constructions                        | *namely*, *e.g.*                                         |
			| RG    | degree adverb                                                        | *very*, *so*, *too*                                      |
			| RGQ   | wh- degree adverb                                                    | *how*                                                    |
			| RGQV  | wh-ever degree adverb                                                | *however*                                                |
			| RGR   | comparative degree adverb                                            | *more*, *less*                                           |
			| RGT   | superlative degree adverb (most, least                               |                                                          |
			| RL    | locative adverb                                                      | *alongside*, *forward*                                   |
			| RP    | prep. adverb, particle                                               | *about*, *in*                                            |
			| RPK   | prep. adv., catenative                                               | *about* (in *be about to*)                               |
			| RR    | general adverb                                                       | *quietly*, *importanlty*                                 |
			| RRQ   | wh- general adverb                                                   | *where*, *when*, why, *how*                              |
			| RRQV  | wh-ever general adverb                                               | *wherever*, *whenever*                                   |
			| RRR   | comparative general adverb                                           | *better*, *longer*                                       |
			| RRT   | superlative general adverb                                           | *best*, *longest*                                        |
			| RT    | quasi-nominal adverb of time                                         | *now*, *tomorrow*                                        |
			| TO    | infinitive marker                                                    | *to*                                                     |
			| UH    | interjection                                                         | *oh*, *yes*, *um*                                        |
			| VB0   | be, base form (finite i.e. imperative, subjunctive)                  | *be*                                                     |
			| VBDR  | were                                                                 | *were*                                                   |
			| VBDZ  | was                                                                  | *was*                                                    |
			| VBG   | being                                                                | *being*                                                  |
			| VBI   | be, infinitive                                                       | *be* (in *to be or not...*  or in   *it will be...*)     |
			| VBM   | am                                                                   | *am*                                                     |
			| VBN   | been                                                                 | *been*                                                   |
			| VBR   | are                                                                  | *are*                                                    |
			| VBZ   | is                                                                   | *is*                                                     |
			| VD0   | do, base form (finite                                                | *do*                                                     |
			| VDD   | did                                                                  | *did*                                                    |
			| VDG   | doing                                                                | *doing*                                                  |
			| VDI   | do, infinitive                                                       | *do* (in *I may do...* or in *to do...*)                 |
			| VDN   | done                                                                 | *done*                                                   |
			| VDZ   | does                                                                 | *does*                                                   |
			| VH0   | have, base form (finite                                              | *have*                                                   |
			| VHD   | had (past tense)                                                     | *had*                                                    |
			| VHG   | having                                                               | *having*                                                 |
			| VHI   | have, infinitive                                                     | *have*                                                   |
			| VHN   | had (past participle)                                                | *had*                                                    |
			| VHZ   | has                                                                  | *has*                                                    |
			| VM    | modal auxiliary                                                      | *can*, *will*, *would*                                   |
			| VMK   | modal catenative                                                     | *ought*, *used*                                          |
			| VV0   | base form of lexical verb                                            | *give*, *work*                                           |
			| VVD   | past tense of lexical verb                                           | *gave*, *worked*                                         |
			| VVG   | -ing participle of lexical verb                                      | *giving*, *working*                                      |
			| VVGK  | -ing participle catenative                                           | *going* (in *be going to*)                               |
			| VVI   | infinitive                                                           | *to give...* *It will work...*                           |
			| VVN   | past participle of lexical verb                                      | *given*, *worked*                                        |
			| VVNK  | past participle catenative                                           | *bound* (in *be bound to*)                               |
			| VVZ   | -s form of lexical verb                                              | *gives*, *works*                                         |
			| XX    | not, n't                                                             | *not*, *n't*                                             |
			| ZZ1   | singular letter of the alphabet                                      | *A,b*                                                    |
			| ZZ2   | plural letter of the alphabet                                        | *A's*, *b's*                                             |
		""")
	st.markdown("---")	
	st.markdown("##### DocuScope (Full)")
	st.markdown("""
			| **Tag**                     | **Description**                                                                                                                                                                                                                                                            | **Examples**                                                                                |
			|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
			| Academic Terms              | Abstract, rare, specialized, or disciplinary specific terms that are indicative of informationally dense writing                                                                                                                                                           | *market price*, *storage capacity*, *regulatory*, *distribution*                            |
			| Academic Writing Moves      | Phrases and terms that indicate academic writing moves, which are common in research genres and are derived from the work of Swales (1981) and Cotos et al. (2015, 2017)                                                                                                   | *in the first section*, *the problem is that*, *payment methodology*, *point of contention* |
			| Character                   | References multiple dimensions of a character or human being as a social agent, both individual and collective                                                                                                                                                             | *Pauline*, *her*, *personnel*, *representatives*                                            |
			| Citation                    | Language that indicates the attribution of information to, or citation of, another source.                                                                                                                                                                                 | *according to*, *is proposing that*, *quotes from*                                          |
			| Citation Authorized         | Referencing the citation of another source that is represented as true and not arguable                                                                                                                                                                                    | *confirm that*, *provide evidence*, *common sense*                                          |
			| Citation Hedged             | Referencing the citation of another source that is presented as arguable                                                                                                                                                                                                   | *suggest that*, *just one opinion*                                                          |
			| Confidence Hedged           | Referencing language that presents a claim as uncertain                                                                                                                                                                                                                    | *tends to get*, *maybe*, *it seems that*                                                    |
			| Confidence High             | Referencing language that presents a claim with certainty                                                                                                                                                                                                                  | *most likely*, *ensure that*, *know that*, *obviously*                                      |
			| Confidence Low              | Referencing language that presents a claim as extremely unlikely                                                                                                                                                                                                           | *unlikely*, *out of the question*, *impossible*                                             |
			| Contingent                  | Referencing contingency, typically contingency in the world, rather than contingency in one's knowledge                                                                                                                                                                    | *subject to*, *if possible*, *just in case*, *hypothetically*                               |
			| Description                 | Language that evokes sights, sounds, smells, touches and tastes, as well as scenes and objects                                                                                                                                                                             | *stay quiet*, *gas fired*, *solar panels*, *soft*, *on my desk*                             |
			| Facilitate                  | Language that enables or directs one through specific tasks and actions                                                                                                                                                                                                    | *let me*, *worth a try*, *I would suggest*                                                  |
			| First Person                | This cluster captures first person.                                                                                                                                                                                                                                        | *I*, *as soon as I*, *we have been*                                                         |
			| Force Stressed              | Language that is forceful and stressed, often using emphatics, comparative forms, or superlative forms                                                                                                                                                                     | *really good*, *the sooner the better*, *necessary*                                         |
			| Future                      | Referencing future actions, states, or desires                                                                                                                                                                                                                             | *will be*, *hope to*, *expected changes*                                                    |
			| Information Change          | Referencing changes of information, particularly changes that are more neutral                                                                                                                                                                                             | *changes*, *revised*, *growth*, *modification to*                                           |
			| Information Change Negative | Referencing negative change.                                                                                                                                                                                                                                               | *going downhill*, *slow erosion*, *get worse*                                               |
			| Information Change Positive | Referencing positive change.                                                                                                                                                                                                                                               | *improving*, *accrued interest*, *boost morale*                                             |
			| Information Exposition      | Information in the form of expository devices, or language that describes or explains, frequently in regards to quantities and comparisons                                                                                                                                 | *final amount*, *several*, *three*, *compare*, *80%*                                        |
			| Information Place           | Language designating places.                                                                                                                                                                                                                                               | *the city*, *surrounding areas*, *Houston*, *home*                                          |
			| Information Report Verbs    | Informational verbs and verb phrases of reporting.                                                                                                                                                                                                                         | *report*, *posted*, *release*, *point out*                                                  |
			| Information States          | Referencing information states, or states of being.                                                                                                                                                                                                                        | *is*, *are*, *existing*, *been*                                                             |
			| Information Topics          | Referencing topics, usually nominal subjects or objects, that indicate the “aboutness” of a text                                                                                                                                                                           | *time*, *money*, *stock price*, *phone interview*                                           |
			| Inquiry                     | Referencing inquiry, or language that points to some kind of inquiry or investigation                                                                                                                                                                                      | *find out*, *let me know if you have any questions*, *wondering if*                         |
			| Interactive                 | Addresses from the author to the reader or from persons in the text to other persons. The address comes in the language of everyday conversation, colloquy, exchange, questions, attention getters, feedback, interactive genre markers, and the use of the second person. | *can you*, *thank you for*, *please see*, *sounds good to me*                               |
			| Metadiscourse Cohesive      | The use of words to build cohesive markers that help the reader navigate the text and signal linkages in the text, which are often additive or contrastive                                                                                                                 | *or*, *but*, *also*, *on the other hand*, *notwithstanding*, *that being said*              |
			| Metadiscourse Interactive   | The use of words to build cohesive markers that interact with the reader                                                                                                                                                                                                   | *I agree*, *let’s talk*, *by the way*                                                       |
			| Narrative                   | Language that involves people, description, and events extending in time                                                                                                                                                                                                   | *today*, *tomorrow*, *during the*, *this weekend*                                           |
			| Negative                    | Referencing dimensions of negativity, including negative acts, emotions, relations, and values                                                                                                                                                                             | *does not*, *sorry for*, *problems*, *confusion*                                            |
			| Positive                    | Referencing dimensions of positivity, including actions, emotions, relations, and values                                                                                                                                                                                   | *thanks*, *approval*, *agreement*, *looks good*                                             |
			| Public Terms                | Referencing public terms, concepts from public language, media, the language of authority, institutions, and responsibility                                                                                                                                                | *discussion*, *amendment*, *corporation*, *authority*, *settlement*                         |
			| Reasoning                   | Language that has a reasoning focus, supporting inferences about cause, consequence, generalization, concession, and linear inference either from premise to conclusion or conclusion to premise                                                                           | *because*, *therefore*, *analysis*, *even if*, *as a result*, *indicating that*             |
			| Responsibility              | Referencing the language of responsibility.                                                                                                                                                                                                                                | *supposed to*, *requirements*, *obligations*                                                |
			| Strategic                   | This dimension is active when the text structures strategies activism, advantage seeking, game playing cognition, plans, and goal seeking.                                                                                                                                 | *plan*, *trying to*, *strategy*, *decision*, *coordinate*, *look at the*                    |
			| Uncertainty                 | References uncertainty, when confidence levels are unknown.                                                                                                                                                                                                                | *kind of*, *I have no idea*, *for some reason*                                              |
			| Updates                     | References updates that anticipate someone searching for information and receiving it                                                                                                                                                                                      | *already*, *a new*, *now that*, *here are some*                                             |
			""")
	st.markdown("")					
	st.markdown("---")	
	st.markdown("##### DocuScope (Common Dictionary)")
	st.markdown("The Common Dictionary contains eight primary categories.")
	st.markdown("""
			| Category     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
			|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
			| Actors       | Actors describe the topical focus of a text or its "aboutness". As the metaphor of "actors" suggests, this category accounts for who or what occupies the stage in a text. Of course, in a longer text, a writer will bring a variety of actors on and off the stage, as topics shift from one to another. However, a text's goals and audience will shape the overall composition of a cast. Consider, for example, how the Actors in an ecomomics paper, a literary analysis paper and an economics paper might be balanced somewhat differently. |
			| Citation     | Citation categories relate to the ways in which writers attribute assertions, claims or messages to other sources. Those attributions can assign more authority to a source (e.g., 'the report shows...') or open up space for alternative conclusions (e.g., 'the report suggests...').                                                                                                                                                                                                                                                            |
			| Confidence   | Confidence language signals a writer's attitude toward statements and claims. Think for example about the difference between "it is clear..." versus "it is possible...". The first signals a greater degree of certainty while the latter acknoweldges the potential for alternative interpretations. Note that niether makes the assertion any more or less objective or factual. In fact, most writing requires us to constantly evaluate and modulate our expressions of confidence.                                                            |
			| Organization | Organization refers to the ways in which writers link phrases, sentences, events and claims. Two types of Organization are highlighted: Narrative and Reasoning. We tend to associate Narrative with the telling of stories, particularly in fiction. However, Narrative is also used in academic and professional writing, as well. Think, for example, about how we might organize a lab report or parts of a Methods section. We would likely need to report a clear sequence of events, which would require Narrative.                          |
			| Planning     | The language of planning points forward and can orient readers toward future states or goals.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
			| Sentiment    | The emotional or affective content of a piece of writing is often measured by Sentiment. Is that emotional content largely postive? Or negative?                                                                                                                                                                                                                                                                                                                                                                                                    |
			| Signposting  | Signposts are words or phrases that help readers navigate a text, marking structure, transitions or the carrying out of expected rheorical functions (like the posing of a research question, for example).                                                                                                                                                                                                                                                                                                                                         |
			| Stance       | Stance is related to the "voice" or "tone" of a text and signals writers' commitments and judgments. Stance can encompass a wide range of features, but these categories focus on the ways in which writers can advertise a more assertive or emphatic stance, and the ways they pull back and moderate their stance.                                                                                                                                                                                                                               |	st.markdown("")	
			""")
	st.markdown("")					
	st.markdown("The specific tags are then organized into that basic taxonomy.")	
	st.markdown("""
			| **Tag**                             | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | **Examples**                        |
			|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
			| Actors: Abstractions                | Abstract Actors are more common when communicating to a specialist rather than a general audience. This kind of language can invoke disciplinary specialization or general abstraction, including words with Greek or Latinate suffixes like -logy, -graph, -ability, -esia, -ization (e.g., 'sociology'; 'polygraph'; 'adoptability'; 'kinesia') but also words that are conceptual (e.g., 'automate'; 'factor'; 'paradigm').                                                                                                       | *model*, *information*, *level*     |
			| Actors: First Person                | First Person is active when we forground ourselves, often using pronouns like 'I' or 'we'. First Person Actors are more frequent in interactive contexts like speech and texting, but First Person Actors serve imporant functions in academic writing, as well.                                                                                                                                                                                                                                                                     | *I*, *our*, *we are*                |
			| Actors: People                      | When People are prioritized as Actors, communication foregrounds characters, groups (e.g., 'women', 'men', 'children', 'teenagers'), individuals and particular communities.                                                                                                                                                                                                                                                                                                                                                         | *people*, *individuals*, *she*      |
			| Actors: Public Entities             | When Actors are Public Entities, they reference concepts from public language, media, the language of authority, institutions, and responsibility.                                                                                                                                                                                                                                                                                                                                                                                   | *national*, *society*, *government* |
			| Citation: Authority                 | Authoritative Citation language aligns your text with your source. It advocates a speaker’s or an author’s point of view and reinforces the authority of that point of view. That authority might be located in an external source; however, it might also be assigned to the results or findings of study.                                                                                                                                                                                                                          | *found that*, *shows that*          |
			| Citation: Controversy               | Controversy Citation language acknowledges the source is part of a controversy and may not share the full story.                                                                                                                                                                                                                                                                                                                                                                                                                     | *argues that*, *claims*             |
			| Citation: Neutral                   | Neutral Citation language focuses on the “facts” the source provides rather than investigating its value or persuasiveness. It can be seen as a dispassionate kind of relationship to a source.                                                                                                                                                                                                                                                                                                                                      | *according to*, *discussed*         |
			| Confidence: Hedged                  | Hedged Confidence language signals moderate or flexible certainty and openness to other points of view.                                                                                                                                                                                                                                                                                                                                                                                                                              | *can be*, *may be*                  |
			| Confidence: High                    | High confidence language signals high certainty that would withstand intense debate.                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *it is*, *clearly*                  |
			| Organization: Narrative             | Narrative is used most often to organize events by time (e.g., 'before'; 'after'), but can also be used to sequence them (e.g., 'first of all'; 'finally').                                                                                                                                                                                                                                                                                                                                                                          | *during the*, *after*               |
			| Organization: Reasoning             | Reasoning directs readers from statement to statement by either opening up inferences or blocking inferences. This language can be constructive, meaning that it can connect ideas to form new pathways (e.g., therefore; it stands to reason that). It can also give possible pathways that depend upon contingencies (e.g., 'if this happens, then that can happen'; 'most likely'). Reasoning language can also shut down new pathways by drawing clearly oppositional lines (e.g., 'it is not the case that'; 'refute'; 'deny'). | *results*, *analysis*               |
			| Planning: Future                    | Referencing future actions, states, or desires.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | *will*, *proposed*                  |
			| Planning: Strategy                  | This dimension is active when the text structures activism, advantage-seeking, game-playing cognition, plans and goal-seeking.                                                                                                                                                                                                                                                                                                                                                                                                       | *design*, *decision*                |
			| Sentiment: Negative                 | Referencing dimensions of negativity, including negative acts, emotions, relations, and values.                                                                                                                                                                                                                                                                                                                                                                                                                                      | *corrupted*, *confrontation*        |
			| Sentiment: Positive                 | References positive across a variety of dimensions, including actions, emotions, relations, and values.                                                                                                                                                                                                                                                                                                                                                                                                                              | *health*, *opportunity*             |
			| Signposting: Academic Writing Moves | Academic Writing Moves are typically associated with STEM-oriented research literature. They can refer to how the research was conducted (i.e., how the writer collected and analyzed data). They can also signal results at a descriptive level, as well as analyze and interpret the meaning and overall significance of the reported findings.                                                                                                                                                                                    | *this study*, *method of*           |
			| Signposting: Metadiscourse          | Metadiscourse functions as traffic signs, orienting and directing readers and can include references to oneself as a writer (e.g., 'I argue'), the audience (e.g., 'we can see that'), or the writing itself (e.g., 'in this paper').                                                                                                                                                                                                                                                                                                | *or*, *however*                     |
			| Stance: Emphatic                    | An emphatic stance shows a higher level of force and stronger commitments, judgments or engagements.                                                                                                                                                                                                                                                                                                                                                                                                                                 | *very*, *actually*                  |
			| Stance: Moderated                   | A moderated stance shows a less intense level of commitment or force, judgments or engagements.                                                                                                                                                                                                                                                                                                                                                                                                                                      | *slightly*, *partially*             |
			""")
	
	st.markdown("")	

if __name__ == "__main__":
    main()