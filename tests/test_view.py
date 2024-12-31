import sys
import os
from unittest.mock import MagicMock
from flet import Page, Row, Column, ScrollMode


# srcディレクトリをsys.pathに追加
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")),
)
from src.view import View


class TestView:
    def setup_method(self):
        self.page = Page(
            conn=MagicMock(), session_id=MagicMock(), loop=MagicMock()
        )
        self.view = View(self.page)

    def test_setup_ui(self):
        # Check if the Row containing the buttons is added
        assert isinstance(self.page.controls[0], Row)
        assert self.page.controls[0].controls[0] == self.view.open_button
        assert self.page.controls[0].controls[1] == self.view.save_button

        # Check if the Column containing the text field is added
        assert isinstance(self.page.controls[1], Column)
        assert self.page.controls[1].controls[0] == self.view.text_field
        assert self.page.controls[1].scroll == ScrollMode.ALWAYS
        assert self.page.controls[1].expand
