# Delhi Indi Curler v1
# Author: Gurjot Sidhu
# For: CPR Climate Team, New Delhi
# Description: This script reads the html files downloaded by delhi-curler.py and pings the NDMC website to scrape the data for all individuals mentioned in each html file.


import time
import csv
import requests
from bs4 import BeautifulSoup
import os

cookies = {
    'ASP.NET_SessionId': '1wjtpqmpdgdtwxo3soq20hbf',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-GB,en-US;q=0.7,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://eservices.ndmc.gov.in/death/Default.aspx',
    'Origin': 'https://eservices.ndmc.gov.in',
    'DNT': '1',
    'Connection': 'keep-alive',
    # 'Cookie': 'ASP.NET_SessionId=1wjtpqmpdgdtwxo3soq20hbf',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
}

files = os.listdir('./delhi')
donefiles = os.listdir('./delhi/data')

for f in files:
  filename = './delhi/' + f
  if (f.strip('.html') + '.csv') in donefiles or f == '.DS_Store' or filename == './delhi/data':
    continue

  with open(filename, 'r') as ff:
    ################################
    ### Get all names for date #####
    ################################
    viewstate = ''
    eventvalidation = ''

    soup = BeautifulSoup(ff.read(), 'html.parser')
    fn = soup.find('input', id='__VIEWSTATE')
    viewstate = fn['value']
    fn = soup.find('input', id='__EVENTVALIDATION')
    eventvalidation = fn['value']
    try:
        my_table = soup.find('table', id='gv_DisplayData')
        totalrows = len(my_table.findChildren(['tr']))
    except:
        continue

    ################################
    ##### Get individual data ######
    ################################

    eventtarget = ['gv_DisplayData$ctl',str(2),'$btn_Select']

    data = {
        '__EVENTTARGET': eventtarget,
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': viewstate,
        '__EVENTVALIDATION': eventvalidation,
        'gv_DisplayData_length': '10',
        'visited': '2',
    }

    ################################
    ##### Extract data to CSV ######
    ################################
    with open('./delhi/data/' + f.strip('.html') + '.csv', 'w+', newline='\n') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',)
        headerrow = ["Registration No.", "Application No.", "Name of Deceased", "Date of Death", "Father's Name", "Mother's Name", "Place of Death", "Permanent Address"]
        spamwriter.writerow(headerrow)

        all_rows = []
        for i in range(2,totalrows+1):
            if (i < 10):
                eventtarget[1] = '0' + str(i)
            else:
                eventtarget[1] = str(i)
            data['__EVENTTARGET'] = ''.join(eventtarget)

            ## get individual data
            response = requests.post('https://eservices.ndmc.gov.in/death/', cookies=cookies, headers=headers, data=data)

            soup = BeautifulSoup(response.text, 'html.parser')
            cells = soup.findAll('td')

            if len(cells) > 1:
                row = []
                for r in range(0,len(cells),2):
                    row.append(cells[r+1].get_text(strip=True))
                spamwriter.writerow(row)
        
      # time.sleep(5)