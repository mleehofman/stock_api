"""Modules required for code"""
import asyncio

import pandas as pd
from codetiming import Timer
from helper_functions import AsyncAPIFunctions, ExcelOperations, Globals, TradesOverview
from technical_trade_analysis import TradeTechnicalRequests


async def main():
    """Function to run main"""
    excel_operations = ExcelOperations()
    await excel_operations.clear_sheets()
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
    writer = pd.ExcelWriter(path="analytics_dataframes.xlsx", engine="xlsxwriter")
    Globals.INCOME_STATEMENT.to_excel(writer, sheet_name="INCOME_STATEMENT")
    Globals.FINANCIAL_RATIOS.to_excel(writer, sheet_name="FINANCIAL_RATIOS")
    writer.close()
    t.stop()
