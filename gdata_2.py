#!/usr/bin/python

import time
import ConfigParser
import gdata.spreadsheet.service

def spread_sheet():
    config = ConfigParser.ConfigParser()
    config.read("/home/mpallavi/Virtualenv/config.cnf")
    email = config.get('client', 'username')
    password = config.get('client', 'password')

    weight = '180'
    # Find this value in the url with 'key=XXX' and copy XXX below
    spreadsheet_key = '1bKB3X8B7gj7RQ-ESNCJfoE1tc7cLtRfxdv0--QDJOXI'
    # All spreadsheets have worksheets. I think worksheet #1 by default always
    # has a value of 'od6'
    worksheet_id = 'od6'

    spr_client = gdata.spreadsheet.service.SpreadsheetsService()
    spr_client.email = email
    spr_client.password = password
    spr_client.source = 'Example Spreadsheet Writing Application'
    spr_client.ProgrammaticLogin()

    # Prepare the dictionary to write
    dict = {}
    dict['date'] = time.strftime('%m/%d/%Y')
    dict['time'] = time.strftime('%H:%M:%S')
    dict['weight'] = weight
    print dict

    entry = spr_client.InsertRow(dict, spreadsheet_key, worksheet_id)
    if isinstance(entry, gdata.spreadsheet.SpreadsheetsList):
      print "Insert row succeeded."
    else:
      print "Insert row failed."



if __name__ == "__main__":
    spread_sheet()
