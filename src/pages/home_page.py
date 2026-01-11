from playwright.sync_api import Page


class HomePage:
    URL = "https://www.ebay.com"
    
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        #open homepage
        self.page.goto(self.URL)
        self.page.wait_for_load_state("domcontentloaded")

    def assert_title(self):
        # check the title
        title = self.page.title()
        print(f"Page title: {title}")
        assert "eBay" in title, f"Unexpected title: {title}"

    def open_advanced_search(self):
        #click at advanced search at the HP
        self.page.get_by_role("link", name="Advanced").click()

        
