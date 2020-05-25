import pandas as pd

from modulesauto.auto24export import exportResult
from modulesauto.auto24cleaner import searchNextPage

c63 = "https://www.autoscout24.fr/lst/mercedes-benz/c-63-amg?sort=standard&desc=0&ustate=N%2CU&atype=C&size=20"
m3 = "https://www.autoscout24.fr/lst/bmw/m3?sort=standard&desc=0&ustate=N%2CU&size=20&atype=C&"
rs4 = "https://www.autoscout24.fr/lst/audi/rs4?sort=standard&desc=0&ustate=N%2CU&size=20&atype=C&"
z4 = "https://www.autoscout24.fr/lst/bmw/z4?sort=standard&desc=0&ustate=N%2CU&size=20&atype=C&"
m135i = "https://www.autoscout24.fr/lst/bmw/135?sort=standard&desc=0&ustate=N%2CU&size=20&atype=C&"
ferrari = "https://www.autoscout24.fr/lst/ferrari?sort=standard&desc=0&ustate=N%2CU&size=20&atype=C&"
porsche = "https://www.autoscout24.fr/lst/porsche?sort=standard&desc=0&ustate=N%2CU&size=20&atype=C&"
aston = "https://www.autoscout24.fr/lst/aston-martin?sort=standard&desc=0&ustate=N%2CU&size=20&atype=C&"
maserati = "https://www.autoscout24.fr/lst/maserati?sort=standard&desc=0&ustate=N%2CU&size=20&atype=C&"
alfaGiulia = "https://www.autoscout24.fr/lst/alfa-romeo/giulia?sort=standard&desc=0&ustate=N%2CU&size=20&page=1&powerfrom=331&powertype=hp&atype=C&"

C63 = []
M3 = []
RS4 = []
Z4 = []
M135 = []
Porsche = []
Ferrari = []
ASTON = []
MASERATI = []
ALFA = []
for year in range(2015, 2020):
    # searchNextPage(link, annonces, "1", 21, )
    # exportResult(annonces, "C63")
    year = str(year)
    #searchNextPage(ferrari, Ferrari, "1", 21, year, year)
    #exportResult(Ferrari, "Ferrari"+year)

    searchNextPage(alfaGiulia, ALFA, "1", 21, year, year)
    exportResult(ALFA, "ALFA"+year)
    #searchNextPage(m135i, M135, "1", 21, "", "")
    #exportResult(M135, "M135")

#searchNextPage(c63, C63, "1", 21, "2012", "2014")
#exportResult(C63, "C632012")
#searchNextPage(m3, M3, "1", 21, "2010")
#exportResult(M3, "M3")
