from urllib.request import urlopen


def main_app() -> str:
    """Main App Template Function."""
    url = "https:\\example.com"
    respone = urlopen(url)
    print(respone)
    return "Running"


if __name__ == "__main__":
    main_app()