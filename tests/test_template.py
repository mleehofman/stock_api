from main_app_template import main_app


def test_main_app(mocker):
    patched_request = mocker.patch("main_app_template.urlopen", return_value = "OK")
    result = main_app()
    assert result == "Running"
    assert patched_request.call_count == 1


""" async example"""
# import asyncio
# import pytest

# async def my_func():
#     await asyncio.sleep(0.1)
#     return True


# @pytest.mark.asyncio
# async def test_my_func():
#     r = await my_func()
#     assert r
