# Delhi Curler v1
# Author: Gurjot Sidhu
# For: CPR Climate Team, New Delhi
# Description: This script pings the NDMC server and saves the result as an html file. Data from 01.01.2010 to 31.12.2020 is downloaded by altering the date and gender fields in the request payload.

import time
import csv
import requests
from bs4 import BeautifulSoup

################################
####### NDMC First Search ######
################################
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

data = {
    '__EVENTTARGET': 'btn_Select',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': 'dNBlJXvhxKyfzyKzQ4278ZnQc7sv7rXjtsfzuzQrKPY4K5GrpaA0Ms0RoOtxgkfjl2OFjIm8WYq+F+UGqknZU2+1tpRJpa1wbQl4qR1257NLzuUDhxCxZvSJ7M6lAWT1YUSz4h3HdYzPwG/U0IipBBQHuvaQGOfVSVLLNS0mokaUjYE2iR1upOj2VjWyfXhLAV1mjkYQ3LwIO0OrbibxRWXcvyslhLsrqwt9h0Yps51t6pYM+mqbYRGGNBPV91ak4tjCUtaGOjKoFEc9dlZ6pJYCe/TGv5PYWar6J/cLN0x9kcSjPDBn0j80bCGW/zycZ/yhagDqpuZd9yKJWNYUbAc1TVe8l/rDEHEm1yYjYklLKTFYB8wq0TRzAnjF8TXojxbylKexUaNpweNmdAKe0fEcsWIIaksLdNd1jCHrkxC39vMULJWhiajUv6O8Med+bPsEn5oXFipoHJfhjEdVJUZHiDINskjkZ18r3El227Jh7tjoBavh4yDGIb5kGPosLZ4SzSnx6OHQXSbBTWzwNtJGe8EKanbT7ILVH/CrWKVg9TlKKidgT0KP5BsRRql2TnY6OO+y63RZfu3ghzoJfeVhrt3G43+K7+usI4PB1DQ7FjgfJuwiWZao1DVuS3130xqb9TMvQ9DA3jXclcAsxTqIeMoBIaXcmLqxRgBLSOrLLIzyqc9EiGS+r/mcAjBxCEnBnNOG6qzhVmfwPrBWfzCUx3OWiVgi+JGAsWx4KngOobWTgeln7nxa3FDA6Fi1cdnf1VsH489jHonKbebrDlqkcRv7Zs2pjfKYvwskWXnZrp0R6RkinnJ+ewoqLakldxTaQlqq7dLyEPlWsDiHigkmyJT5mBd97UIJAyMAzXSC/Xhk+Vn9eFLlEf33ZMcd7EN8Q+p6jAXfUygtheOv6AAHZlMOMvuiLn9mLAOxoT/NfxGHPLQRwMKGT2crQaNg0bG26g2OtY8kIlSz1FQHKODa11Wfye55D5u9JQ4SM+cM8NH0Us40+BKKuaECJDqSEi88VwNWL13oA/sqJKz+2KoUv2IWTpeK8jaD7h3Ydgabu4/CQve8yaunarV8YXKHupc3HrOHbIAmHQrB8LItDlsvLYEtn+6r4CRsH+rEL4snHvHPpM/X7y0ZndMtZm9OrXtwGE+oAch+zBaU8+LVg1MgptgijB1ZUnvqctMzvfVcPohO7lm+X01kI4tv3KGRvg8T/JWxYzw3nZ9F3N+HH0xCiYSrNX7VoGB/nwrw7i4dE/RtEv+1pY9meG4vUR3rOLj91GYFoSaHvDOPuxgE+gZwZqdl8szN5+knQvaAeXpI0f6eouWxqAbHSN5wIBu9eYqsWMP/4dtF8QWs+wtZ1juMHFKKyj7iRVj9wUyyGmES1h+mTyBvDyxW4x2nPrAmdOBXS82hk1GU6H5PFjFDHzU3V8eWgwGRdE5sw0o71+7W/TS2VMPPscg1+DFXf+20TP0DR16vBlCU7asDuDBiGaXs+6J9vm/yjRczqvgDsNteVkwSN9oZZWgqe6qiZWuHJBCY4wQ6f76ajCeHBgXWXzwG8FJxF6mTR5iOBee4/Ip3DE7rLn1YCvX8ys2pND+5MRnR9mO6lvgQDvV5BKrskAOU7NsI2/AQpSm3kvafcVg=',
    '__EVENTVALIDATION': 'oxkiWhj9yOUvDyjgdiRqrIUiOdSWXbWpGm6bYPcAYmkmDCZRrPwsJ0ivAceB/zidFGocUPiMYl2LjCM+3SoAtPcpmF0NjdYrm6ZSOSJj26+0gyZ0j/qOnFrP9mRw+l1/E+XPS/glk5yC6CM35uKcFgBWuTzZdzfPWPET+ojZDUyD0si9c2XvDpqDyyvRUr0OLeQbLY9cSjX/lWYz7wy4OpMaSKnGEClgWrnTefBvK0/KsMRRi0BocAWkagVZNXWAevr9RziqceBYirjOsGugUXdkBx6E0cj2j6IgzX6iABbOplmRKoUF4MDN/2owm4MYc1Zq1TVE/PYyck+IC1GVgo1n/EZEr2+/kZ9GlMfXze7NTLODzU9J3AkYWyWVg+x08ve6fx7L0ZA8+Hr9dsCSAFhaL7NAhGjY9fjn1zY1bHWLzHvhLX/cwqkiAQ8nwP/TLbNGkigqZfE9Fx62seofCyB7iPUhxJWT/Q4CEbdJcqcVc50Q+dmEUDg/SRthgYN5Kb8Iz0hIKpF2eXxDTWYmVyg//8xlR6Ud+lwJAU9g+g7F1uOe660N0aDOIn5OHW2vxXvESWGoXMrotp8dJ4bgRTIMVkPGwzJ0X5P4qKqzGxRYU/eguk/WfBsrr2iFyOSr9Bow0r41+LDd9bXfPK6AJ0KDDXpvXjLQm/s4E6YshZ1HsQ9ruiK7WU8IONDmCjEZta9TN43BO1ifcQUcOX/67UYJJtjv4cLcIsH89juDLDYCs7o+3hIlEeFLM89SaVDfse2mc8tK5nVUjmFnEGMJo5rO71Fms7TPQWff/CelLYyHi5iVuRUPvZd09ZJEtElS9jS8UPmbnNIz9BZuNMGmVPGQgLW8lO0PGeqQl/23Em6IBCaOoMOk/n51wdA8nihE/rvTv41xgQSLKNm84bkn02NA9DyCq1NP4UL93jsqF3bfU0yw2vT+cvJvbEQDQAjv',
    'txt_applicationno': '',
    'txt_registrationno': '',
    'txt_DOB': '',
    'txt_searchDOB': '01-01-2010',
    'ddl_searchgender': 'M',
    'txt_searchFather': '',
    'txt_searchHusband_wife': '',
    'ddl_Paceofbirth': '-1',
    'txt_capcha': '841744',
    'visited': '',
}

years = ['2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010']
# years = ['2010']

for y in years:
  for m in range(1, 13):
    for d in range(2,32):
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
      mm = m
      dd = d
      if m < 10:
        mm = '0' + str(m)
      if d < 10:
        dd = '0' + str(d)
      
      data['txt_searchDOB'] = '-'.join([str(dd),str(mm),str(y)])

      for gender in ['NA', 'M', 'F']:
        data['ddl_searchgender'] = gender
        response = requests.post('https://eservices.ndmc.gov.in/death/', cookies=cookies, headers=headers, data=data)

        soup = BeautifulSoup(response.text, 'html.parser')
        my_table = soup.find('table', id='gv_DisplayData')
        if type(my_table) == type(None):
            continue

        filename = './delhi/' + '-'.join([str(d),str(m),str(y),gender])
        with open(filename + '.html', "w") as f:
          f.write(response.text)
        #   time.sleep(10)
