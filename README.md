
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

We provide a number of convenience shell scripts that allow you to rapidly deploy and manage this project on a server. These shells are standardized across the Eberly Center at CMU and you will find the same basic set in every project.

## Using Docker

1. Clone the repository with: git clone https://github.com/CMUEberlyCenter/eberly-docuscope-ca
2. Change into the project directory: cd eberly-docuscope-ca
3. Build the docker image: **./run-dockerfile-build.sh**
4. Run the docker image: **./run-dockerfile.sh**

## Using docker-compose on a production machine

1. Clone the repository with: git clone https://github.com/CMUEberlyCenter/eberly-docuscope-ca
2. Change into the project directory: cd eberly-docuscope-ca
3. Build the docker image: **./run-dockerfile-build.sh**
4. Run the docker image (in dev mode): **./run-compose-dev.sh**

## Local installation on Machine

1. Clone the repository with: git clone https://github.com/CMUEberlyCenter/eberly-docuscope-ca
2. Change into the project directory: cd eberly-docuscope-ca
3. Let Pip install the dependencies and libraries: **./run-install.sh**
4. If successful, execute the application locally on the machine: **./run.sh**

# Shells and DevOps files

* **docker-compose-dev.yml** Development version of the docker-compose configuration. Works the same as the production version except the images aren't automatically restarted. The Compose file is a YAML file defining services, networks, and volumes for a Docker application. The latest and recommended version of the Compose file format is defined by the Compose Specification.
* **docker-compose-prod.yml** Production version of the docker-compose configuration. Meant to be executed as a deamon (see production shell) and all the images are configured to restart automatically. The Compose file is a YAML file defining services, networks, and volumes for a Docker application. The latest and recommended version of the Compose file format is defined by the Compose Specification.
* **Dockerfile** Docker can build images automatically by reading the instructions from a Dockerfile. A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. 
* **run-compose-dev.sh**
* **run-compose-prod.sh**
* **run-dockerfile-build.sh**
* **run-dockerfile.sh**
* **run-install.sh**
* **run.sh**
* **run-upgrade.sh**
