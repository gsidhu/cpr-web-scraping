# Notes on Scraping
For: CPR Climate Team (bhargav <bhargav@cprindia.org>)

By: Gurjot Sidhu (gurjot@thatgurjot.com)

## NDMC
Link: https://eservices.ndmc.gov.in/death/

1. Open link
2. Set date
3. Set gender
4. Enter captcha and search
5. Set table size to 100 rows
6. Download table values in format
7. Click Select on first row
8. Agree with popup dialogue
9. Save details
10. Repeat 7-9 for all rows 
11. Repeat 3-10 for all genders
12. Repeat 2-11 for all dates from 01/01/2010 to 31/12/2021

**Data available**
In step 6: 
1. Name
2. Father's name
3. † Mother's name 

In step 9:
1. Registration No.
2. Application No.
3. Name of Deceased
4. Date of Death
5. Father's Name
6. † Mother's Name
7. Place of Death
8. † Permanent Address

† not always available

**Method**
1. Manually search and get an active session ID.
2. Use `pycurl.py` to download the data for all dates and genders.


## Rajkot
Link: https://www.rmc.gov.in/DeathCertificate

1. Open link
2. Set date
3. Download PDF
4. Repeat 2-3 for all dates from 01/01/2010 to 30/09/2020
5. Extract tables from PDFs 

**Data available**
1. Registration number 
2. Name
3. Address

**Concern:** All data is in Gujarati.

## Surat
Link: https://www.suratmunicipal.gov.in/OnlineServices/DeathCertificate/Enroll

1. Set language to English
2. Set date
3. Set gender
4. Enter captcha and search
5. Set table size to 100
6. Download table values in format
7. Repeat 3-6 for all genders
8. Repeat 2-7 for all dates from 01/01/2010 to 31/12/2021

**Data available**
1. Name of deceased
2. Address

**Concerns**
1. Figure out how to enter Captcha. Might have to use OCR but that will increase time requirement manifold.
2. Registration number and Place of death data is available only after signing in. However, there is no way to go back once a record is opened and the search query has to be repeated. Doing so will increase the time needed to scrape manifold.

## Nagpur
Link: http://114.79.182.178:8780/egbnd/SearchReports.do

1. Set to and from dates to one day only as website does not return >300 records in one query
2. Download table values in format
3. Repeat 1-2 for all dates from 01/01/2010 to 31/12/2021

**Data available**
1. Registration No.
2. Date Of Death
3. Name Of the Deceased
4. Sex
5. Place of Death
6. Registration Unit

**Concern:** Registration Date and Age are available on opening each individual record. However, there is no way to go back once a record is opened and the search query has to be repeated. Doing so will increase the time taken manifold.

## Jaipur
Link: http://jaipurmc.org/Dynamic/BirthDeath/DeathSearchCriteria.aspx

1. Set date
2. Set gender
3. Download table values in format
4. Repeat 2-3 for all genders
5. Repeat 1-4 for all dates from 01/01/2010 to 31/12/2021

**Data available**
1. Reg No.
2. Reg Date
3. Name
4. Date of Death
5. Gender
6. Father Name
7. Place of Death
8. Inward No.
9. Book No.
10. Zone Name
11. Address

**Concerns**
1. All data is in Hindi.
2. Though the website says data is updated till April 2022. Search does not return data for many dates especially after 2014. Could be because no deaths actually took place considering how Jaipur is a less populated city. But could also be a lapse in data.

## Mumbai
Link: https://portal.mcgm.gov.in/irj/portal/anonymous/qldeathcert?guest_user=english

1. Set date (01.01.2010 format)
2. Set gender
3. Select ward from dropdown
4. Download table values in format
5. Repeat 3-4 for all wards
6. Repeat 2-5 for all genders
7. Repeat 1-6 for all dates from 01/01/2010 to 31/12/2015

**Data available**
1. Registration No.
2. Name of Deceased
3. Address of Deceased
4. Date of Death
5. Gender
6. Name of Father / Husband
7. Death Place (Hospital / Residence)

**Concern:** Data only available till 31/12/2015

