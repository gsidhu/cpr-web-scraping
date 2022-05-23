import csv
import os


# Delhi 
# files = os.listdir('./delhi/data/')

# header = ["Registration No.","Application No.","Name of Deceased","Date of Death","Father's Name","Mother's Name","Place of Death","Permanent Address"]

# with open('./delhi/compiled_data.csv', 'w') as csvfile:
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
#         spamwriter.writerow(row)


# Mumbai
# files = os.listdir('./mumbai/')

# header = ["Registration No.","Name of Deceased","Address of Deceased","Date of Death","Gender","Name of Father / Husband","Place of Death","Ward"]

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
#         spamwriter.writerow(row)

# Chennai
files = os.listdir('./chennai/basic_data/')

header = ["Name of Deceased","Sex","Name of Father/Husband","Date Of Death","Registration No."]

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
        spamwriter.writerow(row)
