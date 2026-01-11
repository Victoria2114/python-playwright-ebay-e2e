import random
import re

class ProductPage:
    def __init__(self, page):
        self.page = page

    def select_random_variant(self):
    
    # Loop until no more selectors appear
        while True:
        # Find all variant selector buttons (Color: Select, Size: Select, etc.)
            variant_buttons = self.page.get_by_role("button",name=re.compile("select", re.I))

            count = variant_buttons.count()

            # If no selectors exist, stop
            if count == 0:
                print("No variant selectors found")
                return

            print(f"Found {count} variant selectors")

            # Try to click the FIRST visible selector
            clicked = False

            for i in range(count):
                btn = variant_buttons.nth(i)

            # Skip selectors that are not visible
                if not btn.is_visible():
                    continue

                btn.wait_for(timeout=10000)
                btn.click()
                clicked = True

            # Find all options inside the dropdown
                options = self.page.locator("[role='option']")
                visible_options = []
                for j in range(options.count()):
                    opt = options.nth(j)
                    if opt.is_visible():
                        visible_options.append(opt)

                if not visible_options:
                    print("No visible options for this selector")
                    break

                # Try selecting a valid option (not out of stock)
                while visible_options:
                    chosen = random.choice(visible_options)
                    text = chosen.text_content().lower()

                    if "out of stock" in text:
                        print("Option out of stock, choosing another")
                        visible_options.remove(chosen)
                        continue
                
                    print("Selected option:", chosen.text_content())
                    chosen.click()
                    break  # break inner loop, then rescan selectors
                else:
                    print("All visible selectors were skipped")
                    break
                break

            if not clicked:
                print("No visible variant selectors to click")
                break
    
    def screenshot(self, name: str):
        self.page.screenshot(path=f"logs/{name}.png")

    def add_to_cart(self):
        self.page.get_by_test_id("x-atc-action").get_by_test_id("ux-call-to-action").click()
        self.page.get_by_role("link", name="See in cart").click()
        self.page.wait_for_load_state("domcontentloaded")
        