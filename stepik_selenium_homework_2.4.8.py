from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

book = browser.find_element_by_id('book')
browser.execute_script("return arguments[0].scrollIntoView(true);", book)

wait = WebDriverWait(browser, 17).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
book.click()


x = browser.find_element_by_id('input_value').text
answer = browser.find_element_by_id('answer')
solve = browser.find_element_by_id('solve')
browser.execute_script("return arguments[0].scrollIntoView(true);", solve)

## What is      ln(abs(12*sin(x)))      , where x = 904?
y = math.log(math.fabs(12*math.sin(float(x))))
answer.send_keys(str(y))
solve.click()
