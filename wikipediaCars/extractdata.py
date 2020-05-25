import re
from bs4 import BeautifulSoup
import requests
import csv

fieldsToManipulateWithFigure = ["production", "cylindree", "annees de production"]
fields = ["puissance maximale", "modele", "marque", "annee", "carrosserie",
          "portes", "sieges", "cylindree", "transmission", "moteur",
          "production", "position du moteur", "classe", "annees de production"]


def extractData(label, value):
    if label in fieldsToManipulateWithFigure:
        match = re.findall("[0-9]{3,4}", value.replace(" ", ""))
        if len(match) > 0:
            value = match[0]
    if label == "puissance maximale":
        match = re.split("min", value.lower().replace(" ", ""))
        if len(match) > 1:
            value = re.findall("[0-9]{3}", match[1])[0]
    return value


def getDetailed(detailUrl, model, brand):
    response = requests.get(detailUrl)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    vehicule = {"puissance maximale": "", "modele": model, "marque": brand.replace("\n", ""), "annee": "", "carrosserie": "",
                "portes": "", "sieges": "", "cylindree": "", "transmission": "", "moteur": "",
                "production": "", "position du moteur": "", "classe": "", "annees de production": ""}
    detailTable = soup.find_all("table", {"class": "infobox_v2"})
    for table in detailTable:
        trs = table.find_all("tr")
        for tr in trs:
            keys = tr.find_all("th")
            values = tr.find_all("td")
            for key in range(0, len(keys)):
                if key < len(values):
                    label = keys[key].text.lower().replace("€ ", "").replace("(s)", "").replace(".", "").replace(",-",
                                                                                                                 "").replace(
                        "\n", "").replace("é", "e")
                    if label in fields:
                        #print(label, values[key].text)
                        vehicule[label] = extractData(label, values[key].text).replace("\n", "").replace('"', "")

    return vehicule


def exportResult(annoncesList, brand):
    csv_columns = fields
    csv_file = "wikicar" + brand + ".csv"
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in annoncesList:
                if type(data) is not str:
                    writer.writerow(data)
    except IOError:
        print("I/O error")
