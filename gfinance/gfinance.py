"""
google_currency.py

A module to retrieve real-time exchange rates and stock value using Google Finance.

Functions:
- `_html_doc(link)`: Converts a webpage link into a readable string.
- `get_change(currencyA, currencyB, amount)`: Fetches exchange rates between two currencies.
- `get_stock(stock,exchange_code,amount)`: Fetches so stock value with the exchange code.

Variables:
- `currencies`: List of supported currency codes.
"""

import urllib.request
from bs4 import BeautifulSoup

def _html_doc(link:str)->str:
    """
    Fetches the HTML content of a given webpage.

    Args:
        link (str): The URL of the webpage.

    Returns:
        str: The HTML content as a string.
    """
    fp = urllib.request.urlopen(link)   #open the link given
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()

    return mystr    # return the string



def get_change(currencyA:str,currencyB:str,amount=1.0)->tuple:
    """
    Fetches the exchange rate between two currencies from Google Finance.

    Args:
        currencyA (str): The base currency code (e.g., 'EUR').
        currencyB (str): The target currency code (e.g., 'USD').
        amount (float, optional): Amount of currencyA to convert. Defaults to 1.0.

    Returns:
        tuple: (Converted amount, Exchange rate) if successful, otherwise (-1, -1).

    Example:
        >>> get_change("EUR", "USD", 2)
        (2.1574, 1.0787)

    Raises:
        AssertionError: If currency codes are not in the `currencies` list.
    """
    #Makes the values uppercase
    currencyA = currencyA.upper()
    currencyB = currencyB.upper()
    
    assert currencyA in currencies and currencyB in currencies,"Selected currencies are not supported"
    
    link = "https://g.co/finance/"+currencyA+"-"+currencyB  # Makes a link like so:"https://g.co/finance/EUR-JPY"
    html = _html_doc(link)   #uses the link to make it readable by bs4
    soup = BeautifulSoup(html, 'html.parser')   #variable made so we can use bs4
    change = [] #a list so only one number is outputed
    
    for classes in soup.find_all('div'):    #finds all the <div><div>
        a = str(classes.div)    #makes it a string
        b = a.find('YMlKec fxKbKc')     #finds all the div where: type="YMlKec fxKbKc"
        string = ""     #creates a new string to put the final value inside
        if b != -1:#checks if the value is found
            for i in range(b+15,b+100):    #removes the "YMlKec fxKbKc" and adds every character after in a string
                if a[i] == '<': #because it's html: 100,01'<' it will allways be like that so ends the loop if '<' to only get the full number
                    break
                string = string + a[i]
            string_verif = ""
            b = len(string)
            for j in range(b):
                if string[j] != ",":
                    string_verif = string_verif + string[j]
                else:
                    for k in range(j+1,b):
                        if string[k] != ".":
                            string_verif = string_verif + string[k]
                        else:
                            break
                    break
            
            if string_verif not in change:    #checks if it already exists to not make duplicates
                change.append(string_verif)
    try:
        a = (float(change[0])*float(amount),float(change[0]))
        return a #returns the final exchange rate*amount of currency being exchnaged
    except:
        try:
            a = (float(change*amount),float(change))
            return a
        except:
            return (-1,-1) # if it can't find the exchange rate returns -1

