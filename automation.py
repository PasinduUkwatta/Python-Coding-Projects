from selenium import webdriver
chrome_browser = webdriver.Chrome('C:/Users/Pasindu Thiwanka/Downloads/chromedriver.exe')

print(chrome_browser)

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

print('Python Easy Demo - Simple Form to Automate using Selenium' in chrome_browser.title)

button_text =chrome_browser.find_elements_by_class_name("btn-default")

print(button_text.get_attribute('innerHTML'))