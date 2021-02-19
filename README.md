# Parser, API, Client for Trademark and Design data from EUIPO

## Data

The xml files are inside parser/data split in a trademark and design folder.
There are a couple of example folders/files there with data thats included but you
need to download the files yourself and move it there if you want more data.
Did test with 90k files (multiple GBs) but I will not be including multiple GBs of files in git

## Run it

### Start db

This creates a postgres database and runs init.sql

```
docker-compose -f dev.docker-compose.yml up --build
```

### Create python venv and activate (inside /parser)

```
python3 -m venv env
source /env/bin/activate
pip3 install -r requirements.txt
```

### Parse data (inside /parser)

```
python3 main.py
```

### Start api (inside /api)

```
npm intall -> only first time
npm start dev
```

### Start web client (/web-client)

```
npm start
```

visit http://localhost:3000
