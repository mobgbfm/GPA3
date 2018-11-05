total = 98856

cat = [700, 1656, 8951, 11710, 2970, 43659, 21396, 1447, 2214]
cat_na = 4152


def calPercentage():
    totalper = total - cat_na
    for i in cat:
        percent = float("{0:.2f}".format((i / totalper)*100))
        print(percent, "%")


calPercentage()
