from selenium.webdriver.common.by import By  

class InventoryPage:  
    def __init__(self, driver):  
        self.driver = driver  

    # Locators  
    ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")  
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")  
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")  

    def add_backpack_to_cart(self):  
        self.driver.find_element(*self.ADD_BACKPACK_BUTTON).click()  

    def go_to_cart(self):  
        self.driver.find_element(*self.SHOPPING_CART).click()  

    def get_cart_count(self):  
        return self.driver.find_element(*self.CART_BADGE).text