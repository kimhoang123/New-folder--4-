#bai 4s
date = input("MM/DD/YYYY")

def changeFormatDate(date):

    month=date[:2]
    day=date[(slice(3,5))]
    year=date[-4:]
    return day + "/"+month+"/"+year

print(changeFormatDate(date=dateInput))