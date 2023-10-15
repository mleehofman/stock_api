"""Modules required for code"""
import asyncio

from codetiming import Timer
from helper_functions import AsyncAPIFunctions, TradesOverview
from technical_trade_analysis import TradeTechnicalRequests


async def main():
    """Function to run main"""
    api_function = AsyncAPIFunctions()
    api_key = await api_function.async_load_api_keys()
    trades = TradesOverview(api_key=api_key)
    symbol_list = await trades.get_trade_symbols()
    trades_request = TradeTechnicalRequests(api_key=api_key)
    results = await asyncio.gather(*(trades_request.get_trade_info(symbol) for symbol in symbol_list))
    return results


if __name__ == "__main__":
    t = Timer(name="class")
    t.start()
    results = asyncio.run(main())
    t.stop()
