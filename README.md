# gspreadmatch
Prototype for extracting match JSON from a Google Spreadsheet


This is a quick and dirty proof of concept to score an athletics match.

If this was a general app, it would violate all known security rules, but it
isn't.  A sheet has been createt titled "Varsity Athletics 2016" and I have
downloaded the needed credentials into a JSON file into this repo.


Usage:

	git clone https://github.com/openath/gspreadmatch.git
	cd gspreadmatch
	virtualenv .
	source bin/activate
	pip install -r requirements.txt
	python fetch.py


You should see athletics data.

## Oauth2client version note

gspread's docs are out of date as oauth2client changes in Feb 2016.  I have therefore set an earlier version in the requirements, because I'm busy and lazy.  No doubt a slight change to the fetching code about credentials will work with the later oauth2client.

## Troubleshooting
If the `pip install -r requirements.txt` fails this may be due to unmet dependencies on your host machine.

On Ubuntu 14.04 you may need to run:

  `sudo apt-get install python-cffi`
  
and

  `sudo apt-get install build-essential libssl-dev libffi-dev python-dev`