**Methods**
0. Params are 1,2,3 for gender. Ward details are in hacks.md
1. Set parameters and make POST request –
curl 'https://crmapp.mcgm.gov.in:8080/sap(bD1lbiZjPTkwMCZwPTMzNzU0JnY9Ny41MA==)/bc/bsp/sap/ZMCGM_XBSP_DAPP/DAPP_01?sap-params=d19iYWNrPTAlMjAmd19iYWNrMT0xJTIwJndfbmE9MCZ3X2NoZWNrbW9kZT1DUkVBVEUmdl9jeWJyX2NpdD0mdXdzX21vZGU9Q1JFQVRFJnV3c19hcHBsaWNhdGlvbj1DUk1fT1JERVImdXdzX3NlcnZpY2VfaWQ9Wk1fRFRIX0FQUCZ1d3NfZ3VpZD0wOTEwNjkyRDI0NjkxRUVDQjJDMDBDMjU0NUNFQzdEMyZ1d3NfdmVyc2lvbj0wMDAwMDAwMDAx' -X POST -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-GB,en-US;q=0.7,en;q=0.3' -H 'Accept-Encoding: gzip, deflate, br' -H 'Referer: https://crmapp.mcgm.gov.in:8080/sap(bD1lbiZjPTkwMCZwPTMzNzU0JnY9Ny41MA==)/bc/bsp/sap/ZMCGM_XBSP_DAPP/DAPP_01?sap-params=d19iYWNrPTAlMjAmd19iYWNrMT0xJTIwJndfbmE9MCZ3X2NoZWNrbW9kZT1DUkVBVEUmdl9jeWJyX2NpdD0mdXdzX21vZGU9Q1JFQVRFJnV3c19hcHBsaWNhdGlvbj1DUk1fT1JERVImdXdzX3NlcnZpY2VfaWQ9Wk1fRFRIX0FQUCZ1d3NfZ3VpZD0wOTEwNjkyRDI0NjkxRUVDQjJDMDBDMjU0NUNFQzdEMyZ1d3NfdmVyc2lvbj0wMDAwMDAwMDAx' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: https://crmapp.mcgm.gov.in:8080' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Cookie: sap-appcontext=c2FwLXNlc3Npb25pZD1TSUQlM2FBTk9OJTNhUFJTQVBDUk1BUFAwMV9NQ1BfMDElM2FZRTJSa002cFBkaV9vWk1nVkxFaHh0dndpcGVfanp5TjBic3B5OHBtLUFUVA%3d%3d; SAPWP_active=1; sap-usercontext=sap-language=EN&sap-client=900' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: frame' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-User: ?1' -H 'Sec-GPC: 1' --data-raw '%2F%2Fform%2Fsearch=2&%2F%2Fform%2Ffname=&%2F%2Fform%2Fmname=&%2F%2Fform%2Fdod=01.01.2010&%2F%2Fform%2Fgender=2&%2F%2Fform%2Fward2=50000242&uws_next_page=DAPP_02&onInputProcessing%28NEXT_PAGE%29=+Search+&uws_guid=0910692D24691EECB2C00C2545CEC7D3&uws_version=0000000001'
2. Make this GET request and pull out the details –
curl 'https://crmapp.mcgm.gov.in:8080/sap(bD1lbiZjPTkwMCZwPTMzNzU0JnY9Ny41MA==)/bc/bsp/sap/ZMCGM_XBSP_DAPP/DAPP_02?sap-params=d19jaGVja21vZGU9Q1JFQVRFJndfYmFjaz0wJTIwJndfYmFjazE9MSUyMCZ3X25hPTAmdl9jeWJyX2NpdD0mdXdzX21vZGU9Q1JFQVRFJnV3c19hcHBsaWNhdGlvbj1DUk1fT1JERVImdXdzX3NlcnZpY2VfaWQ9Wk1fRFRIX0FQUCZ1d3NfZ3VpZD0wOTEwNjkyRDI0NjkxRUVDQjJDMDBDMjU0NUNFQzdEMyZ1d3NfdmVyc2lvbj0wMDAwMDAwMDAx' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-GB,en-US;q=0.7,en;q=0.3' -H 'Accept-Encoding: gzip, deflate, br' -H 'Referer: https://crmapp.mcgm.gov.in:8080/sap(bD1lbiZjPTkwMCZwPTMzNzU0JnY9Ny41MA==)/bc/bsp/sap/ZMCGM_XBSP_DAPP/DAPP_01?sap-params=d19iYWNrPTAlMjAmd19iYWNrMT0xJTIwJndfbmE9MCZ3X2NoZWNrbW9kZT1DUkVBVEUmdl9jeWJyX2NpdD0mdXdzX21vZGU9Q1JFQVRFJnV3c19hcHBsaWNhdGlvbj1DUk1fT1JERVImdXdzX3NlcnZpY2VfaWQ9Wk1fRFRIX0FQUCZ1d3NfZ3VpZD0wOTEwNjkyRDI0NjkxRUVDQjJDMDBDMjU0NUNFQzdEMyZ1d3NfdmVyc2lvbj0wMDAwMDAwMDAx' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Cookie: sap-appcontext=c2FwLXNlc3Npb25pZD1TSUQlM2FBTk9OJTNhUFJTQVBDUk1BUFAwMV9NQ1BfMDElM2FZRTJSa002cFBkaV9vWk1nVkxFaHh0dndpcGVfanp5TjBic3B5OHBtLUFUVA%3d%3d; SAPWP_active=1; sap-usercontext=sap-language=EN&sap-client=900' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: frame' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-User: ?1' -H 'Sec-GPC: 1'

