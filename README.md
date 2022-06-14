# cpr-web-scraping
Scrapes data from a bunch of websites.

## How it works
Get data from the respective websites and store it as CSV files –
1. [`chennai-curler.py`](./chennai-curler.py)
2. [`mumbai-curler.py`](./mumbai-curler.py)
3. [`delhi-curler.py`](./delhi-curler.py) and [`delhi-indi-curler.py`](./delhi-indi-curler.py)

Combine the CSV files into a single file for each website using [`compile_to_csv.py`](./compile_to_csv.py).

Get AQI data from CPCBCCR using the [cpcbccr-data-scraper](https://github.com/gsidhu/cpcbccr-data-scraper) repo.

## Notes
* Was going to use [Playwright](https://github.com/microsoft/playwright) to scrape but then figured out a cURL(y) solution. You can see the Playwright implementation in [`scrape-chennai.js`](./archive/scrape-chennai.js).
* Was going to scrape PDFs for Chennai but abandoned that. You can see the code in [`chennai-pdf-scraper.py`](./archive/chennai-pdf-scraper.py).

## License
* This code is licensed under GNU GPL v3
* Please credit by linking to https://thatgurjot.com 