"""
A simple currency exchange rate retriever using Google Finance.

This package provides:
- `get_change(currencyA, currencyB, amount)`: Get exchange rate between two currencies.
- `currencies`: A list of supported currency codes.
"""

from .gfinance import get_change, get_stock,currencies

__all__ = {"get_change","get_stock","currencies"}

__version__ = "0.1.0"
__author__ = "Maxichax"