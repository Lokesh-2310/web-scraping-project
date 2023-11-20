from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
s=Service('C:/Users/dell/Desktop/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://www.flipkart.com/mobile-phones-store?fm=neo%2Fmerchandising&iid=M_60384cff-6525-4c4c-af9f-c4d8cdfd9512_1_372UD5BXDFYS_MC.ZRQ4DKH28K8J&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Mobiles_ZRQ4DKH28K8J&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L0_view-all&cid=ZRQ4DKH28K8J')
time.sleep(2)
driver.find_element(By.XPATH,value='//*[@id="container"]/div/div[3]/div[4]/div[1]/div/section[3]/div[2]/div[2]').click()
time.sleep(3)

for i in range(2,20):
    l=[9,13,14,15,16,17,18]
    if i in l:
        continue
    driver.find_element(By.XPATH,value=f'//*[@id="container"]/div/div[3]/div[4]/div[1]/div/section[3]/div[2]/div/div[1]/div[2]/div[{i}]').click()
driver.find_element(By.XPATH,value='//*[@id="container"]/div/div[3]/div[4]/div[1]/div/section[3]/div[2]/div/div[1]/div[3]/div/div[2]').click()

time.sleep(5)
counter=1

while counter<=25:
    html=driver.page_source
    if counter==1:
        with open('flip.html', 'a', encoding='utf-8') as f:
            f.write(html + "\n\n\n")
            time.sleep(3)
        driver.find_element(By.XPATH,value='//*[@id="container"]/div/div[3]/div/div[2]/div[26]/div/div/nav/a[11]').click()
        time.sleep(2)
    else:
        with open('flip.html','a',encoding='utf-8') as f:
            f.write(html+"\n\n\n")
            time.sleep(3)
        driver.find_element(By.XPATH,value='//*[@id="container"]/div/div[3]/div/div[2]/div[26]/div/div/nav/a[12]').click()
        time.sleep(2)
    counter=counter+1
input()