import re

cleaners = ["s.a.a", "sarl", "sas", "eurl", "e.u.r.l", "<", ">", "#", "@", ".fr", "^", "$", "gmbh", "_", "-", "/",
            ".com", "add", "merge", "(", ")", ":"]

features = {"Import Fec": ["import fec", "importfec", "fec", "fec import", "importing"],
            "Pieces Manquantes": ["piecesmanquantes", "pieces manquantes", "manquantes", "missing"],
            "Messagerie": ["messagerie", "publi", "ticket"],
            "Saisie Manuelle": ["saisie manuel", "saisie manuelle", "saisi", "manual"],
            "Grand Livre": ["grandlivre", "grand livre"],
            "Journaux": ["journal", "journaux", "entry", "entries"],
            "Balance": ["balance"],
            "Lettering": ["lettering", "lettrage", "lettr", "letter"],
            "Bilan et CDR": ["bilan", "compte de re"],
            "Immos": ["asset", "immo"],
            "Upload": ["telecha", "upload", "achat", "vente"],
            "Anouveaux": ["a nouveau"],
            "Revision": ["revision", "révision"],
            "Export": ["export"],
            "Teledeclaration": ["edi", "liasse", "eportal"],
            "Dossier Permanent": ["permanent", "pérmanent", "dossier permanent", "dossierpermanent",
                                  "dossier entreprise", "dossier ent"],
            "TVA": ["tva", "vat"],
            "Banque": ["bank", "banque"],
            "Design": ["design", "button", "color", "typo", "icon"],
            "Dark": ["dark"],
            "CompteUser": ["onboard", "invite", "home", "users", "profil", "collab", "password", "login"],
            "Search": ["search", "filter"],
            "Facturation": ["billing", "factu"]
            }


def cleanString(rawStringArray):
    a = 0
    while a < len(rawStringArray.values):
        print(a)
        print(len(rawStringArray.values))
        label = rawStringArray.values[a]
        if type(label) is str:
            print("cleanLabel", label)
            label = replaceCommmonMistake(label.lower())
            rawStringArray.values[a] = label

        a = a + 1
    return rawStringArray


def replaceCommmonMistake(label):
    for cleaner in cleaners:
        label = label.replace(cleaner, " ")
    return label


def extractFeatureFromCommitTitle(rawStringArray):
    a = 0
    while a < len(rawStringArray.values):
        print(a)
        print(len(rawStringArray.values))
        label = rawStringArray.values[a]
        if type(label) is str:
            label = proceedFeatureExtraction(label)
            rawStringArray.values[a] = label

        a = a + 1
    return rawStringArray


def proceedFeatureExtraction(label):
    for feature in features.keys():
        for wordToMatch in features[feature]:
            if re.findall(wordToMatch, label):
                label = feature
    return label
