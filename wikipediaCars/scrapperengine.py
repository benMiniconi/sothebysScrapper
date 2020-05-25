from bs4 import BeautifulSoup
import requests
from wikipediaCars.extractdata import getDetailed, exportResult
import re



baseUrl = "https://fr.wikipedia.org/wiki/Liste_des_automobiles_Ferrari"
brand = "Ferrari"





response = requests.get(baseUrl)
data = response.text
list = []
soup = BeautifulSoup(data, "html.parser")
details = soup.find_all("div", {"class": "colonnes"})
for model in details:
    detailsa = model.find_all("a", {"title": re.compile("Ferrari")})
    for detail in detailsa:
        model = re.split(brand, detail.text)[1].strip()
        vehicule = getDetailed("https://fr.wikipedia.org"+detail.attrs["href"], model, brand)
        list.append(vehicule)
        #print("https://fr.wikipedia.org"+detail.attrs["href"])
exportResult(list, brand)