## Vijaywada
Website gets a server error when fetching query results.

## Chennai
Link: https://chennaicorporation.gov.in/gcc/online-services/death-certificate/advance-search/

1. Set date
2. Set gender
3. Set place of death
4. Enter captcha and search
5. Download table values in format
6. Repeat 3-5 for all places
7. Repeat 2-6 for all genders
8. Repeat 1-7 for all dates from 01/01/2010 to 31/12/2021

**Data available**
1. Person Name
2. Sex
3. Father Name/ Husband Name
4. Date Of Death
5. Registration no. (from click event)

From PDF –
6. Place of death
7. Age
8. Address 

**Method**
0. curl 'https://chennaicorporation.gov.in/online-civic-services/deathCertificateNew.do?do=getBasicRecords' -X POST -H 'User-Agent: Mozillaacintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-GB,en-US;q=0.7,en;q=0.3' -H 'Accept-Encoding: gzip, deflate, br' -H 'Referer: https://chennaicorporation.gov.in/gcc/online-services/death-certificate/' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: https://chennaicorporation.gov.in' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Cookie: language=english; JSESSIONID=49925282CC937D629B9DDD102BE20C3C' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-GPC: 1' -H 'Cache-Control: max-age=0' --data-raw 'dateOfDeath=2018-01-01&sel_day=01&sel_month=01&sel_year=2015&Gender=M&rd_bd_type=3&cb_hosp=&txtCaptcha=737107210&txtCaptcha_t=737107210&captchavalue=737107210'
1. Modfiy the reg. no. and download the PDF from https://chennaicorporation.gov.in/online-civic-services/death_cert.jsp?registrationNumber=2018/08/103A/000014/0 
2. Extract data using `pdf_scraper.py`

# AQI monitor
Link: https://app.cpcbccr.com/ccr/#/caaqm-dashboard-all/caaqm-landing/data

1. Set State
2. Set City
3. Set date range
4. Set station name from dropdown
5. Set 'Select all' for parameters
6. Set criteria to 1-hour
7. Repeat 4-6 for all stations
8. Repeat 3-7 for all dates
9. Repeat 1-8 for all cities

**Concerns**
1. Not all stations have data from 01/01/2010 onwards.
2. The website is really slow to return data. Even for a short time range opening the next page of results does not work.

**Method**
1. Manually set the parameters once for all stations to get the permalink.
2. Modify the date and time in the permalink in batches of 1 month and download the Excel file using Playwright. Set a recognizable filename.
3. Convert all xlsx files to csv.
4. Use R to reorganise the csv file.

