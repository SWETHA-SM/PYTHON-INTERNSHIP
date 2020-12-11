#SWETHA S M (Price Comparison)
import warnings
warnings.filterwarnings("ignore")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path

source1 = "https://www.flipkart.com/mi-4x-108-cm-43-ultra-hd-4k-led-smart-android-tv/p/itmab87244d2fead?pid=TVSFJRFFEWHS7RQG&lid=LSTTVSFJRFFEWHS7RQGIB1XXD&marketplace=FLIPKART&srno=b_1_1&otracker=CLP_filters&fm=SEARCH&iid=340974f4-1b40-485b-84da-a16da562964e.TVSFJRFFEWHS7RQG.SEARCH&ppt=sp&ppn=sp&ssid=0q0iy482q80000001607691398578"
source2 = "https://www.amazon.in/Mi-LED-Full-Android-Black/dp/B07T89Z35Z/ref=sr_1_1?dchild=1&keywords=Mi+4X+108+cm+%2843%29+Ultra+HD+%284K%29+LED+Smart+Android+TV&qid=1607691417&sr=8-1"


wait_imp = 10
CO = webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension', False)
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-maximized')
wd = webdriver.Chrome(r"C:\Users\Mukesh\Downloads\chromedriver_win32\chromedriver.exe",options=CO)
print ("********************************************************************\n")
print("                  Starting Program, Please wait ..... \n")

#Flipkart
print ("Connecting to Flipkart")
wd.get(source1)
wd.implicitly_wait(wait_imp)
s_price = wd.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div[1]")
S = s_price.text
pr_name = wd.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span")
product = pr_name.text
print (" ---> Successfully retrieved the price from Flipkart \n")
time.sleep(2)

#Amazon
print("Connecting to Amazon")
wd.get(source2)
wd.implicitly_wait(wait_imp)
m_price = wd.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div[6]/div[4]/div[9]/div[1]/div/table/tbody/tr[2]/td[2]/span[1]")
M = m_price.text
print (" ---> Successfully retrieved the price from Amazon \n")
time.sleep(2)


# Final display
print ("#------------------------PRODUCT NAME-----------------------------#\n")
print("Product Name: "+product)

print ("\n#-------------------------PRICE---------------------------------#\n")
print("Price available at Flipkart is: "+S)
print("Price available at Amazon is:"+M)

