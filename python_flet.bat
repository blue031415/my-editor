@echo off

REM 仮想環境のディレクトリが存在するか確認
IF EXIST .venv (
    REM 存在する場合は削除
    rmdir /s /q .venv
)

REM 新しい仮想環境を作成
python -m venv .venv

REM 仮想環境をアクティベート
call .venv\Scripts\activate

REM 必要なパッケージをインストール
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\pip.exe install -r requirements.txt