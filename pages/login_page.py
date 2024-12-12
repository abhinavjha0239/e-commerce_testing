from selenium.webdriver.common.by import By  

class LoginPage:  
    def __init__(self, driver):  
        self.driver = driver  
        self.url = "https://www.saucedemo.com/"  
        
    # Locators  
    USERNAME_INPUT = (By.ID, "user-name")  
    PASSWORD_INPUT = (By.ID, "password")  
    LOGIN_BUTTON = (By.ID, "login-button")  
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")  

    def navigate(self):  
        self.driver.get(self.url)  

    def login(self, username, password):  
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)  
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)  
        self.driver.find_element(*self.LOGIN_BUTTON).click()  

    def get_error_message(self):  
        return self.driver.find_element(*self.ERROR_MESSAGE).text