import inspect
import os

import fmpsdk
import pandas as pd
from dotenv import load_dotenv


class AsyncAPIFunctions:
    """Class for all general API related functions"""

    async def async_load_api_keys(self):
        """Function to load API Key"""
        load_dotenv()
        apikey = os.getenv("FMP_API_KEY")
        return apikey


class TradesOverview:
    """Obtains stock symbols for analysis

    Parameters:
            api_key (str): api key
    """

    def __init__(self, api_key):
        """Docstring."""
        self.api_key = api_key

    async def get_trade_symbols(self):
        """Abstract trabe symbols"""
        self.tradelist = fmpsdk.available_traded_list(self.api_key)
        symbols = []
        count = 0
        print("is get_trade_symbols a coroutine")
        print(type(self.get_trade_symbols))
        print(inspect.iscoroutinefunction(self.get_trade_symbols))
        for count, trade in enumerate(self.tradelist):
            if count > 10:
                break
            symbols.append(trade["symbol"])
            count += 1
        return symbols


class DataFrameFunctions:
    """Write data to dataframe

    Parameters:
            symbol (str): stock symbol
    """

    def __init__(self, symbol):
        """Docstring."""
        self.symbol = symbol

    def write_to_dataframe(self, data):
        """Function to write to dataframe"""
        print(f"write to dataframe: {self.symbol}")
        df = pd.DataFrame(data)
        print(list(df.columns))
        # trade_df = df.append(df, ignore_index=True)
