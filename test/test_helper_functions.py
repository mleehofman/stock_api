# # from pathlib import Path
import asyncio
import unittest

# from src.helper_functions import ApiHandling

# import pytest

# from src.main_async_run import AsyncAPIFunctions

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
        self.assertEqual(x + y, 9)
        return x


class Test(unittest.TestCase):
    """A class to represent a test."""

    async def test_functionality(self):
        """A class to represent a test."""
        result = await async_add(4, 5)
        self.assertEqual(9, result)


async def async_add(x, y, delay=0.1):
    """A class to represent a test."""
    await asyncio.sleep(delay)
    return x + y


if __name__ == "__main__":
    test = testfunction()
    test.test_function()
