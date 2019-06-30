import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

results_file = 'results.csv'

tickers = [ 'HITK', 'MSFT', 'AAPL', 'TSLA' ]

for ticker in tickers:
    url = "https://www.nasdaq.com/symbol/" + ticker + "/short-interest"
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    if soup.find_all("table", {"id": "quotes_content_left_ShortInterest1_ShortInterestGrid"}):
        table = soup.findAll("table", {"id":"quotes_content_left_ShortInterest1_ShortInterestGrid"})[0]
        rows = table.findAll("tr")

        with open(results_file, 'a', encoding="utf8", newline="") as f:
            writer = csv.writer(f)
            for row in rows:
                counter = 0 
                csv_row = []
                csv_row.append(ticker)
                cells = row.findAll(["td"])
                for cell in cells:
                    cell_text = cell.get_text()
                    csv_row.append(cell_text)
                    counter = counter + 1
                if(counter and csv_row):
                    writer.writerow(csv_row)

rows = csv.reader(open(results_file, 'r'))
newrows = []
for row in rows:
    if row not in newrows:
        newrows.append(row)
writer = csv.writer(open(results_file, 'w', encoding="utf8", newline=""))
writer.writerows(newrows)


