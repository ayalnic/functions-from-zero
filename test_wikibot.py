from wikibot import scrape

def test_scrape():
    assert "American" in scrape("Microsoft")