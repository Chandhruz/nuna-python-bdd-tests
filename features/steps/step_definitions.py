from behave import given, then

from resources.config import Config
from pages.base_page import DriverManager
from pages.landing_page import HomePage


@given('I am on the tavopets ecommerce portal')
def step_impl(context):
    context.driver = DriverManager.launch_browser_and_navigate(Config.BASE_URL)

@then('I click on the ACCEPT-COOKIES button')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.click_accept_button()

@then('I click on the SHOP-NOW button')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.click_all_products_button()

@then('I click on DUPREE product')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.click_on_dupree_product()
    
    
@then('I add DUPREE product to basket')
def step_then_i_add_dupree_product_to_basket(context):
    home_page = HomePage(context.driver)
    home_page.click_add_to_basket()

@then('I click on BASKET')
def step_then_i_click_basket(context):
    home_page = HomePage(context.driver)
    home_page.click_basket()

@then('I click PROCEED-TO-CHECKOUT button')
def step_then_i_click_proceed_to_checkout_button(context):
    home_page = HomePage(context.driver)
    home_page.click_proceed_to_checkout_button()

@then('I enter email')
def step_then_I_enter_email(context):
    home_page = HomePage(context.driver)
    home_page.enter_email()