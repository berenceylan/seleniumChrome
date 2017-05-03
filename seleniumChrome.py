##########################
##        Author        ##
##  Beren İlkim Ceylan  ##
## bceylanues@gmail.com ##
##     @berenceylan     ##
##########################

import os
from selenium import webdriver

# -- Chrome options -- #
chromedriver = "path\\to\\your\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
options = webdriver.ChromeOptions()

options.add_experimental_option("prefs", {
  "download.default_directory": "path\\to\\download",
  "download.directory_upgrade": True,  
  "download.prompt_for_download": False,
  "safebrowsing.enabled": True 
 
})
options.add_argument("--start-maximized")

driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
driver.get("http://google.com")

#Search bar
driver.find_element_by_id("q").send_keys(username)

#Click button
driver.find_element_by_name("btnK").click()
