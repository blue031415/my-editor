from model import Model
from view import View
from flet import Page, FilePicker, FilePickerResultEvent, SnackBar, Text


class Controller:
    def __init__(self, model: Model, view: View, page: Page):
        self.model = model
        self.view = view
        self.page = page
        self.file_picker = FilePicker(on_result=self.on_file_picked)
        self.page.overlay.append(self.file_picker)
        self.current_file_path = None
        self.setup_event_handlers()
        self.page.update()

    def setup_event_handlers(self):
        self.view.open_button.on_click = self.open_file
        self.view.save_button.on_click = self.save_file

    def open_file(self, e):
        self.file_picker.pick_files(
            allow_multiple=False, allowed_extensions=["txt"]
        )

    def on_file_picked(self, e: FilePickerResultEvent):
        if e.files and len(e.files) > 0:
            self.current_file_path = e.files[0].path
            try:
                self.model.load_file(self.current_file_path)
                self.view.display_content(self.model.content)
                self.page.snack_bar = SnackBar(
                    content=Text("ファイルを開きました")
                )
            except Exception as ex:
                self.page.show_snack_bar = SnackBar(
                    content=Text(f"ファイルの書き込みに失敗しました\n{ex}")
                )
        else:
            self.page.snack_bar = SnackBar(
                content=Text("ファイルが選択されませんでした")
            )

        self.page.snack_bar.open = True
        self.page.update()

    def save_file(self, e):
        if self.current_file_path:
            try:
                content = self.view.text_field.value
                self.model.save_file(self.current_file_path, content)
                self.page.snack_bar = SnackBar(
                    content=Text("ファイルを保存しました")
                )
            except Exception as ex:
                self.page.snack_bar = SnackBar(
                    content=Text(f"ファイルの保存に失敗しました\n{ex}")
                )
        else:
            self.page.snack_bar = SnackBar(
                content=Text("保存するファイルが選択されていません")
            )
        self.page.snack_bar.open = True
        self.page.update()
