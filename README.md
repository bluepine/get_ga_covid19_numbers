Get covid-19 data for the Georgia of U.S. from https://dph.georgia.gov/covid-19-daily-status-report


Requirements:

Anaconda: https://www.anaconda.com/distribution/

Mongodb: https://www.mongodb.com/

The scripts assume that you can access mongodb at mongodb://localhost:27017


Please refrain from overloading the server. 

Example cron job to fetch the data every hour:
0 * * * * /home/swei/anaconda3/bin/python /home/swei/git/get_ga_covid19_numbers/get_it.py