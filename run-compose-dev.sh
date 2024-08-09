clear
docker-compose -f docker-compose-dev.yml up --force-recreate --build --remove-orphans 2>&1 | tee ./docuscope.log
