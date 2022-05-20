import requests
from bs4 import BeautifulSoup

################################
####### NDMC First Search ######
################################
cookies = {
    'ASP.NET_SessionId': 'unokvnghsckcb13bd1qqkw4c',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-GB,en-US;q=0.7,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://eservices.ndmc.gov.in/death/',
    'Origin': 'https://eservices.ndmc.gov.in',
    'DNT': '1',
    'Connection': 'keep-alive',
    # 'Cookie': 'ASP.NET_SessionId=unokvnghsckcb13bd1qqkw4c',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
}

data = {
    '__EVENTTARGET': 'btn_Select',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': '6HGTvE3QkcP65LMtD5vt3bwrj67Oc30oYHDGB6ADq5q9yJg8D25Y8IkL1jzgjchWUdoHhOh++OmDmKpnrQflHHs4ZGPLZ1CV6HIx/E1DyI3KLr/IE2uQVKfyOcNLVRsYvPiE6z4cr60jDfJgqLTE+tf6haGOhtMKDr6BR8W9JYJFiZDjEEBItQ2eTmo++UClOaWzItM5tBjpGbKVBQwZsEkygpG0Fs/y1136V/u7ymf2kFeIz1t07KVTIG77AyAOBZ1Tsphyftpo+4W6rlC7vIAqRYhyfnPGPa6Yn4rqMpIp38IXwCOyhZQOMQ3a7lIeL8QvMIoeEz6hiB0jTF6U66Y4Z1D/kKjnQm0sLhifZ//w0jkuh2Cs7ixuc/HtV2IcrB7B9FC82kcX1sWDnAmOA9F2zqnW7wR98Mg3u3dvZrjJmve45RwvzcuWiNjvely/E1bLv0+lF/8dY+4UFIfsxjqPTMKWFcqXw0hJL9hBgBDHjhIqMZxmrEbB4UCgj6WOBWIHY4YZKTT6aIYTdWDTQgwt8k3lbTelU0+nWkrTfmFuR5fbtQMT1ALPwwedAtfrUMbmBCBD/+sHOHa/UNaIN+rLbPGvHVhsdeUINSHCGIpjn7ZA5UdNoA8CYLd4WR/fR13S9BRH1W8l5+s9UA/l51D6cg6Al6nGVpe3T3MABJMhzltqzkw4HRFFroSbCCON5fUOXr79i79n4m9xOvAcOyDjfQ+nRZI+3pfzwoBTGVH5a37sRYXegPTwgV/0tYAoa69Ja5ASje7Hsf1mJ0UxUk1GKB7Ri3RGToJ5wyuSzLkbOYU4E9rmo6ZtTdndT13MrYh9LoEqGbmQL1K4hOplU5FRHP5qAO4NpL0YZXeLePLTjsj+JgvD840naj2qB53Bjp6gMAPBZOpm0VooYSjbIhQPIn2Thzo59g+YsCe7Ouy4c8IhoC4ToNw3SyC7imjaKkakp5j44fyWQNUWQXT+nPJFxvaePQ/Sm+iDZ9q7N4Tg/OtUHCRMsqIX6KBdS0Zl3qETLPq3FfEco8oqyEC7mAP9lJ65OEoOoTVR9MRbUxkdRnBGlW4CMtCBnCNSa5W21dV9A4vQLQKAKkXgw/K1Wg6mx/sUrJUyBcHs5m2N9WDGQHYt/O3XzWPoaNRNvbsfs4fvRTO9uacWU0sRdFSpKXj3r/R0FWsaaOsClp26fQ6wttNdkUbUwo9Irn/HLuZ10Mi6Ow+90UCBmMbfy387zDLjpW7sj/LZpC4hNsihzCEplKp3A5s2saw9Nz2Oq7tYA+qZWoe407xaoA/JPAPhaU3Xbjmw5lZND1ALqk8CxTp12C651aba0OvzUUAvjQ8XxLrsrGd8Pq2vpNDMkFbzJOPdUkKd7XA+K89CfL57X1q0rkD2xcIIFhDtTMJ/Ov7UO6EfvghzpVs1Fp7+jZOTAABAImjniFCJHTx9NPgA9mfD7Z2RRlE+/UuAftMxTwTy/hNfobut4ZZNgc9ejD0TKgCWoh+/fWHO1yiv8T8ECAMK1Luv0nkGDfmOchitEvVPiKNLXAfHpAB6UhJgWJg/bPN9ILE3mRE+1e87ymTiyyNJUv6dkdtoLuiaqBjgVuD79N/O98HIvSEZ2s+OSKuKfTszFs7HJh9Kv8X1R0UYt8U=',
    '__EVENTVALIDATION': 'zJ6V7t78SJ/vsxeUCg/7QDfoRDmGSdP3xD89G27lbafxqelvVILsxYJoc0QLQV3Uf0Hjoc1k/shIfOvgW8t9Cc302SBdlnUz/N+tbNj1Oi8iM3VjmhKSpqi7AhlmfSqco0KjCe9XQa5L+fSSNuVjbPcH2YKuiKOtT7fStB7OGwN19UxnsAC209FgOoDIrsKtw/oT15LR+IvU4y0nnSLy32glQFHBZEO60lNNVxO712y2/yfEMRUrTC4BKgbKmbxwUX6AlhMj0Ht0fs1nwAWjSFm7EpWCF3CN8Ps7S1GlOd/kUAP9UUUN92HOSYwfiJXzi0vTByuq8Ic6O4RdnZlvBKDGgQjE2UErglKsdHQ5a+gscKDqlv9B7fD8nH4aa9NMKvxpTcLJ9wK+KIn2FIk+Hv/A/OKND1dV++sDGGf3eJq/WnJxfgYNu12SfbxorVmj8uA++rW+5GQPxiKRv8BQUw6lTG6cIoVcktWUd0Zqeyp2ipPxMoH765zUvBtzT3QFDtwHWra0ZtdCxHPjhcPprNePQ2h8gRwFiqwF+xc3TumdPz96kNRwJo2KteL6uGw7cwYojjBDjf75LVDRAJryvE+//L/Q9bkZCXYSDY5GzvK1go27o/QpWFgwvC3E9xsISwrBfG2cc0d9ClOvHoGVS2uxYgmV2fAXEEkxSg3YNK/Pjcf82XUtwZDU/EhGp1WlqHq1SEXUftKrVbi6ry2QQGzYeRG+c9jbb4cR7KJHHW7VtbaIvROSytwxAFsnYrRXdSqVg746MEbK249VdQhNJ8nE9Hfzgmc0vdGBQ8QALz2QZ65cdiW/0I/Oxg4taU61vZ8xQmWuDy6aPQJkxv5BEhb9/hDpsG4IY/Wb500SoXyZFzKtAU5/A9PrmEJMnAuASt8O+5qNQQR8DPGpBEFRswplNub/N4uPlLVVhpbjNsVEWgir+jRZTTkwgdSlF1wj',
    'txt_applicationno': '',
    'txt_registrationno': '',
    'txt_DOB': '',
    'txt_searchDOB': '31-12-2020',
    'ddl_searchgender': 'M',
    'txt_searchFather': '',
    'txt_searchHusband_wife': '',
    'ddl_Paceofbirth': '-1',
    'txt_capcha': '178FA6',
    'visited': '',
}

