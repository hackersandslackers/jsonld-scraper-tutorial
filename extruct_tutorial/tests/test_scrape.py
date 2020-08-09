"""Validate JSON-LD Scrape outcome."""
import pytest
from extruct_tutorial import scrape


@pytest.fixture
def url():
    """Target URL to scrape metadata."""
    return 'https://hackersandslackers.com/creating-django-views/'


@pytest.fixture
def expected_json():
    """Expected metadata to be returned."""
    return {'@context': 'https://schema.org/', '@type': 'Article',
            'author': {'@type': 'Person', 'name': 'Todd Birchard',
                       'image': 'https://hackersandslackers-cdn.storage.googleapis.com/2020/04/todd@2x.jpg',
                       'sameAs': ['https://toddbirchard.com', 'https://twitter.com/ToddRBirchard']},
            'keywords': 'Django, Python, Software Development', 'headline': 'Creating Interactive Views in Django',
            'url': 'https://hackersandslackers.com/creating-django-views/',
            'datePublished': '2020-04-23T12:21:00.000-04:00', 'dateModified': '2020-05-02T13:31:33.000-04:00',
            'image': {'@type': 'ImageObject',
                      'url': 'https://hackersandslackers-cdn.storage.googleapis.com/2020/04/django-views-1.jpg',
                      'width': '1000', 'height': '523'},
            'publisher': {'@type': 'Organization', 'name': 'Hackers and Slackers', 'founder': 'Todd Birchard',
                          'logo': {'@type': 'ImageObject',
                                   'url': 'https://hackersandslackers-cdn.storage.googleapis.com/2020/03/logo-blue-full.png',
                                   'width': 60, 'height': 60}},
            'description': 'Create interactive user experiences by writing Django views to handle dynamic content, submitting forms, and interacting with data.',
            'mainEntityOfPage': {'@type': 'WebPage', '@id': 'https://hackersandslackers.com'}}


def test_scrape(url, expected_json):
    """Match scrape's fetched metadata to known value."""
    metadata = scrape(url)
    assert metadata == expected_json
