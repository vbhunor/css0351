import pytest
from bs4 import BeautifulSoup

@pytest.fixture
def html_content():
    """Beolvassa az index.html fájlt tesztelésre."""
    with open("index.html", encoding="utf-8") as f:
        return f.read()

@pytest.fixture
def css_content():
    """Beolvassa a style.css fájlt tesztelésre."""
    with open("style.css", encoding="utf-8") as f:
        return f.read()

def test_has_stylesheet(html_content):
    """Ellenőrzi, hogy a HTML fájl beimportálja-e a style.css-t."""
    soup = BeautifulSoup(html_content, "html.parser")
    link_tag = soup.find("link", {"rel": "stylesheet", "href": "style.css"})
    assert link_tag is not None, "A style.css nincs beimportálva a HTML fájlba!"

def test_has_container(html_content):
    """Ellenőrzi, hogy van-e egy fő konténer div."""
    soup = BeautifulSoup(html_content, "html.parser")
    container = soup.find("div", class_="container")
    assert container is not None, "A fő konténer (div.container) hiányzik!"

def test_has_four_small_squares(html_content):
    """Ellenőrzi, hogy pontosan négy kis négyzet van-e benne."""
    soup = BeautifulSoup(html_content, "html.parser")
    squares = soup.find_all("div", class_="small-square")
    assert len(squares) == 4, "Nincs pontosan négy kis négyzet (div.small-square)!"

def test_css_has_container(css_content):
    """Ellenőrzi, hogy a CSS tartalmazza-e a .container szabályt."""
    assert ".container" in css_content, "A CSS fájl nem tartalmazza a .container szabályt!"

def test_css_has_small_square(css_content):
    """Ellenőrzi, hogy a CSS tartalmazza-e a .small-square szabályt."""
    assert ".small-square" in css_content, "A CSS fájl nem tartalmazza a .small-square szabályt!"

def test_css_has_positions(css_content):
    """Ellenőrzi, hogy a kis négyzetek megfelelő pozícióban vannak-e definiálva."""
    expected_positions = ["square1", "square2", "square3", "square4"]
    for pos in expected_positions:
        assert f".{pos}" in css_content, f"A(z) {pos} osztály nincs definiálva a CSS fájlban!"
