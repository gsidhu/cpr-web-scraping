# cpr-web-scraping
Scrapes data from a bunch of websites.

## Files of interest
1. [`chennai-curler.py`](./chennai-curler.py) and [`chennai-pdf-scraper.py`](./chennai-pdf-scraper.py)
2. [`mumbai-curler.py`](./mumbai-curler.py)
3. [`delhi-curler.py`](./delhi-curler.py) and [`delhi-indi-curler.py'](./delhi-indi-curler.py)
4. [`compile_to_csv.py`](./compile_to_csv.py)
5. [`cpcb_station_params.js`](./cpcb_station_params.js) and [`code`](./cpcb/code/)

1, 2 and 3 get data from the respective websites and store it as CSV files.

4 combines the CSV files into a single file for each website.

5-1 gets the params for each station of interest and after some manual importing, the scripts in 5-2 fetch the data and parse it.

## Notes
* Was going to use [Playwright](https://github.com/microsoft/playwright) to scrape but then figured out a cURL(y) solution. You can see the Playwright implementation in [`scrape-chennai.js`](./scrape-chennai.js).
* Hat tip to [thej](https://github.com/thejeshgn/) for his work on scraping the CPCB dashboard ([repo](https://github.com/thejeshgn/cpcbccr/)).