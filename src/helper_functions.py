"""Modules required for code"""
import os

import fmpsdk
import openpyxl
import pandas as pd
from dotenv import load_dotenv


class Globals:
    """Definition of dataframes"""

    INCOME_STATEMENT = pd.DataFrame()
    FINANCIAL_RATIOS = pd.DataFrame()


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
        # print("is get_trade_symbols a coroutine")
        # print(type(self.get_trade_symbols))
        # print(inspect.iscoroutinefunction(self.get_trade_symbols))
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

    def write_to_dataframe(self, data, name_df):
        """Function to write to dataframe"""
        print(f"write to dataframe: {self.symbol}")
        df = pd.DataFrame(data)
        # print(data)
        # for col in df.columns:
        #     print(col)

        # Set the title of the DataFrame
        df.name = name_df

        # combined_data = pd.concat([existing_data, data])

        # print(list(df.columns))
        # trade_df = df.append(df, ignore_index=True)

        if name_df == "INCOME_STATEMENT":
            Globals.INCOME_STATEMENT = pd.concat([Globals.INCOME_STATEMENT, df], ignore_index=True)
        if name_df == "FINANCIAL_RATIOS":
            Globals.FINANCIAL_RATIOS = pd.concat([Globals.FINANCIAL_RATIOS, df], ignore_index=True)


class ExcelOperations:
    """Class to perform excel functions"""

    def delete(sheet):
        """Deletes a given sheet"""
        # continuously delete row 2 until there
        # is only a single row left over
        # that contains column names
        while sheet.max_row > 1:
            # this method removes the row 2
            sheet.delete_rows(2)
        # return to main function
        return

    def clear_sheets(self):
        """Obtains all sheets for excel file"""
        # enter your file path
        path = "analytics_dataframes.xlsx"

        # load excel file
        book = openpyxl.load_workbook(path)

        # select the sheet
        sheet = book["INCOME_STATEMENT"]

        print("Maximum rows before removing:", sheet.max_row)

        ExcelOperations.delete(sheet)

        print("Maximum rows after removing:", sheet.max_row)

        # select the sheet
        sheet = book["FINANCIAL_RATIOS"]

        print("Maximum rows before removing:", sheet.max_row)

        ExcelOperations.delete(sheet)

        print("Maximum rows after removing:", sheet.max_row)

        # save the file to the path

        book.save(path)
