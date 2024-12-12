from selenium.webdriver.common.by import By  

class CartPage:  
    def __init__(self, driver):  
        self.driver = driver  

    # Locators  
    CHECKOUT_BUTTON = (By.ID, "checkout")  

    def click_checkout(self):  
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()