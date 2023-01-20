from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome import service as fs

import csv

driver_path = "C:/Program Files/Google/Chrome/chromedriver.exe"
chrome_service = fs.Service(executable_path=driver_path)

driver = webdriver.Chrome(service=chrome_service)

#urlを指定する。
url = "https://cdnjs.com/libraries/echarts"

driver.get(url)

xpath = '//*[@id="__app"]/main/section/div/span/ul/li/span'

result = driver.find_elements(by=By.XPATH,value = xpath)

res = []
#要素を取得する。
for row in result:
    res.append(row.text)

    with open("./echarts.csv", "a", newline="", encoding="utf-8") as f:
        witer = csv.writer(f)
        witer.writerow([row.text])

#driverを終了する
driver.close()