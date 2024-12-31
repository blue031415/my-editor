class Model:
    _content: str

    def __init__(self):
        self._content = ""

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content: str):
        self._content = content

    def load_file(self, file_path: str):
        with open(file_path, "r", encoding="utf-8") as f:
            self._content = f.read()

    def save_file(self, file_path: str, content: str):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        self._content = content
