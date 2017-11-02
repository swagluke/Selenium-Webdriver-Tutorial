from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


options = webdriver.ChromeOptions()

# Selenium Headless Web Browser Set up
# For options.binary_location Mac uses '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'.
# For options.binary_location Ubuntu 16.04.  There are a few possible options 
#'/opt/google/chrome/google-chrome', '/usr/bin/google-chrome', '/usr/local/bin/chromedriver'.

options.binary_location = '/usr/bin/google-chrome'

# Indicating whether the webdriver should be headless or not.
options.add_argument('headless')

# If you are running Ubuntu without GUI (AWS EC2 Instance), --no-sandbox is nedded. Not needed if you are running OSX or window.
options.add_argument('--no-sandbox')

# Lanuch webdriver.Chrome using the chrome_options.
driver = webdriver.Chrome(chrome_options=options)

# Kinda using ChromeDriver as a server, therefore save the executor url so webdriver. Remote can re attach back to it.
executor_url = driver.command_executor._url

# Saving the session id (Webdriver Tab ID) for the existing driver. 
session_id = driver.session_id

# print(session_id)
# print(executor_url)

# Point webdriver to the url you want to test/visit.
url = "https://www.google.com"
driver.get(url)

# Screen shot the page or print out the current url address to verify whther driver is working or not.
# driver.get_screenshot_as_file('main-page.png')
# print(driver.current_url)

# Turns out webdriver.Remote will need similar ChromeOptions setting too. 
driver2 = webdriver.Remote(command_executor=executor_url, desired_capabilities=options.to_capabilities())

# A lot of people get scraed about the close statement. I discover that webdriver.Remote opens up a new webdriver everytime
# and we lost control of it after we  re-attach the new Remote driver to the old driver. (Left a new zombie process)
# However, there is this little hack here that allows you to close the driver2 before you re-attach to the old driver.
# If you don't feel comfortable about this. Go ahead comment out the driver2.close()
driver2.close()
driver2.session_id = session_id
# You will see 
print(driver2.current_url)
driver2.get("https://www.facebook.com")
print(driver2.current_url)

# Calling quit to kill the webdriver process. If you want to continue using the webdriver for another python code.
# Comment out the driver2.quit() Line 57, then sust save the executor_url and session_id
# Repeat the process from line 41 to line 48. (Create Webdriver.Remote again.)
driver2.quit()

