from selenium import webdriver
import time
from sothebysscrapper.sothebysdetailextraction import extractLot, exportResult
from selenium.webdriver.support.ui import Select

import re

detail = webdriver.Chrome()


def getSalesLots(link, year):
    #implicitly wait unitl 20 sec for elements selection especially for modal
    detail.implicitly_wait(20)
    #trigger sale navigation through selenium
    detail.get(link)
    time.sleep(5)

    # Dismiss modal if Exist
    modalButtons = detail.find_elements_by_xpath(
        "//div[@class='modal-content text-center']/button[@data-dismiss='modal']")

    # Wait for the page to be loaded
    time.sleep(10)

    for button in modalButtons:
        if button.is_displayed():
            button.click()

    select = Select(detail.find_element_by_id('pageSize'))
    #print all sales to page by selecting the filter
    select.select_by_value("object:6")
    # wait for the DOM to refresh
    time.sleep(20)


    #Pass Updated DOM to beautiful soup to excrat core data out of the browser
    lots = extractLot(detail.page_source, year)
    if len(lots) > 0:
        vente = lots[0]["Vente"].replace(" ", "")
        exportResult(lots, vente, year)
    #sales = detail.find_elements_by_xpath("//div[@class='RMAuctions']/a")
    #for sale in sales:
    #    print(sale.get_attribute("href"))

    #sales = detail.find_elements_by_xpath("//div[@class='RMSothebys']/a")
    #for sale in sales:
    #   print(sale.get_attribute("href"))