Link for Alipur, New Delhi – https://app.cpcbccr.com/ccr/#/caaqm-dashboard-all/caaqm-view-data-report/%2522%257B%255C%2522parameter_list%255C%2522%253A%255B%257B%255C%2522id%255C%2522%253A0%252C%255C%2522itemName%255C%2522%253A%255C%2522PM2.5%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_193%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A1%252C%255C%2522itemName%255C%2522%253A%255C%2522PM10%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_215%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A2%252C%255C%2522itemName%255C%2522%253A%255C%2522NO%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_226%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A3%252C%255C%2522itemName%255C%2522%253A%255C%2522NO2%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_194%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A4%252C%255C%2522itemName%255C%2522%253A%255C%2522NOx%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_225%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A5%252C%255C%2522itemName%255C%2522%253A%255C%2522NH3%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_311%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A6%252C%255C%2522itemName%255C%2522%253A%255C%2522SO2%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_312%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A7%252C%255C%2522itemName%255C%2522%253A%255C%2522CO%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_203%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A8%252C%255C%2522itemName%255C%2522%253A%255C%2522Ozone%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_222%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A9%252C%255C%2522itemName%255C%2522%253A%255C%2522Benzene%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_202%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A10%252C%255C%2522itemName%255C%2522%253A%255C%2522Toluene%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_232%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A11%252C%255C%2522itemName%255C%2522%253A%255C%2522Eth-Benzene%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_216%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A12%252C%255C%2522itemName%255C%2522%253A%255C%2522MP-Xylene%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_240%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A13%252C%255C%2522itemName%255C%2522%253A%255C%2522RH%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_235%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A14%252C%255C%2522itemName%255C%2522%253A%255C%2522WD%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_234%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A15%252C%255C%2522itemName%255C%2522%253A%255C%2522SR%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_237%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A16%252C%255C%2522itemName%255C%2522%253A%255C%2522BP%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_238%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A17%252C%255C%2522itemName%255C%2522%253A%255C%2522AT%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_204%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A18%252C%255C%2522itemName%255C%2522%253A%255C%2522TOT-RF%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_37%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A19%252C%255C%2522itemName%255C%2522%253A%255C%2522RF%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_236%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A20%252C%255C%2522itemName%255C%2522%253A%255C%2522Xylene%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_223%255C%2522%257D%255D%252C%255C%2522criteria%255C%2522%253A%255C%25221%2520Hours%255C%2522%252C%255C%2522reportFormat%255C%2522%253A%255C%2522Tabular%255C%2522%252C%255C%2522fromDate%255C%2522%253A%255C%252201-04-2022%2520T00%253A00%253A00Z%255C%2522%252C%255C%2522toDate%255C%2522%253A%255C%252230-04-2022%2520T23%253A59%253A59Z%255C%2522%252C%255C%2522state%255C%2522%253A%255C%2522Delhi%255C%2522%252C%255C%2522city%255C%2522%253A%255C%2522Delhi%255C%2522%252C%255C%2522station%255C%2522%253A%255C%2522site_5024%255C%2522%252C%255C%2522parameter%255C%2522%253A%255B%255C%2522parameter_193%255C%2522%252C%255C%2522parameter_215%255C%2522%252C%255C%2522parameter_226%255C%2522%252C%255C%2522parameter_194%255C%2522%252C%255C%2522parameter_225%255C%2522%252C%255C%2522parameter_311%255C%2522%252C%255C%2522parameter_312%255C%2522%252C%255C%2522parameter_203%255C%2522%252C%255C%2522parameter_222%255C%2522%252C%255C%2522parameter_202%255C%2522%252C%255C%2522parameter_232%255C%2522%252C%255C%2522parameter_216%255C%2522%252C%255C%2522parameter_240%255C%2522%252C%255C%2522parameter_235%255C%2522%252C%255C%2522parameter_234%255C%2522%252C%255C%2522parameter_237%255C%2522%252C%255C%2522parameter_238%255C%2522%252C%255C%2522parameter_204%255C%2522%252C%255C%2522parameter_37%255C%2522%252C%255C%2522parameter_236%255C%2522%252C%255C%2522parameter_223%255C%2522%255D%252C%255C%2522parameterNames%255C%2522%253A%255B%255C%2522PM2.5%255C%2522%252C%255C%2522PM10%255C%2522%252C%255C%2522NO%255C%2522%252C%255C%2522NO2%255C%2522%252C%255C%2522NOx%255C%2522%252C%255C%2522NH3%255C%2522%252C%255C%2522SO2%255C%2522%252C%255C%2522CO%255C%2522%252C%255C%2522Ozone%255C%2522%252C%255C%2522Benzene%255C%2522%252C%255C%2522Toluene%255C%2522%252C%255C%2522Eth-Benzene%255C%2522%252C%255C%2522MP-Xylene%255C%2522%252C%255C%2522RH%255C%2522%252C%255C%2522WD%255C%2522%252C%255C%2522SR%255C%2522%252C%255C%2522BP%255C%2522%252C%255C%2522AT%255C%2522%252C%255C%2522TOT-RF%255C%2522%252C%255C%2522RF%255C%2522%252C%255C%2522Xylene%255C%2522%255D%257D%2522