#All the currencies availabe (there may be more that works if you found one you can add it to this list)
currencies = [
    'AED',  # United Arab Emirates Dirham
    'AFN',  # Afghan Afghani
    'ALL',  # Albanian Lek
    'AMD',  # Armenian Dram
    'ANG',  # Netherlands Antillean Guilder
    'ARS',  # Argentine Peso
    'AUD',  # Australian Dollar
    'AWG',  # Aruban Florin
    'AZN',  # Azerbaijani Manat
    'BAM',  # Bosnia-Herzegovina Convertible Mark
    'BBD',  # Barbadian Dollar
    'BDT',  # Bangladeshi Taka
    'BGN',  # Bulgarian Lev
    'BHD',  # Bahraini Dinar
    'BIF',  # Burundian Franc
    'BMD',  # Bermudan Dollar
    'BND',  # Brunei Dollar
    'BOB',  # Bolivian Boliviano
    'BRL',  # Brazilian Real
    'BSD',  # Bahamian Dollar
    'BTN',  # Bhutanese Ngultrum
    'BWP',  # Botswanan Pula
    'BYN',  # Belarusian Ruble
    'BZD',  # Belize Dollar
    'CAD',  # Canadian Dollar
    'CDF',  # Congolese Franc
    'CHF',  # Swiss Franc
    'CLP',  # Chilean Peso
    'CNY',  # Chinese Yuan
    'COP',  # Colombian Peso
    'CRC',  # Costa Rican Colón
    'CUP',  # Cuban Peso
    'CVE',  # Cape Verdean Escudo
    'CZK',  # Czech Koruna
    'DJF',  # Djiboutian Franc
    'DKK',  # Danish Krone
    'DOP',  # Dominican Peso
    'DZD',  # Algerian Dinar
    'EGP',  # Egyptian Pound
    'ETB',  # Ethiopian Birr
    'EUR',  # Euro
    'FJD',  # Fijian Dollar
    'GBP',  # British Pound Sterling
    'GEL',  # Georgian Lari
    'GHS',  # Ghanaian Cedi
    'GMD',  # Gambian Dalasi
    'GNF',  # Guinean Franc
    'GTQ',  # Guatemalan Quetzal
    'GYD',  # Guyanaese Dollar
    'HKD',  # Hong Kong Dollar
    'HNL',  # Honduran Lempira
    'HTG',  # Haitian Gourde
    'HUF',  # Hungarian Forint
    'IDR',  # Indonesian Rupiah
    'ILS',  # Israeli New Shekel
    'INR',  # Indian Rupee
    'IQD',  # Iraqi Dinar
    'IRR',  # Iranian Rial
    'ISK',  # Icelandic Króna
    'JMD',  # Jamaican Dollar
    'JOD',  # Jordanian Dinar
    'JPY',  # Japanese Yen
    'KES',  # Kenyan Shilling
    'KGS',  # Kyrgystani Som
    'KHR',  # Cambodian Riel
    'KMF',  # Comorian Franc
    'KRW',  # South Korean Won
    'KWD',  # Kuwaiti Dinar
    'KYD',  # Cayman Islands Dollar
    'KZT',  # Kazakhstani Tenge
    'LAK',  # Laotian Kip
    'LBP',  # Lebanese Pound
    'LKR',  # Sri Lankan Rupee
    'LRD',  # Liberian Dollar
    'LSL',  # Lesotho Loti
    'LYD',  # Libyan Dinar
    'MAD',  # Moroccan Dirham
    'MDL',  # Moldovan Leu
    'MGA',  # Malagasy Ariary
    'MKD',  # Macedonian Denar
    'MMK',  # Myanma Kyat
    'MOP',  # Macanese Pataca
    'MRU',  # Mauritanian Ouguiya
    'MUR',  # Mauritian Rupee
    'MVR',  # Maldivian Rufiyaa
    'MWK',  # Malawian Kwacha
    'MXN',  # Mexican Peso
    'MYR',  # Malaysian Ringgit
    'MZN',  # Mozambican Metical
    'NAD',  # Namibian Dollar
    'NGN',  # Nigerian Naira
    'NIO',  # Nicaraguan Córdoba
    'NOK',  # Norwegian Krone
    'NPR',  # Nepalese Rupee
    'NZD',  # New Zealand Dollar
    'OMR',  # Omani Rial
    'PAB',  # Panamanian Balboa
    'PEN',  # Peruvian Nuevo Sol
    'PGK',  # Papua New Guinean Kina
    'PHP',  # Philippine Peso
    'PKR',  # Pakistani Rupee
    'PLN',  # Polish Zloty
    'PYG',  # Paraguayan Guarani
    'QAR',  # Qatari Rial
    'RON',  # Romanian Leu
    'RSD',  # Serbian Dinar
    'RUB',  # Russian Ruble
    'RWF',  # Rwandan Franc
    'SAR',  # Saudi Riyal
    'SBD',  # Solomon Islands Dollar
    'SCR',  # Seychellois Rupee
    'SDG',  # Sudanese Pound
    'SEK',  # Swedish Krona
    'SGD',  # Singapore Dollar
    'SHP',  # Saint Helena Pound
    'SLL',  # Sierra Leonean Leone
    'SOS',  # Somali Shilling
    'SRD',  # Surinamese Dollar
    'SZL',  # Swazi Lilangeni
    'THB',  # Thai Baht
    'TJS',  # Tajikistani Somoni
    'TMT',  # Turkmenistani Manat
    'TND',  # Tunisian Dinar
    'TOP',  # Tongan Paʻanga
    'TRY',  # Turkish Lira
    'TTD',  # Trinidad and Tobago Dollar
    'TWD',  # New Taiwan Dollar
    'TZS',  # Tanzanian Shilling
    'UAH',  # Ukrainian Hryvnia
    'UGX',  # Ugandan Shilling
    'USD',  # US Dollar
    'UYU',  # Uruguayan Peso
    'UZS',  # Uzbekistan Som
    'VES',  # Venezuelan Bolívar Soberano
    'VND',  # Vietnamese Dong
    'XAF',  # Central African CFA Franc
    'XCD',  # East Caribbean Dollar
    'XOF',  # West African CFA Franc
    'XPF',  # CFP Franc
    'YER',  # Yemeni Rial
    'ZAR',  # South African Rand
    'ZMW',  # Zambian Kwacha
    
    'BTC',  # Bitcoin
    'ETH',  # Ethereum
    'LTC',  # Litecoin
    'BCH',  # Bitcoin Cash
    'XRP',  # Ripple
    'DOGE',  # Dogecoin
]


