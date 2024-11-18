import requests
url="http://127.0.0.1:5000/"
files={'file': open('your_csv_file.csv','rb')}
response=requests.post(url,files=files)

print(response.json())