response = requests.post('https://eservices.ndmc.gov.in/death/', cookies=cookies, headers=headers, data=data)

# with open("response.html", "w") as f:
#   f.write(response.text)

################################
########### MAGIC ##############
################################
viewstate = ''
eventvalidation = ''

soup = BeautifulSoup(response.text, 'html.parser')
fn = soup.find('input', id='__VIEWSTATE')
viewstate = fn['value']
fn = soup.find('input', id='__EVENTVALIDATION')
eventvalidation = fn['value']
my_table = soup.find('table', id='gv_DisplayData')
totalrows = len(my_table.findChildren(['tr']))

################################
####### NDMC Detail Search #####
################################
cookies = {
    'ASP.NET_SessionId': 'unokvnghsckcb13bd1qqkw4c',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-GB,en-US;q=0.7,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://eservices.ndmc.gov.in/death/',
    'Origin': 'https://eservices.ndmc.gov.in',
    'DNT': '1',
    'Connection': 'keep-alive',
    # 'Cookie': 'ASP.NET_SessionId=unokvnghsckcb13bd1qqkw4c',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
}

eventtarget = ['gv_DisplayData$ctl',str(2),'$btn_Select']

data = {
    '__EVENTTARGET': eventtarget,
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': viewstate,
    '__EVENTVALIDATION': eventvalidation,
    'gv_DisplayData_length': '10',
    'visited': '2',
}

## POST request
for i in range(2,totalrows+1):
    if (i < 10):
        eventtarget[1] = '0' + str(i)
    else:
        eventtarget[1] = str(i)
    data['__EVENTTARGET'] = ''.join(eventtarget)
    response = requests.post('https://eservices.ndmc.gov.in/death/', cookies=cookies, headers=headers, data=data)
    filename = "response" + str(i-1) + "_post.html"
    soup = BeautifulSoup(response.text, 'html.parser')
    fn = soup.find('div', id='div_DataDisp')
    with open(filename, "w") as f:
        f.write(str(fn))

#### Instead of saving each file just store the data in a list
#### and write the list as CSV instead