import fitz  # this is pymupdf
import re
import csv
from datetime import datetime
import os

date = datetime.now().strftime("%d-%b-%Y")


def exportToCsv(file,name):
    with fitz.open(file) as doc:
        text = ""
        for page in doc:
            text += page.getText()

    text = re.findall(f"(?<={name}).*",
                      text.replace("\n", " "))
    text = ''.join(text)
    text = re.sub("(?=(Neuer)).*", "", text)
    text = re.split("(?=(PUNKTE)\s\d{2}[.]\d{2}[.]\d{4})", text)
    cleanData(text)


def cleanData(text):
    data = []
    temp = ""
    for i, string in enumerate(text, start=0):
        if(i == len(text)-1):
            data.append(string.lstrip())
        if i % 2 == 0:
            if string[0:7] == "PUNKTE ":
                string = string[6:].lstrip()
            temp = string
        else:
            temp += string
            data.append(temp)
    data_final = []
    for d in data:
        d = re.split("(\d{2}[.]\d{2}[.]\d{4})", d)
        if len(d) == 5:
            data_final.append(
                [d[1], d[2].strip(), d[3], re.findall("\d+[,]\d{2}", d[4])[0], re.findall("([+]|[-])", d[4])[0]])
            
    generateCSV(data_final)


def generateCSV(data):
    with open(f"{date}.csv", mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=';', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for row in data:
            writer.writerow(row)
    file.close()

# path to the folder where you store ur bills
path = "pdf_DIR"  
# replace with the corresponding line in your bill
visa_code_name = "Visa Karte XXXX XXXX XXXX XXXX FIRSTNAME GIVENNAME"
for file in os.listdir(path):
    if file.endswith(".pdf"):
        exportToCsv(f"path\{file}", visa_code_name) 


