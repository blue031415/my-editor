from flet import TextField, Page, ElevatedButton, Column, Row


class View:
    def __init__(self, page: Page):
        self.page = page
        self.text_field = TextField(
            expand=True,
            multiline=True,
            border="underline",
            hint_text="ここにファイルの内容が表示されます",
        )
        self.open_button = ElevatedButton(text="ファイルを開く")
        self.save_button = ElevatedButton(text="保存")
        self.setup_ui()

    def setup_ui(self):
        self.page.add(
            Column(
                [
                    Row([self.open_button, self.save_button]),
                    self.text_field,
                ]
            )
        )

    def display_content(self, content: str):
        self.text_field.vale = content
        self.text_field.update()
