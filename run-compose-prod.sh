clear
docker-compose -f docker-compose-prod.yml up --force-recreate --build --remove-orphans 2>&1 | tee ./docuscope.log

