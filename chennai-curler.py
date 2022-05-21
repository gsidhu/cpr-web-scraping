# Chennai Curler v1
# Author: Gurjot Sidhu
# For: CPR Climate Team, New Delhi
# Description: This script pings the GCC server and saves the result in a CSV file. Data from 01.01.2010 to 31.12.2020 is downloaded by altering the date and gender fields in the request payload.

import time
import requests
from bs4 import BeautifulSoup
import csv

################################
########## Chennai GCC #########
################################

import requests

cookies = {
    'JSESSIONID': 'D2AFE992CBC273D667C90420BF5B472E',
    'language': 'english',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-GB,en-US;q=0.7,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://chennaicorporation.gov.in/gcc/online-services/death-certificate/',
    'Origin': 'https://chennaicorporation.gov.in',
    'DNT': '1',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'JSESSIONID=D2AFE992CBC273D667C90420BF5B472E; language=english',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
}

params = {
    'do': 'getBasicRecords',
}

# years = ['2015', '2014', '2013', '2012', '2011', '2010']
years = ['2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010']

data = {
    'dateOfDeath': '2020-01-01',
    'sel_day': '01',
    'sel_month': '01',
    'sel_year': '2020',
    'Gender': 'M',
    'rd_bd_type': '3',
    'cb_hosp': '',
    'txtCaptcha': '10932452',
    'txtCaptcha_t': '10932452',
    'captchavalue': '10932452',
}

for y in years:
  for m in range(1, 7):
    for d in range(1, 32):
      # skip the 31st in 30-day months
      if m in [4,6,9,11] and d > 30:
        continue
      # if february
      if m == 2:
        # if 29th
        if d == 29:
          # skip if not a leap year
          if y not in ['2012', '2016', '2020']:
            continue
        # skip if 30th or 31st
        elif d > 29:
          continue

      data['sel_day'] = d
      data['sel_month'] = m
      data['sel_year'] = y
      data['dateOfDeath'] = '-'.join([str(y),str(m),str(d)])

      for gender in ['G', 'M', 'F']:
        data['Gender'] = gender
        response = requests.post('https://chennaicorporation.gov.in/online-civic-services/deathCertificateNew.do', params=params, cookies=cookies, headers=headers, data=data)

        filename = './chennai/basic_data/' + data['dateOfDeath'] + '-' + gender
        # with open(filename + '.html', "w") as f:
        #   f.write(response.text)
        #   time.sleep(10)

        ################################
        ##### Extract data to CSV ######
        ################################

        soup = BeautifulSoup(response.text, 'html.parser')

        cells = soup.findAll('td', class_='tableRow')

        if len(cells) > 1:
          with open(filename + '.csv', 'w+', newline='\n') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';',)
            for r in range(0,len(cells),5):
              row = [
                cells[r].get_text(strip=True),
                cells[r+1].get_text(strip=True),
                cells[r+2].get_text(strip=True),
                cells[r+3].get_text(strip=True),
              ]
              if r == 0:
                row.append(cells[r+4].get_text(strip=True))
              else:
                regno = cells[r+4].find('input')['onclick']
                regno = regno[7:regno.index("',")]
                row.append(regno)
              spamwriter.writerow(row)
            
          # time.sleep(5)