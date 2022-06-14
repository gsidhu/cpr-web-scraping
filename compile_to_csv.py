# Compile to CSV v1
# Author: Gurjot Sidhu
# For: CPR Climate Team, New Delhi
# Description: This script compiles all the data from the individual CSV files for each city

import csv
import os

# Delhi 
# files = os.listdir('./delhi/data/')

# # header = ["Registration No.","Application No.","Name of Deceased","Date of Death","Father's Name","Mother's Name","Place of Death","Permanent Address","Sex"]
# header = ["Registration No.","Date of Death","Place of Death","Sex"]

# with open('./delhi/compiled_data.csv', 'w+') as csvfile:
#   spamwriter = csv.writer(csvfile, delimiter=';')
#   spamwriter.writerow(header)

#   for f in files:
#     if f == '.DS_Store':
#       continue
#     with open('./delhi/data/' + f,'r') as ff:
#       spamreader = csv.reader(ff, delimiter=';')
#       for row in spamreader:
#         if row[0] == 'Registration No.':
#           continue
#         insert_row = [row[0], row[3], row[6],f[-5]]
#         spamwriter.writerow(insert_row)

# Mumbai - 548830
# files = os.listdir('./mumbai/')

# # header = ["Registration No.","Name of Deceased","Address of Deceased","Date of Death","Gender","Name of Father / Husband","Place of Death","Ward"]
# header = ["Registration No.","Date of Death","Gender","Pin code","Place of Death","Ward"]

# with open('./mumbai/compiled_data.csv', 'w') as csvfile:
#   spamwriter = csv.writer(csvfile, delimiter=';')
#   spamwriter.writerow(header)

#   for f in files:
#     if f == '.DS_Store':
#       continue
#     with open('./mumbai/' + f,'r') as ff:
#       spamreader = csv.reader(ff, delimiter=';')
#       for row in spamreader:
#         if row[0] == 'Registration No.':
#           continue
#         try:
#           pincode = row[2].split(', ')[-3]
#         except:
#           pincode = 'NA'
#         insert_row = [row[0], row[3], row[4], pincode, row[6], row[7]]
#         spamwriter.writerow(insert_row)

# Chennai - 670088
files = os.listdir('./chennai/basic_data/')

# header = ["Name of Deceased","Sex","Name of Father/Husband","Date Of Death","Registration No."]
header = ["Date Of Death","Sex","Registration No."]

with open('./chennai/compiled_data.csv', 'w') as csvfile:
  spamwriter = csv.writer(csvfile, delimiter=';')
  spamwriter.writerow(header)

  for f in files:
    if f == '.DS_Store':
      continue
    with open('./chennai/basic_data/' + f,'r') as ff:
      spamreader = csv.reader(ff, delimiter=';')
      for row in spamreader:
        if row[0] == 'Person Name':
          continue
        insert_row = [row[3], row[1], row[4]]
        spamwriter.writerow(insert_row)