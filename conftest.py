# filepath: /c:/Users/blue0/my_editor/tests/conftest.py
from dotenv import load_dotenv
import os
import sys

# .env ファイルを読み込む
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

# srcディレクトリをsys.pathに追加
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")),
)
