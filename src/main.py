import flet
from model import Model
from view import View
from controller import Controller


def main(page):
    print("Hello world")
    page.title = "簡易テキストエディタ"
    page.padding = 20

    model = Model()
    view = View(page)
    Controller(model, view, page)


if __name__ == "__main__":
    flet.app(target=main)
