class AdvancedSearchPage:
    def __init__(self, page):
        self.page = page

    def search_item(self, text):
        self.page.get_by_test_id("_nkw").fill(text)

    def set_max_price(self, price):
        self.page.get_by_role("textbox", name="Enter maximum price range").fill(price)
    
    def set_max_items_onPage(self, limit: str):
        self.page.get_by_test_id("s0-1-20-8[9]-1[2]-_ipg").select_option(limit)

    def submit(self):
        self.page.get_by_role("button", name="Search").nth(1).click()
        self.page.wait_for_load_state("domcontentloaded")

    def search_items_under_item_price_limit(self, query: str, max_price: str, limit: str):
        self.search_item(query)
        self.set_max_price(max_price)
        self.set_max_items_onPage(limit)
        self.submit()
