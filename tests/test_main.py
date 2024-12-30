import sys
import pytest
from io import StringIO


def test_main_output():
    from src.main import main

    captured_output = StringIO()
    sys.stdout = captured_output
    main()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == "Hello world"
