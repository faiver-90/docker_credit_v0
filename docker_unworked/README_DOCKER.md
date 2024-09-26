# Installation

## Create directory

## Open command line from directory project

## Clone repo

```
git clone https://github.com/faiver-90/app_v0.git .
```

## Delete 'docker' .env_docker and put .env file in dir (if it doesn't start, ask me for update this file )

## Delete 'docker' from settings.py_docker and change in dir 'app_v0'

## Ask for migration file, put it in credit_v0

## Run Docker

## Up image project (run without --build if not pull from git)

```
docker-compose up --build -d
```

## Pull update from git (from directory with project)

```
git pull
```

## If the application does not appear immediately for a long time

```
docker-compose stop
docker-compose up -d
```

## If you have problem with DB(ex. (1146, "Table 'credit.credit_v0_extrainsurance' doesn't exist")):

- go to Docker->volumes->delete all if this is the only project in docker-> run 'docker-compose up -d'



