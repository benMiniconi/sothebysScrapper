from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sothebysscrapper.sothebysscrapper import getSalesLots
import time
import re

driver = webdriver.Chrome()


for year in range(2002, 2020):
    #Force Driver to wait for 20 sec for the find elements to crash or to bind
    driver.implicitly_wait(20)
    #driver.get("https://rmsothebys.com/en/home/lots/fl20#?SortBy=Default&SearchTerm=&Category=All%20Categories&IncludeWithdrawnLots=false&Auction=FL20&OfferStatus=All%20availability&AuctionYear=&Model=Model&Make=Make&FeaturedOnly=false&StillForSaleOnly=false&Collection=All%20Lots&WithoutReserveOnly=false&Day=All%20Days&CategoryTag=All%20Motor%20Vehicles&TimedOnly=false&OneHubLinkOnly=false&page=1&pageSize=40")
    driver.get("https://rmsothebys.com/en/home/results/"+str(year))


    #Dismiss modal if Exist
    modalButtons = driver.find_elements_by_xpath("//div[@class='modal-content text-center']/button[@data-dismiss='modal']")

    #Wait for the page to be loaded
    time.sleep(5)

    for button in modalButtons:
        if button.is_displayed():
            button.click()


    #Get The Link for Sales Results
    sales = driver.find_elements_by_xpath("//li/a[@class='button button--block button--icon ']")

    #Extra Wait fot the async list to be loaded.
    time.sleep(5)

    #List the auctions with cars params for filtering
    for sale in sales:
        match = re.findall("VIEW", sale.text)
        if len(match) > 0:
            link = sale.get_attribute("href")+"?SortBy=Default&SearchTerm=&Category=All%20Categories&IncludeWithdrawnLots=false&Auction=NY17&OfferStatus=All%20availability&AuctionYear=&Model=Model&Make=Make&FeaturedOnly=false&StillForSaleOnly=false&Collection=All%20Lots&WithoutReserveOnly=false&Day=All%20Days&CategoryTag=All%20Motor%20Vehicles&TimedOnly=false&OneHubLinkOnly=false&page=1&pageSize=200"
            print("view lots", link)
            time.sleep(5)
            getSalesLots(link, year)