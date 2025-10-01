import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
options.add_argument('disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

url = "https://realtorsbd.com/project"
driver = webdriver.Chrome(options=options)
driver.get(url)
driver.maximize_window()


try :
    time.sleep(2)
    estate_list = []
    estates = driver.find_elements(By.CSS_SELECTOR, "div.property-item")
    if estates :
        for estate in estates :
            clickable = estate.find_element(By.CSS_SELECTOR, "h5.property-title>a").get_attribute("href")
            if clickable :
                estate_list.append(clickable)
                time.sleep(3)
            else :
                print("Heading not found")
        i = 0
        estate_data = []
        while i < len(estate_list):
            driver.get(estate_list[i])
            try : 
                title = driver.find_element(By.CSS_SELECTOR, "div.property-detail-title>h3").text
                investment = driver.find_element(By.CSS_SELECTOR, "div.property-detail-title>h4").text
                location = driver.find_element(By.XPATH, "//h5[contains(text(), 'Property Location')]/following::h6").text
                property_type = driver.find_element(By.XPATH, "//h5[contains(text(), 'Property Type')]/following::h6").text
                features = driver.find_elements(By.CSS_SELECTOR, "div.row>div.col-sm-12>ul>li")
                for feature in features :
                    feature_list = [f.text.strip() for f in features if f.text.strip()]
                
            except :
                print("Error occured")
            estate_data.append({
                'id': i,
                'title': title,
                'investment': investment,
                'property location': location,
                'property type': property_type,
                'features': feature_list
            },
            )
            i += 1
        with open("real_estate.json","w", encoding="utf-8") as f :
            json.dump(estate_data, f, ensure_ascii=False, indent=2)
        
    else :
        print("estate not available")
except :
    print("Error found")