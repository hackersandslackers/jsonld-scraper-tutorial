"""Fetch structured JSON-LD data from a given URL."""
from pprint import pprint
import requests
import extruct
from w3lib.html import get_base_url


def scrape(url: str):
    """Parse structured data from a target page."""
    html = get_html(url)
    metadata = get_metadata(html, url)
    pprint(metadata, indent=2, width=150)
    return metadata


def get_html(url):
    """Get raw HTML from a URL."""
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    req = requests.get(url, headers=headers)
    return req.content


def get_metadata(html: bytes, url: str):
    """Fetch JSON-LD structured data."""
    metadata = extruct.extract(
        html,
        base_url=get_base_url(url),
        syntaxes=['json-ld'],
        uniform=True
    )['json-ld']
    if bool(metadata) and isinstance(metadata, list):
        metadata = metadata[0]
    return metadata
