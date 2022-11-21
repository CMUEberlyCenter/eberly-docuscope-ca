
[![](https://avatars.githubusercontent.com/u/21162269?s=200&v=4)](https://www.cmu.edu/dietrich/english/research-and-publications/docuscope.html)

:speech_balloon: :dolphin: porpoise linguistics 4 everyone

# DocuScope Corpus Analysis

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://browndw-corpus-tagger-corpus-analysis-q1x796.streamlitapp.com/) [![](https://badge.fury.io/py/docuscospacy.svg)](https://badge.fury.io/py/docuscospacy) [![](https://readthedocs.org/projects/docuscospacy/badge/?version=latest)](https://docuscospacy.readthedocs.io/) [![](https://zenodo.org/badge/512227318.svg)](https://zenodo.org/badge/latestdoi/512227318) [![Built with spaCy](https://img.shields.io/badge/made%20with%20❤%20and-spaCy-09a3d5.svg)](https://spacy.io)

## DocuScope and Part-of-Speech tagging with spaCy

This application is designed for the analysis of small corpora assisted by part-of-speech and rhetorical tagging.

With the application users can:

1. process small corpora
2. create frequency tables of words, phrases, and tags
3. calculate associations around node words
4. generate key word in context (KWIC) tables
5. compare corpora or sub-corpora
6. explore single texts
7. practice advanced plotting

# Installation and Running

## Using Docker

1. Clone the repository with: git clone https://github.com/CMUEberlyCenter/eberly-docuscope-ca
2. Change into the project directory: cd eberly-docuscope-ca
3. Build the docker image: ./run-dockerfile-build.sh
4. Run the docker image: ./run-dockerfile.sh

## Using docker-compose on a production machine

1. Clone the repository with: git clone https://github.com/CMUEberlyCenter/eberly-docuscope-ca
2. Change into the project directory: cd eberly-docuscope-ca
3. Build the docker image: ./run-dockerfile-build.sh
4. Run the docker image (in dev mode): ./run-compose-dev.sh

## Local installation on Machine

1. Clone the repository with: git clone https://github.com/CMUEberlyCenter/eberly-docuscope-ca
2. Change into the project directory: cd eberly-docuscope-ca
3. Let Pip install the dependencies and libraries: ./run-install.sh
4. If successful, execute the application locally on the machine: ./run.sh

# Shells and DevOps files

docker-compose-dev.yml
docker-compose-prod.yml
Dockerfile
run-compose-dev.sh
run-compose-prod.sh
run-dockerfile-build.sh
run-dockerfile.sh
run-install.sh
run.sh
run-upgrade.sh
