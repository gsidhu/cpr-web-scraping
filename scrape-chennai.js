import fs from 'fs';
import playwright from 'playwright';
let browser = await playwright.chromium.launch({ headless: true, acceptDownloads: true });
const page = await browser.newPage();

let url = "https://chennaicorporation.gov.in/gcc/online-services/death-certificate/"

const YEARS = ['2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010']

const DAY_DROPDOWN = '.dob-select > div:nth-child(1) > select'
const MONTH_DROPDOWN = '.dob-select > div:nth-child(2) > select'
const YEAR_DROPDOWN = '.dob-select > div:nth-child(3) > select'

const MALE_RADIO = '.gender-list > div:nth-child(1) > label > input'
const FEMALE_RADIO = '.gender-list > div:nth-child(2) > label > input'
const TRANS_RADIO = '.gender-list > div:nth-child(3) > label > input'

const CAPTCHA_VALUE = '#txtCaptcha_span'
const CAPTCHA_INPUT = '#captchavalue'

const SUBMIT_BUTTON = '#form-btn1'

const exportPath = './chennai/basic_data'

async function pullData(url) {
  await page.goto(url)
  await page.waitForLoadState();

  for (var y=3;y < 4;d++) { //13 13 32
    for (var m=1; m < 2; m++) {
      for (var d=1;d < 2;d++) {
        let date = [d,m,y]
        await downloadData(page,date, 'M')
        await page.waitForTimeout(5000)
        await downloadData(page,date, 'F')
        await page.waitForTimeout(5000)
        await downloadData(page,date, 'T')
        await page.waitForTimeout(30000)
      }
      await page.waitForTimeout(30000)
    }
  }

  await browser.close();
}

async function downloadData(page, date, gender) {
  // Open #2002
  let day = await page.$(DAY_DROPDOWN)
  let month = await page.$(MONTH_DROPDOWN)
  let year = await page.$(YEAR_DROPDOWN)
  await day.selectOption({ index: date[0]})
  await month.selectOption({ index: date[1]})
  await year.selectOption({ index: date[2]})

  if (gender === 'M' ) {
    await page.check(MALE_RADIO)
  } else if (gender === 'F') {
    await page.check(FEMALE_RADIO)
  } else if (gender === 'T') {
    await page.check(TRANS_RADIO)
  }

  let captcha = await page.textContent(CAPTCHA_VALUE)
  await page.click(CAPTCHA_INPUT)
  await page.keyboard.type(captcha)

  await page.click(SUBMIT_BUTTON)
  await page.waitForLoadState();

  let filename = exportPath

  const allusers = await page.$$eval('.tableBorder > tbody > tr', (users) => {
    return users.map(user => {
        const name = user.querySelector('td:nth-child(1)');
        const sex = user.querySelector('td:nth-child(2)');
        const father = user.querySelector('td:nth-child(3)');
        const dod = user.querySelector('td:nth-child(4)');
        let regno = user.querySelector('td:nth-child(5)');

        if (regno.innerHTML.indexOf('print') > -1) {
          let start = regno.innerHTML.indexOf('print') + 7
          let end = regno.innerHTML.indexOf(",'')") - 1
          regno = regno.innerHTML.substring(start, end)
        }
        else {
          regno = 'Registration No.'
        }
        filename = filename + dod.textContent.trim()
        return {
            name: name.textContent.trim(),
            sex: sex.textContent.trim(),
            father: father.textContent.trim(),
            dod: dod.textContent.trim(),
            regno: regno
        };
    });
  });
  
  console.log(`${allusers.length} users found`);
  // console.dir(allusers);

  filename = filename + '-' + gender + '.json'
  fs.writeFile(filename, JSON.stringify(allusers), function (err) {
    if (err) return console.log(err);
  });
}

pullData(url)