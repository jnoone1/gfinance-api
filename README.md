# Google Finance Currency & Stock Fetcher

## Overview
This module allows users to retrieve real-time exchange rates and stock values using data from Google Finance.

**⚠ Disclaimer:** This project is **not affiliated with Google** in any way. It simply extracts publicly available information from Google Finance.

## Features
- Fetch live exchange rates between currencies.
- Retrieve stock values using exchange codes.
- Supports multiple global currencies and stock exchanges.

## Installation
Ensure you have Python installed, then install the required dependencies:
```sh
pip install beautifulsoup4
```

## Usage
### 1️⃣ Fetch Currency Exchange Rate
```python
from google_currency import get_change

converted_value, exchange_rate = get_change("EUR", "USD", 2)
print(converted_value, exchange_rate)
```
**Output Example:**
```
(2.1574, 1.0787)
```

### 2️⃣ Fetch Stock Value
```python
from google_currency import get_stock

stock_value, single_stock_price = get_stock("META", "NASDAQ", 2)
print(stock_value, single_stock_price)
```
**Output Example:**
```
(1205.16, 602.58)
```

## Available Currencies
This module supports major global currencies such as `USD`, `EUR`, `GBP`, `JPY`, `AUD`, and many more. It also supports cryptocurrencies like `BTC`, `ETH`, and `DOGE`.
You can see them all with the currencies list. (There may be more that I forgot feel free to add them)

## Notes
- The script relies on web scraping. If Google changes its webpage structure, the script may break.
- The returned values depend on Google's real-time updates.
- It is recommended to use this module for **personal or educational** purposes only.
- JT edits

## License
This project is licensed under the MIT License. See `LICENSE` for details.

"#gfinance-api" 
