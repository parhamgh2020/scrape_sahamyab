# sahamyab scrape

## setup steps and run:

### config program:

config program from  './config/config.ini' </br>
</br>
[urls] target of scrape </br>
[working_time] start time, end time and days of scrape execution </br>
[mongo] config of mongodb database </br>

### install requirements:

virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
playwright install chromium

### run program:

python3 main.py </br>

## run program with docker-compose

docker-compose up --build -d

