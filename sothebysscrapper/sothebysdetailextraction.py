import requests
import time
from bs4 import BeautifulSoup
brands = ["alfa romeo", "mercedes", "porsche", "ferrari", "bmw", "maserati", "aston martin", "mercedes benz"]
fields = ["Price", "Immat", "KM", "Power", "modele", "marque", "annee", "couleurexterieure", "interieur",
          "couleurexterieure", "typedepeinture", "couleuroriginale", "versionpays", "interieur", "carrosserie",
          "portes", "sieges", "cylindree", "transmission"]
template = {'Vente': '', 'VenteYear': ['1963'], 'marque': 'porsche', 'annee': '1965', 'modele': '356c cabriolet', 'Price': '45100'}
import re
import csv
from modulesauto.auto24export import fields


def extractLot(page_source, year):
    #pass source page coming from selenium to beautiful parser
    soup = BeautifulSoup(page_source, "html.parser")
    #filter dom to H2 sale title
    auction_title_elements = soup.find_all("h2", {"class": "tile__title"})
    auction_title = ""
    for title in auction_title_elements:
        print("title", title.text)
        auction_title = title.text
    vehicleExtraDetails = soup.find_all("div", {"class": 'RMAuctions'})
    # loop into lots whom class is RMSothebys
    vehicleExtraDetailsSoth = soup.find_all("div", {"class": 'RMSothebys'})
    lotsToLoop = vehicleExtraDetails if len(vehicleExtraDetails) > 0 else vehicleExtraDetailsSoth
    lots = []
    for lot in lotsToLoop:
        vehicule = {}
        vehicule["Vente"] = auction_title
        vehicule["VenteYear"] = year
        vehicleDetails = lot.find_all("p")
        for detail in vehicleDetails:
            label = detail.text.lower().replace("-", " ").replace("'", " ").replace("é","e").replace("è", "e").replace("à", "a").replace(",", "").replace("$", "usd")
            for brandP in brands:
                brand = re.findall(brandP, label)
                if len(brand) > 0:
                    print("brand", brand[0])
                    vehicule["marque"] = brand[0]
                    yearImmat = re.findall("[0-9]{4}", label)
                    if len(yearImmat) > 0:
                        print("year", yearImmat[0])
                        vehicule["annee"] = yearImmat[0]
                    model = re.split(brandP, label)[1]
                    model = model.strip()
                    vehicule["modele"] = model
                    print("model", model)
                price = re.findall("sold for", label)
                if len(price) > 0:
                    #print("price", re.findall("[0-9]{4,10}", label)[0])
                    vehicule["Price"] = re.findall("[0-9]{1,10}", label)[0]
            print(vehicule)
            if "Price" in vehicule.keys() and "marque" in vehicule.keys():
                lots.append(vehicule)
    return lots


def exportResult(annoncesList, vente, year):
    csv_columns = template.keys()
    csv_file = "sothebys"+vente+str(year)+".csv"
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in annoncesList:
                if type(data) is not str:
                    writer.writerow(data)
    except IOError:
        print("I/O error")
