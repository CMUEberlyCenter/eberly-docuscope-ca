# Regular image
FROM python:3.10

# Small footprint image
#FROM python:3.7-alpine

COPY . /app
WORKDIR /app

# Expose the ports we're interested in
EXPOSE 8501

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install ffmpeg libsm6 libxext6 -y

RUN pip install streamlit --upgrade
RUN pip install -r requirements.txt

#ENTRYPOINT ["streamlit"]
CMD ["streamlit","run","./corpus_analysis.py","--server.headless","true","--server.port","8501","serverAddress","0.0.0.0"]
