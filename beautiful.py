from bs4 import BeautifulSoup
from pprint import pprint as pp

# MUMBAI 
# with open('./mumbai/1-1-2015-M.html') as f:
#     #read File
#     content = f.read()
#     #parse HTML
#     soup = BeautifulSoup(content, 'html.parser')
#     cells = soup.findAll('td')
#     if len(cells) > 1:
#         for r in range(0,len(cells),8):
#             row = [
#                 cells[r+1].get_text(strip=True).replace('\n', ''),
#                 cells[r+2].get_text(strip=True).replace('\n', ''),
#                 cells[r+3].get_text(strip=True).replace('\n', ''),
#                 cells[r+4].get_text(strip=True).replace('\n', ''),
#                 cells[r+5].get_text(strip=True).replace('\n', ''),
#                 cells[r+6].get_text(strip=True).replace('\n', ''),
#                 cells[r+7].get_text(strip=True).replace('\n', ''),
#             ]
#             print(row)



# DELHI

# viewstate = ''
# eventvalidation = ''
# my_table = ''
# totalrows = ''

# with open('response.html') as f:
#     #read File
#     content = f.read()
#     #parse HTML
#     soup = BeautifulSoup(content, 'html.parser')
#     fn = soup.find('input', id='__VIEWSTATE')
#     viewstate = fn['value']
#     fn = soup.find('input', id='__EVENTVALIDATION')
#     eventvalidation = fn['value']
#     my_table = soup.find('table', id='gv_DisplayData')
#     totalrows = my_table.findChildren(['tr'])

with open('./response2_post.html') as f:
    #read File
    content = f.read()
    #parse HTML
    soup = BeautifulSoup(content, 'html.parser')
    cells = soup.findAll('td')
    if len(cells) > 1:
        row = []
        for r in range(0,len(cells),2):
            row.append(cells[r+1].get_text(strip=True))
        print(row)
