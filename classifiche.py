# vim test.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tabulate import tabulate

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
    
    table_data = []
    
    # recupero elemento con id u868
    el_table = driver.find_element(By.ID, 'u868')
    
    # da el_table recupero tbhead 
    el_theads = el_table.find_elements(By.CLASS_NAME, 'tbhead')
    
    # prendo ultimo elemento di tbhead come header e lo aggiungo alla lista table_data
    el_thead = el_theads[-1]
    
    # scorro le righe di thead e le aggiungo alla lista table_data
    cells = el_thead.find_elements(By.TAG_NAME, 'td')
    table_data.append([cell.text for cell in cells])

    # da el_table recupero tbbody
    el_tbody = el_table.find_elements(By.TAG_NAME, 'tbody')        
    for tbody in el_tbody:  # Iterate over each tbody element
        for row in tbody.find_elements(By.TAG_NAME, 'tr')[:100]:  # Find rows within each tbody
            cells = row.find_elements(By.TAG_NAME, 'td') 
            if cells[0].text.startswith("<") or cells[0].text.startswith(">") or cells[0].text.startswith("Tutti") or cells[0].text == "" :
                continue            
            table_data.append([cell.text for cell in cells])

    # Cerca intestazione tramite classe tbhead 
    # table_data = []
    # for row in element.find_elements(By.CLASS_NAME, 'tbhead')[:100]:
    #     cells = row.find_elements(By.TAG_NAME, 'td') 
    #     table_data.append([cell.text for cell in cells])
    
    
    # Print the table element
    # table_data = []
    # for row in element.find_elements(By.TAG_NAME, 'tr')[:100]:
    #     cells = row.find_elements(By.TAG_NAME, 'td') 
    #     table_data.append([cell.text for cell in cells])
    
    print(tabulate(table_data, headers="firstrow", tablefmt="grid"))
        
except Exception as e:
    print(f"An error of type {type(e).__name__} occurred. Details: {e}")
finally:
    driver.close()