clear
docker build --tag corpustagger .
docker run -p 8501:8501 corpustagger 2>&1 | tee ./docuscope.log


