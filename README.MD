# ACP - Amazon Credit Card(LBB) Bill to CSV

This littel Script is able to go through the Amazon Credit Card Bill PDF and export the table in to a csv.

Only works with the german version

## Requirements
```bash
pip install PyMuPDF
````


## Usage

Edit the path and the pattern line to match your case

```python
# path to the folder where you store ur bills
path = "pdf_DIR"  
# replace with the corresponding line in your bill
visa_code_name = "Visa Karte XXXX XXXX XXXX XXXX FIRSTNAME GIVENNAME"
for file in os.listdir(path):
    if file.endswith(".pdf"):
        exportToCsv(f"path\{file}", visa_code_name) 

```

## Example Outout
Note: Script Output doesnt include a csv Header
````csv
date_bought;desc;date_billed;Sum_in_€;type
"01.01.2021";"sample desc 1";"02.01.2021";"17,70";"+"
"03.01.2021";"sample desc 2";"04.01.2021";"17,70";"-"
````


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
