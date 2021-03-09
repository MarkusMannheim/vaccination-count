import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# load in existing data
data = pd.read_csv("./vaccinations_data.csv")
data.date = pd.to_datetime(data.date)
last_date = data.iat[len(data) - 1, 0]

# use a headless browser (saves time)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--start-maximized")

# set up the browser
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.covid19.act.gov.au/")

# scrape date
date_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "spf-article-card--tabular-subtitle"))
)
date_text = date_field.find_element_by_tag_name("p").get_attribute("innerText")
date = date_text[date_text.index(",") + 2:]
date = pd.to_datetime(date, format="%d/%m/%Y") # transform to date object

# scrape vaccinations
vaccination_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-lg-6:last-child td:last-child"))
)
vaccinations = int(vaccination_field.get_attribute("innerText").replace(",", ""))

# check if data needs update
if date > last_date:
    print("This is new data — saving to file.")
    print(f"{vaccinations:,.0f} vaccinations as of {date:%B %d, %Y}.")
    
    # save to file    
    data.loc[len(data)] = [date, vaccinations]
    data.to_csv("data.csv", index=False)
    print("New data saved to file.")
    
elif date == last_date:
    print("This data has already been scraped.")

else:
    print("An error seems to have occured — this data is from the past.")

driver.quit()
quit()
last_date = data.iat[len(data) - 1, 0]

# use a headless browser (saves time)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--start-maximized")

# set up the browser
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.covid19.act.gov.au/")

# scrape date
date_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "spf-article-card--tabular-subtitle"))
)
date_text = date_field.find_element_by_tag_name("p").get_attribute("innerText")
date = date_text[date_text.index(",") + 2:]
date = pd.to_datetime(date, format="%d/%m/%Y") # transform to date object

# scrape vaccinations
vaccination_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-lg-6:last-child td:last-child"))
)
vaccinations = int(vaccination_field.get_attribute("innerText").replace(",", ""))

# check if data needs update
if date > last_date:
    print("This is new data — saving to file.")
    print(f"{vaccinations:,.0f} vaccinations as of {date:%B %d, %Y}.")
    
    # save to file    
    data.iloc[len(data)] = [date, vaccinations]
    data.to_csv("data.csv", index=False)
    print("New data saved to file.")
    
elif date == last_date:
    print("This data has already been scraped.")

else:
    print("An error seems to have occured — this data is from the past.")

driver.quit()
quit()
