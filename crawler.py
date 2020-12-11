#Crawler for data journalism 
import requests 
import csv
from io import StringIO

PARAMS = {'start':'20170101','end':'20201111','category':'education','format':'csv'} 

file_list_apit = 'https://api.data.gov.hk/v1/historical-archive/list-files'
file_down_api = 'https://api.data.gov.hk/v1/historical-archive/get-file'

# sending get request and saving the response as response object 
r = requests.get(url = file_list_apit, params = PARAMS) 

# extracting data in json format 
if r.status_code == 200:
    data = r.json() 
    
    for file in data['files']:
        if all(word in file['resource-name-en'] for word in ['English','Employment','Graduate']) :
            file_url = file['url']
            r = requests.get(url = file_url, allow_redirects = True)
            with open('Employment Data.csv', 'w') as f:
                writer = csv.writer(f)
                for ind,line in enumerate(r.iter_lines()):
                    row = line.decode('utf-8')
                    row = row.replace(", "," | ")
                    row = row.replace('"','')
                    row = row.split(',')
                    writer.writerow(row)
