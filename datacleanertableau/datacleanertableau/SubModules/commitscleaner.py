import re as reg
patterns = ["S.A.S", "SARL", "SAS", "EURL", "E.U.R.L", "bank", "DESIGN"]


def cleanCommitsDescription(x):
    print("inModule")
    for pattern in patterns:
        if reg.search(pattern, x):
            print("Matched")
        else:
            print("unmatched")
    return x