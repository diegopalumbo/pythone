# vim test.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

result = driver.get("https://live-tennis.eu/it/classifica-atp-live")
try:
    # Wait for the table to be present
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, 'u868'))
    )
    # Print the table element
    for row in element.find_elements(By.TAG_NAME, 'tr'):
        print(row.text)
except Exception as e:
    print("Error:", e)
finally:
    driver.close()