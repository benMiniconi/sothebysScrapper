import csv

fields = ["Price", "Immat", "KM", "Power", "modele", "marque", "annee", "couleurexterieure", "interieur",
          "couleurexterieure", "typedepeinture", "couleuroriginale", "versionpays", "interieur", "carrosserie",
          "portes", "sieges", "cylindree", "transmission"]


def exportResult(annoncesList, modele):
    csv_columns = fields
    csv_file = "auto24" + modele + ".csv"
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in annoncesList:
                if type(data) is not str:
                    writer.writerow(data)
    except IOError:
        print("I/O error")