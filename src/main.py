import flet


def main(page):
    print("Hello world")
    page.title = "初めてのアプリ"
    page.add()


if __name__ == "__main__":
    flet.app(target=main)
