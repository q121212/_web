#!/usr/bin/python3

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('GSpreadsheet-cf991a59cbcd.json', scope)
client = gspread.authorize(creds)

# Open the first sheet in workbook
sheet = client.open("GSpreadsheet").sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)
list_of_hashes = sheet.get_all_values()
print(list_of_hashes)
print(dir(sheet))
# print(sheet.row_values(1))
# print(sheet.col_values(1))
print(sheet.cell(1, 1).value)
sheet.update_cell(1,1, "I would like to")
# row = ["I'm","inserting","a","row","into","a,","Spreadsheet","with","Python"]
# index = 4
# sheet.insert_row(row, index)
print(sheet.findall('fsdfsdg'))
print(sheet.row_count)
sheet.clear()