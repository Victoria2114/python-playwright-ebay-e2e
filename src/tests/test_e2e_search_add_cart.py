import allure
from src.pages.home_page import HomePage
from src.pages.advancedSearch_page import AdvancedSearchPage
from src.pages.base_page import BasePage
from src.pages.product_page import ProductPage
from src.pages.cart_page import CartPage

@allure.title("End-to-End Tests: Search, Add to Cart and Verify Cart Total")
def test_e2e(page):

    search_page = page  # save the main tab
    with allure.step("Open the eBay homepage"):
        home = HomePage(page)
        home.open()
        home.assert_title()

    with allure.step("Looking for items by name under a certain price and limit"):
        home.open_advanced_search()
        adv = AdvancedSearchPage(page)
        adv.search_items_under_item_price_limit("dress", "100", "60")
        page.wait_for_selector("#srp-river-results")

    with allure.step("Add first 3 items from search results to cart with variant selection"):
        base = BasePage(search_page)

        ITEMS_TO_ADD = 3
        for i in range(ITEMS_TO_ADD):
            product_page = base.click_product_card(label="Buy It Now")
            product_page.select_random_variant()
            product_page.add_to_cart()

        # screenshot in Allure report after adding each item
        allure.attach(
            product_page.page.screenshot(),
            name=f"added_item_{i+1}",
            attachment_type=allure.attachment_type.PNG
        )

        # Close product tab and return to search page
        product_page.page.close()
        search_page.bring_to_front()

    with allure.step("Verify cart total does not exceed the limit"):
        cart_page = CartPage(page)
        cart_page.open()
        cart_page.assert_total_not_exceeds(110, ITEMS_TO_ADD)
    

