from selenium import webdriver
import time
import keyboard
from pynput.keyboard import Key, Controller
from bs4 import BeautifulSoup



from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://twitter.com/")



kullanici_adi = str('username')
time.sleep(1)



giris_yap = browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/div[3]/div[4]/span/span")
giris_yap.click()

time.sleep(3)

giris_yap = browser.find_element(By.XPATH,"/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/a/div/span/span")
giris_yap.click()
time.sleep(5)
browser.find_element(By.NAME,'username').send_keys(kullanici_adi)
butonnext=browser.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div")
butonnext.click()
time.sleep(2)
browser.find_element(By.NAME,"password").send_keys("inputYourPassword")
time.sleep(2)
buttongiris=browser.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div")
buttongiris.click()
time.sleep(3)
searchbox=browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/section/div/div/div/div/div[2]/div/div/div[3]")
searchbox.click()
time.sleep(1)
latest=browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div/div[2]/div/div[2]/a/div")
latest.click()
time.sleep(5)
Dosya=open("AllTweets.txt","a",encoding="utf8")

lenOfPage=browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    lenOfPage = browser.execute_script("window.scrollTo(0,document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    time.sleep(5)
    if lastCount == lenOfPage:
        match=True
    sayfa = browser.page_source
    soup = BeautifulSoup(sayfa, "html.parser")
    tweets = soup.find_all("div", attrs={
        "class": "css-901oao r-1fmj7o5 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"})
    for element in tweets:
        print("************************************************************")


        if element.find("span", attrs={"class": "css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"}) is not None:
            tweeticerik=element.find("span", attrs={"class": "css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"}).text
            print(tweeticerik)
            print(type(tweeticerik))
            Dosya.write(tweeticerik + "\n")
            Dosya.write("************************************************************\n")
        else:
            tweeticerik = None


Dosya.close()
time.sleep(5)
