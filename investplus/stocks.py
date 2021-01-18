import requests
import re
from lxml.html import fromstring


def get_stock_balance_sheet():
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

    root_ = fromstring(req.text)
    path_ = root_.xpath("//*[@id='rrtable']/table")
    if path_:
        for elements_ in path_:
            # Balance sheet dates
            balance_sheet_dates = _extract_balance_sheet_dates(elements_)

            # Total current assets
            total_current_assets = _extract_total_current_assets(
                elements_, balance_sheet_dates
            )

            # Total assets
            total_assets = _extract_total_assets(elements_, balance_sheet_dates)

            # Total current liabilities
            total_current_liabilities = _extract_current_liabilities(
                elements_, balance_sheet_dates
            )

            # Total liabiities
            total_liabilities = _extract_total_liabilities(
                elements_, balance_sheet_dates
            )
    else:
        raise RuntimeError("ERR: data retrieval error while scraping.")


def _extract_balance_sheet_dates(elements):
    """
    Extract budget dates to a list. Date format is dd/mm/yyyy.
    """
    # Extract years. Use python reg. Can also use lxml exslt
    years = list()
    nodes = elements.xpath(".//*[@id='header_row']/th/span")
    for node in nodes:
        match = re.search(r"\d\d\d\d", node.text_content().strip())
        if match:
            years.append(match.string)

    # Extract month and day
    month_days = list()
    nodes = elements.xpath("//*[@id='header_row']/th/div")
    for node in nodes:
        match = re.search(r"\d\d/\d\d", node.text_content().strip())
        if match:
            month_days.append(match.string)

    # Budget timestamps
    return ["/".join(map(str, i)) for i in zip(month_days, years)]


def _extract_total_current_assets(elements, balance_sheet_dates):
    nodes = elements.xpath(".//*[@id='parentTr']/td")


def _extract_total_assets(elements):
    pass


def _extract_current_liabilities(elements):
    pass


def _extract_total_liabilities(elements):
    pass
