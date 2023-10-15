"""Modules required for code"""
import asyncio
import inspect

import fmpsdk
from codetiming import Timer
from helper_functions import DataFrameFunctions


class TradeTechnicalRequests:
    """Handles api requests for technical analysis

    Parameters:
            api_key (str): api key
    """

    def __init__(self, api_key):
        """Docstring."""
        self.api_key = api_key

    async def get_income_statement(self, symbol):
        """Function to get income statement"""
        result = fmpsdk.income_statement(apikey=self.api_key, symbol=symbol, period="quarter")
        self.dataframe = DataFrameFunctions(symbol=symbol)
        if len(result) > 0:
            self.dataframe.write_to_dataframe(data=result)
            print(f"successfully run {symbol}")

    async def get_financial_ratios(self, symbol):
        """Function to get financial ratios"""
        result = fmpsdk.financial_ratios(apikey=self.api_key, symbol=symbol, period="quarter")
        self.dataframe = DataFrameFunctions(symbol=symbol)
        if len(result) > 0:
            self.dataframe.write_to_dataframe(data=result)
            print(f"successfully run {symbol}")

    async def get_trade_info(self, symbol):
        """Function to get trade info"""
        t = Timer(name="class")
        t.start()
        print(f"trade {symbol} requested")

        task1 = asyncio.create_task(self.get_financial_ratios(symbol=symbol))
        task2 = asyncio.create_task(self.get_income_statement(symbol=symbol))

        await task1
        print(f"Task 1 Done for {symbol}")

        await task2
        print(f"Task 2 Done for {symbol}")

        result = print(inspect.iscoroutinefunction(self.get_trade_info))

        t.stop()
        return result
