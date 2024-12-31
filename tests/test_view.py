import sys
import os
import pytest
from flet import Page, TextField, ElevatedButton, Row, Column, ScrollMode
from view import View

# srcディレクトリをモジュール検索パスに追加
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
)


@pytest.fixture
def setup():
    page = Page()
    view = View(page)
    return view, page


def test_setup_ui(setup):
    view, page = setup
    assert isinstance(view.text_field, TextField)
    assert isinstance(view.open_button, ElevatedButton)
    assert isinstance(view.save_button, ElevatedButton)
    assert isinstance(page.controls[0], Row)
    assert isinstance(page.controls[1], Column)
    assert page.controls[1].scroll == ScrollMode.ALWAYS
    assert page.controls[1].expand


def test_display_content(setup):
    view, _ = setup
    view.display_content("Test content")
    assert view.text_field.value == "Test content"
