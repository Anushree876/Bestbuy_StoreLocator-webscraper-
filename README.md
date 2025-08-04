# Best Buy Store Locator Scraper

This Python script uses **Selenium** to scrape store details from [BestBuy.com](https://www.bestbuy.com) based on a specified ZIP code.

## ✅ Features

- Navigates to the Best Buy store locator
- Inputs a ZIP code (`10001` by default)
- Extracts details from the **first 5** store listings:
  - Store name
  - Address
  - Contact information
  - Store rating
  - Available services
- Saves the data to `data.csv`

---

## 📦 Requirements

- Python 3.7+
- Google Chrome browser
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (must match your installed Chrome version)
- Selenium

### Install Selenium:

```bash
pip install selenium
