import requests
import time
from bs4 import BeautifulSoup
import re
from modulesauto.auto24export import fields

def getPagesList(soup):
    # pagesList = soup.find_all("ul", {"class": "sc-pagination"})
    # for page in pagesList:
    nextpage = soup.find_all("li", {"class": "next-page"})
    if len(nextpage):
        print("nextPage", nextpage[0].attrs["href"])


def searchNextPage(url, annonces, page, maxPage, startingYear, endYear):
    cleanUrl = url + "&page=" + page if page else url
    cleanUrl = cleanUrl + "&fregfrom=" + startingYear if startingYear else cleanUrl
    cleanUrl = cleanUrl + "&fregto=" + endYear if endYear else cleanUrl
    print(cleanUrl)
    response = requests.get(cleanUrl)
    time.sleep(5)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    # pages = getPagesList(soup)

    getAnnonces(soup, annonces)
    if int(page) < 20:
        searchNextPage(url, annonces, str(int(page) + 1), maxPage, startingYear, endYear)


def getAnnonces(soup, liste):
    annonces = soup.find_all("div", {"class": "cl-list-element-gap"})
    for annonce in annonces:
        car = {}
        vehicleDetails = annonce.find_all("ul", {"data-item-name": "vehicle-details"})
        vehicleExtraDetails = annonce.find_all("a", {"data-item-name": "detail-page-link"})
        for extraLink in vehicleExtraDetails:
            link = "https://www.autoscout24.fr" + extraLink.attrs["href"]
            car = getDetailedCarAnnonce(link, car)
            print(car)
            liste.append(car)
    return liste

def getDetailedCarAnnonce(link, car):
    response = requests.get(link)
    # time.sleep(5)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    caracterisitiquesPrice = soup.find_all("div", {"class": "cldt-price"})
    for caracterisitique in caracterisitiquesPrice:
        vehicleDetails = caracterisitique.find_all("h2")
        car["Price"] = vehicleDetails[0].text.replace("€ ", "").replace(".", "").replace(",-", "").replace("\n", "")

    caracterisitiquesKM = soup.find_all("span", {"class": "cldt-stage-primary-keyfact"})
    for caracterisitique in caracterisitiquesKM:
        label = caracterisitique.text.lower().replace("€ ", "").replace(".", "").replace(",-", "").replace("\n", "")
        if len(re.findall("[0-9]{4,6} km", label)) > 0:
            car["KM"] = re.findall("[0-9]{4,6}", label)[0]
    caracterisitiquesImmat = soup.find_all("span", {"id": "basicDataFirstRegistrationValue"})
    for caracterisitique in caracterisitiquesImmat:
        car["Immat"] = caracterisitique.text.lower().replace("€ ", "").replace(".", "").replace(",-", "").replace("km",
                                                                                                                  "").replace(
            "\n", "")
    caracterisitiquesPower = soup.find_all("span", {"class": "cldt-stage-primary-keyfact"})
    for caracterisitique in caracterisitiquesPower:
        label = caracterisitique.text.lower().replace("€ ", "").replace(".", "").replace(",-", "").replace("km",
                                                                                                           "").replace(
            "\n", "")
        match = re.findall("[0-9]{3} ch", label)
        if len(match) > 0:
            car["Power"] = re.findall("[0-9]{3}", match[0])[0]
    caracterisitiques = soup.find_all("div", {"class": "cldt-data-section"})
    for caracterisitique in caracterisitiques:
        vehicleDetails = caracterisitique.find_all("dl")
        if len(vehicleDetails) > 0:
            filteredList = list(filter(lambda x: str(x) != "\n", vehicleDetails[0].contents))
            for dd in range(0, len(filteredList)):
                if dd + 1 < len(filteredList):
                    if filteredList[dd].name == "dt":
                        # print(filteredList[dd].text, ": ", filteredList[dd+1].text)
                        rawText = filteredList[dd].text.lower().replace("-", " ").replace("'", " ").replace("é",
                                                                                                            "e").replace(
                            "è", "e").replace("à", "a").replace(" ", "")
                        fieldValue = str(
                            filteredList[dd + 1].text.lower().replace("\n", "").replace(",", "").replace("'",
                                                                                                         " ").replace(
                                "é", "e").replace("è", "e").replace("à", "a").replace(" ", ""))
                        if rawText in fields:
                            car[rawText] = fieldValue
    return car