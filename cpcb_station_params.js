// This script loads the CPCB dashboard and iteratively saves the list of Parameters for each station.
// This list is required when querying the server to pull data using Thej's code.

import fs from 'fs';
import playwright from 'playwright';
let browser = await playwright.chromium.launch({ headless: false, acceptDownloads: true });
const page = await browser.newPage();

let url = "https://app.cpcbccr.com/ccr/#/caaqm-dashboard-all/caaqm-landing/data"

const result = {}

const STATES = ["Delhi", "Tamil Nadu", "Maharashtra"]

const CITIES = ["Delhi", "Chennai", "Mumbai"]

const DELHI_STATIONS_LIST = ["Alipur, Delhi - DPCC", "Anand Vihar, Delhi - DPCC", "Ashok Vihar, Delhi - DPCC", "Aya Nagar, Delhi - IMD", "Bawana, Delhi - DPCC", "Burari Crossing, Delhi - IMD", "CRRI Mathura Road, Delhi - IMD", "Chandni Chowk, Delhi - IITM", "DTU, Delhi - CPCB", "Dr. Karni Singh Shooting Range, Delhi - DPCC", "Dwarka-Sector 8, Delhi - DPCC", "East Arjun Nagar, Delhi - CPCB", "IGI Airport (T3), Delhi - IMD", "IHBAS, Dilshad Garden, Delhi - CPCB", "ITO, Delhi - CPCB", "Jahangirpuri, Delhi - DPCC", "Jawaharlal Nehru Stadium, Delhi - DPCC", "Lodhi Road, Delhi - IITM", "Lodhi Road, Delhi - IMD", "Major Dhyan Chand National Stadium, Delhi - DPCC", "Mandir Marg, Delhi - DPCC", "Mundka, Delhi - DPCC", "NSIT Dwarka, Delhi - CPCB", "Najafgarh, Delhi - DPCC", "Narela, Delhi - DPCC", "Nehru Nagar, Delhi - DPCC", "North Campus, DU, Delhi - IMD", "Okhla Phase-2, Delhi - DPCC", "Patparganj, Delhi - DPCC", "Punjabi Bagh, Delhi - DPCC", "Pusa, Delhi - DPCC", "Pusa, Delhi - IMD", "R K Puram, Delhi - DPCC", "Rohini, Delhi - DPCC", "Shadipur, Delhi - CPCB", "Sirifort, Delhi - CPCB", "Sonia Vihar, Delhi - DPCC", "Sri Aurobindo Marg, Delhi - DPCC", "Vivek Vihar, Delhi - DPCC", "Wazirpur, Delhi - DPCC"]

const CHENNAI_STATIONS_LIST = ["Alandur Bus Depot, Chennai - CPCB", "Arumbakkam, Chennai - TNPCB", "Kodungaiyur, Chennai - TNPCB", "Manali Village, Chennai - TNPCB", "Manali, Chennai - CPCB", "Perungudi, Chennai - TNPCB", "Royapuram, Chennai - TNPCB", "Velachery Res. Area, Chennai - CPCB"]

const MUMBAI_STATIONS_LIST = ["Bandra Kurla Complex, Mumbai - IITM", "Bandra, Mumbai - MPCB", "Borivali East, Mumbai - IITM", "Borivali East, Mumbai - MPCB", "Chakala-Andheri East, Mumbai - IITM", "Chhatrapati Shivaji Intl. Airport (T2), Mumbai - MPCB", "Colaba, Mumbai - MPCB", "Deonar, Mumbai - IITM", "Kandivali East, Mumbai - MPCB", "Khindipada-Bhandup West, Mumbai - IITM", "Kurla, Mumbai - MPCB", "Malad West, Mumbai - IITM", "Mazgaon, Mumbai - IITM", "Mulund West, Mumbai - MPCB", "Navy Nagar-Colaba, Mumbai - IITM", "Powai, Mumbai - MPCB", "Siddharth Nagar-Worli, Mumbai - IITM", "Sion, Mumbai - MPCB", "Vasai West, Mumbai - MPCB", "Vile Parle West, Mumbai - MPCB", "Worli, Mumbai - MPCB"]

const DROPDOWN = "div.toggle:nth-child(2)"
const INPUT = ".filter > input:nth-child(1)"
const STATION_DROPDOWN = "div.col-md-12:nth-child(2) > div:nth-child(1) > div:nth-child(1) > ng-select:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3)"

const PARAMS_LI = 'li.pure-checkbox'

async function pullData(url) {
  await page.goto(url)
  await page.waitForLoadState();

  let s = 2
  
  // Enter STATE
  console.log("stating")
  await page.click(DROPDOWN);
  await page.click(INPUT)
  await page.keyboard.type(STATES[s])
  await page.keyboard.press('Enter')
  // Enter CITY
  await page.click(DROPDOWN);
  await page.click(INPUT)
  await page.keyboard.type(CITIES[s])
  await page.keyboard.press('Enter')
  // Select Station
  let stations = DELHI_STATIONS_LIST
  if (s === 1 ) {
    stations = CHENNAI_STATIONS_LIST
  }
  if (s === 2) {
    stations = MUMBAI_STATIONS_LIST
  }
  for (var t=0; t< stations.length;t++) {
    if (t === 0) { await page.click(DROPDOWN); }
    else { await page.click(STATION_DROPDOWN); }
    await page.click(INPUT)
    await page.keyboard.type(stations[t])
    await page.keyboard.press('Enter')

    // Download Parameters list for station
    // let LIST_PARAMS = []
    let LIS = await page.locator(PARAMS_LI)
    let LIST_PARAMS = await LIS.allInnerTexts()
    let NEW_PARAMS = []
    for (var i=0; i<LIST_PARAMS.length; i++) {
      NEW_PARAMS.push(LIST_PARAMS[i].trim())
    }
    console.log(NEW_PARAMS)

    result[stations[t]] = NEW_PARAMS

    // await page.waitForTimeout(5000)
  }

  fs.appendFile('./cpcb_station_params.json', JSON.stringify(result), function (err) {
    if (err) return console.log(err);
  });

  await browser.close();
}

pullData(url)