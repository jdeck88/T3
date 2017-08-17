from bs4 import BeautifulSoup
import csv
import requests
import codecs

# Run the discovery environment
# NOTE: this function a bit of a hack as it is calling a development website
# and relies on scraping HTML... better to install service directly
def run_discovery(input_file, output_file):
    discovery_url = 'http://verbs.colorado.edu/~ribh9977/cgi-bin/run.cgi'
    files = {'text': open(input_file, 'rb'), 'dropdown': 'Text'}
    #files = {'text': codecs.open(input_file, encoding='utf-8'),'dropdown': 'Text'}

    r = requests.post(discovery_url, files=files)
    # NOTE: need to find a better way around encoding errors
    html = r.text.encode('ascii','ignore')
    html = r.text
    print(html)

    soup = BeautifulSoup(html,'html.parser')
    table = soup.find("table")
    # python3 just use th.text
    headers = [th.text for th in table.select("tr th")]

    with open(output_file, "w") as f:
        wr = csv.writer(f)
        wr.writerow(headers)
        wr.writerows([[td.text for td in row.find_all("td")] for row in table.select("tr + tr")])
