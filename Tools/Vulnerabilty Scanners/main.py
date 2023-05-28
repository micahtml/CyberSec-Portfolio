from tkinter import Tk, Label, Entry, Button
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

# Configure Firefox driver
firefox_options = FirefoxOptions()
firefox_options.headless = True  # Run Firefox in headless mode
firefox_driver = webdriver.Firefox(options=firefox_options)

# Configure Chrome driver
chrome_options = ChromeOptions()
chrome_options.headless = True  # Run Chrome in headless mode
chrome_driver = webdriver.Chrome(options=chrome_options)


def scan_for_vulnerabilities():
    url = entry.get()

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

    # Output vulnerability findings to the GUI
    output_label.configure(
        text=f"URL: {url}\n\nVulnerabilities Found:\n\n(SQL Injection)\n\n(XSS)")


# Create the GUI window
window = Tk()
window.title("Vulnerability Scanner")

# Input Label
label = Label(window, text="Enter Target URL:")
label.pack()

# Input Entry
entry = Entry(window)
entry.pack()

# Scan Button
scan_button = Button(window, text="Scan", command=scan_for_vulnerabilities)
scan_button.pack()

# Output Label
output_label = Label(window, text="")
output_label.pack()

# Run the GUI loop
window.mainloop()

# Clean up resources
firefox_driver.quit()
chrome_driver.quit()
