from pages.login_page import LoginPage  
from pages.inventory_page import InventoryPage  
from pages.cart_page import CartPage  
from pages.checkout_page import CheckoutPage  

def test_valid_purchase_flow(driver):  
    # Login Page  
    login_page = LoginPage(driver)  
    login_page.navigate()  
    login_page.login("standard_user", "secret_sauce")  
    
    # Inventory Page  
    inventory_page = InventoryPage(driver)  
    inventory_page.add_backpack_to_cart()  
    
    # Verify cart count  
    assert inventory_page.get_cart_count() == "1"  
    
    # Go to Cart  
    inventory_page.go_to_cart()  
    
    # Cart Page  
    cart_page = CartPage(driver)  
    cart_page.click_checkout()  
    
    # Checkout Page  
    checkout_page = CheckoutPage(driver)  
    checkout_page.fill_information("John", "Doe", "12345")  
    checkout_page.complete_purchase()  
    
    # Add final assertion to verify successful purchase  
    assert "checkout-complete" in driver.current_url  

def test_invalid_login(driver):  
    # Login Page  
    login_page = LoginPage(driver)  
    login_page.navigate()  
    login_page.login("invalid_user", "invalid_password")  
    
    # Verify error message  
    error_message = login_page.get_error_message()  
    assert "Username and password do not match" in error_message