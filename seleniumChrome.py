# -- Selenium vars -- #
chromedriver = "pat\\to\\your\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
options = webdriver.ChromeOptions()

options.add_experimental_option("prefs", {
  "download.default_directory": path,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True 
 
})
options.add_argument("--start-maximized")

driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
