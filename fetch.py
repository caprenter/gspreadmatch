import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

def run():
	
	scope = ['https://spreadsheets.google.com/feeds']

	credentials = ServiceAccountCredentials.from_json_keyfile_name('varsity-athletics-bdce819be77f.json', scope)

	gc = gspread.authorize(credentials)

	wb = gc.open("Varsity Athletics 2016")


	wks = wb.get_worksheet(1)
	stuff = wks.get_all_values()
	print "Got it!"
	print
	print stuff

if __name__=='__main__':
	run()
