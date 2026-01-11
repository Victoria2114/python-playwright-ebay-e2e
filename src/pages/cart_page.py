
from src.utils.price_parser import clean_price

class CartPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        # Navigate to the cart page
        self.page.goto("https://cart.ebay.com/")
        self.page.wait_for_load_state("domcontentloaded")
        #
    def get_total(self):
        # Get total amount from cart page
        subtotal = self.page.locator('[data-test-id="SUBTOTAL"]')
        subtotal.wait_for(timeout=10000)

        text = subtotal.text_content()
        return clean_price(text)
    
    def assert_total_not_exceeds(self, budget_per_item: float, items_count: int):
    
        # Read the total amount from the cart
        total = self.get_total()

        # Calculate the allowed maximum based on budget per item
        threshold = budget_per_item * items_count

        # Validate that the cart total does not exceed the allowed threshold
        if total > threshold:
            raise AssertionError(
                f"Cart total {total} exceeds allowed budget {threshold}"
            )

        print(f"Cart total OK: {total} ≤ {threshold}")


    def screenshot(self, name="cart"):
        self.page.screenshot(path=f"logs/{name}.png")