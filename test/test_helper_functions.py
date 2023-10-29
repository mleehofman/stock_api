# # from pathlib import Path
import asyncio
import unittest

# from src.helper_functions import Globals

# import pytest

# # from src.main_async_run import AsyncAPIFunctions


# @pytest.mark.asyncio
# async def test_get_api_key() -> None:
#     """
#     Function to test getting the API key
#     :return: None
#     """
#     result_api_key = await asyncio.sleep(3)
#     # AsyncAPIFunctions.async_load_api_keys
#     x = 5
#     y = 10
#     assert result_api_key is None


class testfunction(unittest.TestCase):
    """A class to represent a test."""

    def test_function(self):
        """This is a simple test"""
        x = 4
        y = 5
        print(x + y)
        self.assertEqual(x + y, 9)


class TestHelperFunctions(unittest.IsolatedAsyncioTestCase):
    """A class to represent a test."""

    async def test_api_key(self):
        """This is a simple test"""
        # a = Globals.FINANCIAL_RATIOS
        await asyncio.sleep(0.1)
        print("ok")
        # api_key = await AsyncAPIFunctions.async_load_api_keys()
        # print('ok')
        # self.assertIsNotNone(api_key)


# if __name__ == "__main__":
#     test = testfunction()
#     test.test_function()
