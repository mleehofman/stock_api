"""Modules required for code"""
import asyncio
import inspect
import os

import fmpsdk
import pandas as pd
from codetiming import Timer
from dotenv import load_dotenv


class AsyncAPIFunctions:
    """Class for all general API related functions"""

    async def async_load_api_keys(self):
        """Function to load API Key"""
        load_dotenv()
        apikey = os.getenv("FMP_API_KEY")
        return apikey


async def get_income_statement(api_key, symbol):
    """Function to get income statement"""
    result = fmpsdk.income_statement(apikey=api_key, symbol=symbol, period="quarter")
    if len(result) > 0:
        write_to_dataframe(symbol, result)


async def get_financial_ratios(api_key, symbol):
    """Function to get financial ratios"""
    result = fmpsdk.financial_ratios(apikey=api_key, symbol=symbol, period="quarter")
    if len(result) > 0:
        write_to_dataframe(symbol, result)


async def get_trade_info(api_key, symbol):
    """Function to get trade info"""
    t = Timer(name="class")
    t.start()
    print(f"trade {symbol} requested")

    task1 = asyncio.create_task(get_financial_ratios(api_key, symbol))
    task2 = asyncio.create_task(get_income_statement(api_key, symbol))

    await task1
    print(f"Task 1 Done for {symbol}")

    await task2
    print(f"Task 2 Done for {symbol}")

    result = print(inspect.iscoroutinefunction(get_trade_info))

    t.stop()
    return result


async def get_trade_symbols(tradelist):
    """Abstract trabe symbols"""
    symbols = []
    count = 0
    print("is get_trade_symbols a coroutine")
    print(type(get_trade_symbols))
    print(inspect.iscoroutinefunction(get_trade_symbols))
    for count, trade in enumerate(tradelist):
        if count > 10:
            break
        symbols.append(trade["symbol"])
        count += 1
    return symbols


async def main():
    """Function to run main"""
    api_function = AsyncAPIFunctions()
    api_key = await api_function.async_load_api_keys()
    tradelist = fmpsdk.available_traded_list(api_key)
    symbol_list = await get_trade_symbols(tradelist)
    results = await asyncio.gather(*(get_trade_info(api_key, symbol) for symbol in symbol_list))
    return results


def write_to_dataframe(symbol, data):
    """Function to write to dataframe"""
    print(f"write to dataframe: {symbol}")
    df = pd.DataFrame(data)
    return df


if __name__ == "__main__":
    t = Timer(name="class")
    t.start()
    results = asyncio.run(main())
    print(len(results))
    t.stop()
