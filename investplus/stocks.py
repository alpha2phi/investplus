import requests


def get_stock():
    url = "https://www.investing.com/equities/apple-computer-inc-balance-sheet"
    user_agent = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3 GTB5"
    head = {
        "User-Agent": user_agent,
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "text/html",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    req = requests.get(url, headers=head)

    if req.status_code != 200:
        raise ConnectionError(
            "ERR: error " + str(req.status_code) + ", try again later."
        )

    print(req.text)
    # root_ = fromstring(req.text)
    # path_ = root_.xpath("//div[contains(@class, 'overviewDataTable')]/div")
