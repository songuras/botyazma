from modules.excel import Excel
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

xl = Excel("linkedin_posts.xlsx")
xl.write_header([
        "owner name"
        "owner url"
        "date"
        "text"
        "shared text"
    ])

excel_file = "linkedin_posts.xlsx"


#tarayıcıyı çalıştır ve linkedine giriş yap


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://linkedin.com')
sleep(5)












xl.save()