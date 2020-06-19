
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from contextlib import contextmanager
import time


driver = webdriver.Chrome()
driver.get("https://www.morele.net")
driver.maximize_window()

def wait_for(condition_function):
    start_time = time.time()
    while time.time() < start_time + 3:
        if condition_function():
            return True
        else:
            time.sleep(4)


@contextmanager
def wait_for_page_load(driver):
    old_page = driver.find_element_by_tag_name('html')

    yield

    def page_has_loaded():
        new_page = driver.find_element_by_tag_name('html')
        return new_page.id != old_page.id

    wait_for(page_has_loaded)


def displayCategoriesBar():
    navigation = driver.find_element_by_id("horizontal_navigation")
    linksLength = len(navigation.find_elements_by_tag_name("li"))
    for x in range (linksLength):
        nav = driver.find_element_by_id("horizontal_navigation")
        links = nav.find_elements_by_tag_name("li")
        with wait_for_page_load(driver):    
            links[x].click()
        driver.back()
        time.sleep(1)
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

def addElementToCartFromHomePage():
    categoryList = driver.find_element_by_class_name('cn-shop')
    laptops = categoryList.find_element_by_tag_name("li")
    with wait_for_page_load(driver):    
        laptops.click()
    listOfProducts = driver.find_element_by_class_name('cat-list-products')
    productsToAdd = listOfProducts.find_elements_by_class_name('cat-product-buttons')
    with wait_for_page_load(driver):    
        productsToAdd[0].click()
    confirmEl =  driver.find_element_by_class_name('md-footer')
    confirmButton = confirmEl.find_element_by_tag_name('button')
    with wait_for_page_load(driver):    
        confirmButton.click()


def addElementToCart():
    categories = driver.find_element_by_id('common_navigation')
    action = ActionChains(driver)
    action.move_to_element(categories).perform()
    time.sleep(3)
    categoriesDisplayed = driver.find_element_by_id('common_navigation')
    laptopFromList = categoriesDisplayed.find_element_by_class_name('cn-bar')
    lap = laptopFromList.find_element_by_tag_name('ul')
    s = lap.find_element_by_tag_name('li')
    with wait_for_page_load(driver):    
        s.click()

def addManyElementsToCart(numberOfProductsToAdd):
    for x in range (1,numberOfProductsToAdd):
        listOfProducts1 = driver.find_element_by_class_name('cat-list-products')
        productsToAdd1 = listOfProducts1.find_elements_by_class_name('cat-product-buttons')
        actions = ActionChains(driver)
        actions.move_to_element(productsToAdd1[x+1]).perform()
        time.sleep(3)
        with wait_for_page_load(driver):    
            productsToAdd1[x].click()
        confirmEl1 =  driver.find_element_by_class_name('md-footer')
        confirmButton1 = confirmEl1.find_element_by_tag_name('button')
        with wait_for_page_load(driver):    
            confirmButton1.click()
        categories = driver.find_element_by_id('common_navigation')
        action = ActionChains(driver)
        action.move_to_element(categories).perform()
        time.sleep(3)
        categoriesDisplayed = driver.find_element_by_id('common_navigation')
        laptopFromList = categoriesDisplayed.find_element_by_class_name('cn-bar')
        lapUl = laptopFromList.find_element_by_tag_name('ul')
        lap = lapUl.find_element_by_tag_name('li')
        with wait_for_page_load(driver):    
            lap.click()
   

displayCategoriesBar()
addElementToCartFromHomePage()
addElementToCart()
addManyElementsToCart(4)
driver.close()
   

