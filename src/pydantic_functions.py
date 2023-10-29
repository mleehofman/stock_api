from typing import List

from pydantic import BaseModel, ValidationError, validator


class ApiHandling(BaseModel):
    """Write data to dataframe

    Parameters:
            BaseModel
    """

    api_key: str
    tradeslist: List[int] = []
    trade: str

    @validator("tradeslist")
    def check_trades_list(cls, tradeslist: list):
        """Checks whether stocks are included in list"""
        if len(tradeslist) < 1:
            raise ValidationError("trades list does not contain enough entries")
        return tradeslist

    @validator("trade")
    def check_length_symbol(cls, symbol: str):
        """Checks whether the symbol is not too long"""
        if len(symbol) > 20:
            raise ValidationError(f"this symbol is too long: {symbol}")
        return symbol
