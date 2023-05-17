from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

# Target URLs to scan
target_urls = ["http://example.com/login", "http://example.com/contact"]

# Configure Firefox driver
firefox_options = FirefoxOptions()
firefox_options.headless = True  # Run Firefox in headless mode
firefox_driver = webdriver.Firefox(options=firefox_options)

# Configure Chrome driver
chrome_options = ChromeOptions()
chrome_options.headless = True  # Run Chrome in headless mode
chrome_driver = webdriver.Chrome(options=chrome_options)


def scan_for_vulnerabilities(url):
    # Scan for SQL injection vulnerabilities
    sql_payload = "' OR '1'='1"
    # Send request to target URL using Firefox
    firefox_driver.get(url)
    # Inject payload into input fields
    input_elements = firefox_driver.find_elements_by_tag_name("input")
    for input_element in input_elements:
        input_element.send_keys(sql_payload)
    # Submit the form
    form_element = firefox_driver.find_element_by_tag_name("form")
    form_element.submit()
    # Analyze response for SQL injection vulnerability

    # Scan for XSS vulnerabilities
    xss_payload = "<script>alert('XSS')</script>"
    # Send request to target URL using Chrome
    chrome_driver.get(url)
    # Inject payload into input fields
    input_elements = chrome_driver.find_elements_by_tag_name("input")
    for input_element in input_elements:
        input_element.send_keys(xss_payload)
    # Submit the form
    form_element = chrome_driver.find_element_by_tag_name("form")
    form_element.submit()
    # Analyze response for XSS vulnerability

    # Output vulnerability findings to the terminal
    print(f"URL: {url}")
    print("Vulnerabilities Found:")
    # Output SQL injection vulnerabilities

    # Output XSS vulnerabilities
    print()


# Scan each target URL
for url in target_urls:
    scan_for_vulnerabilities(url)

# Clean up resources
firefox_driver.quit()
chrome_driver.quit()
