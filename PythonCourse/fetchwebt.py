import requests, sys

def fetchtitle(url) -> str:
    title = ""
    try:
        res = requests.get(url)
        page = res.text
        titlestart = page.lower().find("<title>")
        titleend = page.lower().find("</title>")
        title = page[titlestart+7:titleend]
    except:
        title = "Title fetching failed."
    # Add requests here
    return title


def main() -> int:
    print(fetchtitle(input("Web page: ")))
    return 0

if __name__ == '__main__':
    sys.exit(main())

