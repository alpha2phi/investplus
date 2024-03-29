import re

import requests

from lxml.html import fromstring
from parsel import selector

from .utils import http_headers, is_float


def get_stock_balance_sheet(url):
    req = requests.get(url, headers=http_headers())
    if req.status_code != 200:
        raise ConnectionError("ERR: error " + str(req.status_code) +
                              ", try again later.")

    root_ = fromstring(req.text)
    path_ = root_.xpath("//*[@id='rrtable']/table")
    if path_:
        for elements_ in path_:
            balance_sheet_dates = _extract_balance_sheet_dates(elements_)
            balance_sheet = _extract_balance_sheet(elements_,
                                                   balance_sheet_dates)
            return balance_sheet

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


def _extract_balance_sheet(elements, balance_sheet_dates):
    """
    Extract balance sheet info.
    """
    nodes = elements.xpath(".//*[@id='parentTr']/td")
    balance_sheet = {}
    section = ""
    dt_index = 0
    for node in nodes:
        value = node.text_content().strip()
        if not is_float(value):
            section = value
            balance_sheet[section] = {}
            dt_index = 0
        else:
            balance_sheet[section][balance_sheet_dates[dt_index]] = float(
                value)
            dt_index = dt_index + 1
    return balance_sheet
