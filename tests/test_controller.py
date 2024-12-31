import sys
import os
import pytest
from flet import Page
from controller import Controller
from model import Model
from view import View

# srcディレクトリをモジュール検索パスに追加
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
)


@pytest.fixture
def setup():
    page = Page()
    model = Model()
    view = View(page)
    controller = Controller(page, model, view)
    return controller, page


def test_save_file_success(setup):
    controller, page = setup
    controller.current_file_path = "test.txt"
    controller.view.text_field.value = "Test content"
    controller.save_file(None)
    assert page.snack_bar.content.value == "ファイルを保存しました"


def test_save_file_failure(setup):
    controller, page = setup
    controller.current_file_path = None
    controller.save_file(None)
    assert (
        page.snack_bar.content.value
        == "保存するファイルが選択されていません"
    )
