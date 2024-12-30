import sys
from io import StringIO
import os

# srcディレクトリをモジュール検索パスに追加
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
)


def test_main_output():
    from main import main

    captured_output = StringIO()
    sys.stdout = captured_output
    main()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == "Hello world"
