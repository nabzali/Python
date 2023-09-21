import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless=new")

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)

url = 'http://18.168.179.166/Prayers_alkalaam_ig2/'

driver.get(url)

today = datetime.date.today()

# Format the date
formatted_date = today.strftime("%A %dth %B %Y")

print(f"Today is {formatted_date}")

isJummah = today.strftime("%A") == "Friday"

timings = {}
prayers = ["Fajr", "Jummah" if isJummah else "Zohr", "Asr", "Magrib", "Isha"]
    
for prayer in prayers:
    # Find the element by its ID
    time = driver.find_element(By.ID, f"{prayer.lower()}-begins")
    jamaat = driver.find_element(By.ID, f"{prayer.lower()}-jamaat")
    print(f"{prayer} begins at: {time.text} ({jamaat.text})")
    timings[prayer] = [time, jamaat]

if isJummah:
    prayers.append("Jummah")



      
driver.quit()
print("It is Jummah today." if isJummah else "It is not Jummah today.")