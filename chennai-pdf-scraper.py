import requests
import csv
import PyPDF2

oldURL = "https://chennaicorporation.gov.in/online-civic-services/death_cert.jsp?registrationNumber="
newURL = "https://gccapp.chennaicorporation.gov.in/birth_death_tn/CORPBIRTHTAMIL/esign/signed_death_"

headers = ["Date of Death", 'Registration No.', 'Name of Deceased', 'Age', 'Sex', "Father's Name", "Mother's Name", "Name of Husband / Wife", "Place of Death", "Address at the time of death", "Permanent address of deceased", "Date of Registration", "Date of Issue"]

## Open basic data CSV file
for d in range(1,2):
  for g in ['M']:
    write_filename = './chennai/full_data/2020-1-' + str(d) + '-' + g + '.csv'
    full_csv = open(write_filename, 'w+')
    spamwriter = csv.writer(full_csv, delimiter=';')
    spamwriter.writerow(headers)

    read_filename = './chennai/basic_data/2020-1-' + str(d) + '-' + g + '.csv'
    with open(read_filename, 'r') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=';')
      count = 0
      for row in spamreader:
        count += 1
        regno = row[4]
        if regno == 'Print':
          continue

        ## Download PDF for that reg no
        with open ("temporary.pdf", "wb") as f:
          try:
            URL = newURL + regno + '.pdf'
            f.write(requests.get(URL, verify=False).content)
          except:
            URL = oldURL + regno
            f.write(requests.get(URL, verify=False).content)
        
        # creating a pdf object 
        pdfFileObj = open('temporary.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(0) 
            
        # extracting text from page 
        text = pageObj.extractText()
        text = text.split('\n')

        try:
          full_row = {
            47: [
              text[37],text[25],text[16],text[31],text[32],text[17],text[18],text[42],text[35] + text[36],text[19] + text[20] + text[21],text[22] + text[23] + text[24],text[26],text[27]
            ],
            46: [
              text[36],text[24],text[16],text[30],text[31],text[17],text[18],text[41],text[34] + text[35],text[19] + text[20] + text[21],text[22] + text[23] + text[24],text[25],text[26]
            ],
            45: [
              text[35],text[23],text[16],text[29],text[30],text[17],text[18],text[40],text[33] + text[34],text[19] + text[20],text[21] + text[22],text[24],text[25]
            ],
            44: [
              text[34],text[23],text[16],text[29],text[30],text[17],text[18],text[39],text[33],text[19] + text[20],text[21] + text[22],text[24],text[25]
            ],
            43: [
              text[34],text[23],text[16],text[29],text[30],text[17],text[18],text[38],text[33],text[19] + text[20],text[21] + text[22],text[24],text[25]
            ],
            42: [
              text[32],text[21],text[16],text[27],text[28],text[17],text[18],text[37],text[31],text[19],text[20],text[22],text[23]
            ],
            41: [
              text[32],text[21],text[16],text[27],text[28],text[17],text[18],text[36],text[31],text[19],text[20],text[22],text[23]
            ]
          }
          # depending on the length of the extracted text, the correct mapping is written to file
          towrite = full_row[len(text)]
        except:
          towrite = ['Data skipped',0,0,0,0,0,0,0,0,0,0,0,0]
        
        ## Add data to new CSV
        spamwriter.writerow(towrite)
        
        pdfFileObj.close()
        
        # if count > 50:
        #   break

    full_csv.close()