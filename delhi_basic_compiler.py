# Delhi Curler v1
# Author: Gurjot Sidhu
# For: CPR Climate Team, New Delhi
# Description: This script compiles the basic data from all the html files in the `delhi`` folder.

import csv 
import os 
from bs4 import BeautifulSoup

files = os.listdir('./delhi')

csvfile = open('./delhi/basic_data.csv', 'w')
spamwriter = csv.writer(csvfile, delimiter=';')
spamwriter.writerow(["Date of Death", "Name of Deceased", "Father's Name", "Mother's Name", "Sex"])

for f in files:
  filename = './delhi/' + f
  if f in ['.DS_Store', 'delhi_compiled_data.csv', 'data.zip',] or filename == './delhi/data':
    continue

  with open(filename, 'r') as ff:
    ################################
    ### Get all names for date #####
    ################################

    soup = BeautifulSoup(ff.read(), 'html.parser')
    try:
        my_table = soup.find('table', id='gv_DisplayData')
        totalrows = len(my_table.findChildren(['tr']))
    except:
        continue

    cells = soup.findAll('td')
    if len(cells) > 1:
      for r in range(0,len(cells),5):
        row = [
          f[:-7], # date 
          cells[r+1].get_text(strip=True).replace('\n', '').replace('\r', ''),
          cells[r+2].get_text(strip=True).replace('\n', '').replace('\r', ''),
          cells[r+3].get_text(strip=True).replace('\n', '').replace('\r', ''),
          f[11:-5] # sex
        ]
        spamwriter.writerow(row)

csvfile.close()