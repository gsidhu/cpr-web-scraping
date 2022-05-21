# Mumbai Curler v1
# Author: Gurjot Sidhu
# For: CPR Climate Team, New Delhi
# Description: This script pings the BMC server and saves the result as an aggregated CSV file. Data from 01.01.2010 to 31.12.2015 is downloaded by altering the date, gender and ward fields in the request payload.

import time
import requests
from bs4 import BeautifulSoup
import csv
from pprint import pprint as pp

cookies = {
    'sap-appcontext': 'c2FwLXNlc3Npb25pZD1TSUQlM2FBTk9OJTNhUFJTQVBDUk1BUFAwM19NQ1BfMDMlM2FfTEVhN3RRZ2VOWnQ4SkNsdm43dVVRd1o3MzBpTUxhN2tnSEpYQTFuLUFUVA%3d%3d',
    'SAPWP_active': '1',
    'sap-usercontext': 'sap-language=EN&sap-client=900',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-GB,en-US;q=0.7,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://crmapp.mcgm.gov.in:8080/sap(bD1lbiZjPTkwMCZwPTMzNzU0JnY9Ny41MA==)/bc/bsp/sap/ZMCGM_XBSP_DAPP/DAPP_01?sap-params=d19iYWNrPTAlMjAmd19iYWNrMT0xJTIwJndfbmE9MCZ3X2NoZWNrbW9kZT1DUkVBVEUmdl9jeWJyX2NpdD0mdXdzX21vZGU9Q1JFQVRFJnV3c19hcHBsaWNhdGlvbj1DUk1fT1JERVImdXdzX3NlcnZpY2VfaWQ9Wk1fRFRIX0FQUCZ1d3NfZ3VpZD0wOTEwNjkyRDI0NjkxRUVDQjY4NDVENDc1QTkzOUI4OCZ1d3NfdmVyc2lvbj0wMDAwMDAwMDAx',
    'Origin': 'https://crmapp.mcgm.gov.in:8080',
    'DNT': '1',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'sap-appcontext=c2FwLXNlc3Npb25pZD1TSUQlM2FBTk9OJTNhUFJTQVBDUk1BUFAwM19NQ1BfMDMlM2FfTEVhN3RRZ2VOWnQ4SkNsdm43dVVRd1o3MzBpTUxhN2tnSEpYQTFuLUFUVA%3d%3d; SAPWP_active=1; sap-usercontext=sap-language=EN&sap-client=900',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'frame',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
}

params = {
    'sap-params': 'd19iYWNrPTAlMjAmd19iYWNrMT0xJTIwJndfbmE9MCZ3X2NoZWNrbW9kZT1DUkVBVEUmdl9jeWJyX2NpdD0mdXdzX21vZGU9Q1JFQVRFJnV3c19hcHBsaWNhdGlvbj1DUk1fT1JERVImdXdzX3NlcnZpY2VfaWQ9Wk1fRFRIX0FQUCZ1d3NfZ3VpZD0wOTEwNjkyRDI0NjkxRUVDQjY4NDVENDc1QTkzOUI4OCZ1d3NfdmVyc2lvbj0wMDAwMDAwMDAx',
}

data = {
    '//form/search': '2',
    '//form/fname': '',
    '//form/mname': '',
    '//form/dod': '01.01.2015',
    '//form/gender': '1',
    '//form/ward2': '50000042',
    'uws_next_page': 'DAPP_02',
    'onInputProcessing(NEXT_PAGE)': ' Search ',
    'uws_guid': '0910692D24691EECB6845D475A939B88',
    'uws_version': '0000000001',
}

# years = ['2015']
years = ['2015', '2014', '2013', '2012', '2011', '2010']
wards = ["50000225","50000226","50016000","50000227","50002100","50000229","50000230","50000232","50000231","50000234","50000233","50000235","50008904","50000236","50000042","50000150","50000242","50016050","50000076","50000091","50000243","50000238","50000237","50000241","50000240","50000239","50000244","50016279","50000245"]

wardnames = {'50000225': 'A  Ward', '50000226': 'B  Ward', '50016000': 'BHAG', '50000227': 'C  Ward', '50002100': 'CW  Ward', '50000229': 'D  Ward', '50000230': 'E  Ward', '50000232': 'FN  Ward', '50000231': 'FS  Ward', '50000234': 'GN  Ward', '50000233': 'GS  Ward', '50000235': 'HE  Ward', '50008904': 'HO', '50000236': 'HW  Ward', '50000042': 'KE  Ward', '50000150': 'KW  Ward', '50000242': 'L  Ward', '50016050': 'L1 Tunga', '50000076': 'ME  Ward', '50000091': 'MW  Ward', '50000243': 'N  Ward', '50000238': 'PN  Ward', '50000237': 'PS  Ward', '50000241': 'RC  Ward', '50000240': 'RN  Ward', '50000239': 'RS  Ward', '50000244': 'S  Ward', '50016279': 'S1 Lodha', '50000245': 'T  Ward'}

