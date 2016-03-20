import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
from pprint import pprint

def run():
	json_key = json.load(open('varsity-athletics-bdce819be77f.json'))
	scope = ['https://spreadsheets.google.com/feeds']

	credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

	gc = gspread.authorize(credentials)

	wb = gc.open("Varsity Athletics 2016")


	wks = wb.get_worksheet(1)
	stuff = wks.get_all_values()
	print "Got it!"
	print
	print stuff

if __name__=='__main__':
	run()