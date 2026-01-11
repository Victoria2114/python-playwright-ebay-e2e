from playwright.sync_api import Page
from .product_page import ProductPage
import random

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click(self, locator):
         self.page.locator(locator).click()

    def fill(self, locator, text):
         self.page.locator(locator).fill(text)

    def screenshot(self, name):
         self.page.screenshot(path=f"reports/{name}.png")

    def click_product_card(self, index=None, label: str | None = None):
    # Locate the container that holds all search results
     results = self.page.locator("#srp-river-results")

     # Base locator for all product cards
     cards = results.get_by_role("listitem")

     # If label is provided, filter cards by that label
     if label:
        cards = cards.filter(has_text=label)

     count = cards.count()

     if count == 0:
        if label:
            raise Exception(f"No products found with label '{label}'")
        raise Exception("No product cards found on the search results page")

     # If no index is provided, choose a random product card
     if index is None:
        index = random.randint(0, count - 1)

     card = cards.nth(index)

     # Universal selector for the real product link
     link = card.locator("a[href*='/itm/']").first

     # Clicking the product link opens the item in a new tab (popup)
     with self.page.expect_popup() as page1_info:
        link.click()

     new_page = page1_info.value
     new_page.wait_for_load_state("domcontentloaded")
     return ProductPage(new_page)