for y in years:
  for m in range(1, 13):
    for d in range(1, 32):
      if y == '2015' and m < 10 and d < 2:
        continue
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

      data['//form/dod'] = '.'.join([str(d),str(m),str(y)])

      for gender in range(1,4):
        data['//form/gender'] = gender
        
        gender = ['M', 'F', 'T'][gender-1]
        filename = './mumbai/' + '-'.join([str(d),str(m),str(y),str(gender)])

        all_wards = []
        
        csvfile = open(filename + '.csv', 'w+', newline='\n')
        spamwriter = csv.writer(csvfile, delimiter=';',)
        ## Add Ward
        for w in wards:
          data['//form/ward2'] = w
        
          # POST request
          requests.post('https://crmapp.mcgm.gov.in:8080/sap(bD1lbiZjPTkwMCZwPTMzNzU0JnY9Ny41MA==)/bc/bsp/sap/ZMCGM_XBSP_DAPP/DAPP_01', params=params, cookies=cookies, headers=headers, data=data)

          # GET request
          headers['Referer'] = 'https://crmapp.mcgm.gov.in:8080/sap(bD1lbiZjPTkwMCZwPTMzNzU0JnY9Ny41MA==)/bc/bsp/sap/ZMCGM_XBSP_DAPP/DAPP_01?sap-params=d19iYWNrPTAlMjAmd19iYWNrMT0xJTIwJndfbmE9MCZ3X2NoZWNrbW9kZT1DUkVBVEUmdl9jeWJyX2NpdD0mdXdzX21vZGU9Q1JFQVRFJnV3c19hcHBsaWNhdGlvbj1DUk1fT1JERVImdXdzX3NlcnZpY2VfaWQ9Wk1fRFRIX0FQUCZ1d3NfZ3VpZD0wOTEwNjkyRDI0NjkxRUVDQjY4NDVENDc1QTkzOUI4OCZ1d3NfdmVyc2lvbj0wMDAwMDAwMDAx'
          params['sap-params'] = 'd19iYWNrPTAlMjAmd19iYWNrMT0xJTIwJndfbmE9MCZ3X2NoZWNrbW9kZT1DUkVBVEUmdl9jeWJyX2NpdD0mdXdzX21vZGU9Q1JFQVRFJnV3c19hcHBsaWNhdGlvbj1DUk1fT1JERVImdXdzX3NlcnZpY2VfaWQ9Wk1fRFRIX0FQUCZ1d3NfZ3VpZD0wOTEwNjkyRDI0NjkxRUVDQjY4NDVENDc1QTkzOUI4OCZ1d3NfdmVyc2lvbj0wMDAwMDAwMDAx'

          response = requests.get('https://crmapp.mcgm.gov.in:8080/sap(bD1lbiZjPTkwMCZwPTMzNzU0JnY9Ny41MA==)/bc/bsp/sap/ZMCGM_XBSP_DAPP/DAPP_02', params=params, cookies=cookies, headers=headers)
          # with open(filename + '.html', "w") as f:
          #   f.write(response.text)

          ################################
          ##### Extract data to CSV ######
          ################################

          soup = BeautifulSoup(response.text, 'html.parser')

          cells = soup.findAll('td')

          if len(cells) > 1:
            for r in range(0,len(cells),8):
              row = [
                cells[r+1].get_text(strip=True).replace('\n', '').replace('\r', ''),
                cells[r+2].get_text(strip=True).replace('\n', '').replace('\r', ''),
                cells[r+3].get_text(strip=True).replace('\n', '').replace('\r', ''),
                cells[r+4].get_text(strip=True).replace('\n', '').replace('\r', ''),
                cells[r+5].get_text(strip=True).replace('\n', '').replace('\r', ''),
                cells[r+6].get_text(strip=True).replace('\n', '').replace('\r', ''),
                cells[r+7].get_text(strip=True).replace('\n', '').replace('\r', ''),
              ]
              if r == 0:
                row.append('Ward')
              else:
                row.append(wardnames[w])
              
              if r == 0 and len(all_wards) > 0:
                continue
              else:
                all_wards.append(row)
        
        for rrr in all_wards:
          spamwriter.writerow(rrr)

        csvfile.close()
          # time.sleep(2)