def get_stock(stock:str,exchange_code:str,amount=1.0)->tuple:
    """
    Fetches the stock value according to the exchange code from Google Finance

    Args:
        stock (str): The stock (e.g., 'META').
        exchange_code (str): The exchange code (e.g., 'NASDAQ').
        amount (float, optional): Amount of stock dipslayed. Defaults to 1.0.

    Returns:
        tuple: (stock value amount, stock value) if successful, otherwise (-1, -1).

    Example:
        >>> get_change("META", "NASDAQ", 2)
        (1205.16, 602.58)
    """
    #Makes the values uppercase
    stock = stock.upper()
    exchange_code = exchange_code.upper()
    
    
    link = "https://g.co/finance/"+stock+":"+exchange_code  # Makes a link like so:"https://g.co/finance/BABA34:BVMF"
    html = _html_doc(link)   #uses the link to make it readable by bs4
    soup = BeautifulSoup(html, 'html.parser')   #variable made so we can use bs4
    change = [] #a list so only one number is outputed
    
    for classes in soup.find_all('div'):    #finds all the <div><div>
        a = str(classes.div)    #makes it a string
        b = a.find('YMlKec fxKbKc')     #finds all the div where: type="YMlKec fxKbKc"
        string = ""     #creates a new string to put the final value inside
        if b != -1:#checks if the value is found
            for i in range(b+15,b+100):    #removes the "YMlKec fxKbKc" and adds every character after in a string
                if a[i] == '<': #because it's html: 100,01'<' it will allways be like that so ends the loop if '<' to only get the full number
                    break
                string = string + a[i]
            for i in ['$','¥','€','₹','HK$','C$','£','﷼','kr','A$','R$','zł','CHF','₪','₩','Rp','R','₺']: #because string is outputed like so: €100 we remove the symbol according to the currency
                string = string.strip(i)
            if string not in change:    #checks if it already exists to not make duplicates
                change.append(string)
    try:
        a = (float(change[0])*float(amount),float(change[0]))
        return a #returns the final exchange rate*amount of currency being exchnaged
    except:
        try:
            a = (float(change*amount),float(change))
            return a
        except:
            return (-1,-1) # if it can't find the exchange rate returns -1
        
#print(get_stock("META","NASDAQ",2))