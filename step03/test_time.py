import pytest
import sys

from time.py import main

# 正常系確認
def test_main(capfd, mocker):
    test_argments = ["", "100"]
    macker.patch('sys.argv' return_value=test_argments)
    main()
    out, err = capfd.readouterr()
    assert out == '1970-01-01T09:00:01+0900\n'
    assert err == ''
