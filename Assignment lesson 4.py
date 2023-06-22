from selenium import webdriver
from selenium.webdriver.edge.service import Service
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument('--some-option')
# my_driver = Service('c:/users/zvikap/downloads/chromedriver/chromedriver.exe')
# my_driver = webdriver.Chrome(service=chrome_service, options=chrome_optio


# Write a script which will open the following:
# a. Chrome – http://www.walla.co.il
# b. Firefox – http://www.ynet.co.il

# my_driver = webdriver.Chrome(service=Service('c:/users/zvikap/downloads/chromedriver/chromedriver.exe'))
# my_driver.get('http://www.walla.co.il')
# from selenium.webdriver.common.by import By
# input()

# my_driver = webdriver.Edge(service=Service('c:/users/zvikap/downloads/edgedriver_win32/msedgedriver.exe'))
# my_driver.get('http://www.ynet.co.il')
# from selenium.webdriver.common.by import By
# input()

# In one of the browsers you have open, do the following:
   # a. Create a variable with the website’s title
   # b. Refresh website
   # c. Get website name and compare it to the variable you created in clause 1

# my_driver.get('http://www.ynet.co.il')
# print(my_driver.title)
# my_driver.refresh()
# print(my_driver.current_url)

# Open a few browsers, locate any element, does the element has the same locator in the other browser?
# Edge =   //*[@id="SknDZdImryw3"]/h1/span
# chrome = //*[@id="Hk6VEwBNrkvh"]/h1/span

# Create a test with the following:
   # a. Open Google Translate web page
   # b. Write anything in Hebrew in the text area

# my_driver.get('https://translate.google.co.il/?hl=iw&sl=auto&tl=iw&op=translate')
# my_driver.implicitly_wait(10)
# my_driver.find_element(webdriver.common.by.By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').send_keys("שלום")
# input()

# Open Youtube web page
  # a. Type a name of a song
  # b. Click on search

# my_driver.get('https://www.youtube.com/')
# my_driver.implicitly_wait(5)
# my_driver.find_element(webdriver.common.by.By.XPATH, '//input[@id="search"]').send_keys("send me an angle")
# my_driver.find_element(webdriver.common.by.By.XPATH, '//*[@id="search-icon-legacy"]').click()
# input()


# Open Chrome browser on Google Translate website: https://translate.google.com/
   # a. Find translation text field (the one you send keys to) with 3 different locators and
   # print the WebElement you created.

# my_driver.get('https://translate.google.co.il/?hl=iw&sl=auto&tl=iw&op=translate')
# my_driver.implicitly_wait(10)
# # my_driver.find_element(webdriver.common.by.By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').send_keys("שלום")
# # my_driver.find_element(webdriver.common.by.By.XPATH, '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').send_keys("שלום")
# my_driver.find_element(By.CLASS_NAME, 'er8xn').send_keys("hello")


# Open Chrome browser on Facebook website https://www.facebook.com/
   # a. Login into Facebook (No need to send me credentials).

# my_driver.get('https://www.facebook.com/')
# my_driver.implicitly_wait(10)
# my_driver.find_element(webdriver.common.by.By.XPATH, '//*[@id="email"]').send_keys("zvikapepel@gmail.com")
# my_driver.find_element(webdriver.common.by.By.XPATH, '//*[@id="pass"]').send_keys("xxxxxxx")
# my_driver.find_element(webdriver.common.by.By.XPATH, '//*[@id="u_0_9_o2"]').click()




# input()Open Chrome browser on any webpage:
   # a. Delete all cookies from browser.
   # b. Make sure all cookies are deleted by printing all cookies stored in the browser.

# my_driver.delete_all_cookies()

# First test if I can print all Cookies
# my_driver.get('https://github.com/')
# cookies = my_driver.get_cookies()
# for cookie in cookies:
#     print(f"Name: {cookie['name']}")
#     print(f"Value: {cookie['value']}")
#     print(f"Domain: {cookie['domain']}")
#     print(f"Path: {cookie['path']}")
#     print(f"Secure: {cookie['secure']}")
#     print("-----")

# # then try to print after delete all Cookies
# print('Try to delete cookies Try to delete cookies Try to delete cookies Try to delete cookies Try to delete cookies')
# my_driver.delete_all_cookies()
# cookies = my_driver.get_cookies()
# for cookie in cookies:
#     print(f"Name: {cookie['name']}")


# Open any browser on "Github" website https://github.com/
   # a. Enter “Selenium” keyword in search textfield
   # b. Press Enter to search (through code - of course).

# my_driver.get('https://github.com/')
# my_driver.find_element(By.XPATH, "//input[@name='q']").send_keys("selenium")
# my_driver.find_element(By.XPATH, "//input[@name='q']").send_keys(Keys.ENTER)


# Find a way to disable all extensions in
   # a. Chrome
   # b. Firefox
   # c. Explorer.


# my_driver = webdriver.Chrome(service=Service('c:/users/zvikap/downloads/chromedriver/chromedriver.exe'))
# driver_path = 'c:/users/zvikap/downloads/chromedriver/chromedriver.exe'
# chrome_options = Options()
# chrome_options.add_argument('--user-data-dir=c:/users/zvikap/downloads/chromedriver')
# chrome_options.add_argument('--disable-extensions')
# my_driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)



# driver_path = 'c:/users/zvikap/downloads/edgedriver_win32/msedgedriver.exe'
# edge_options = EdgeOptions()
# edge_options.use_chromium = True
# edge_options.add_argument('--disable-extensions')
# driver = Edge(executable_path=driver_path, options=edge_options)

# Find a way to start a browser without extensions.

# chrome_options.add_argument('--disable-extensions')
# driver = webdriver.Chrome(options=chrome_options)

# input()
