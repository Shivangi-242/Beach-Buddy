import requests
import json

url = "https://samudra.incois.gov.in/incoismobileappdata/rest/incois/currentslatestdata"

payload = ""
headers = {
    "^Accept": "*/*^",
    "^Accept-Language": "en-US,en;q=0.6^",
    "^Connection": "keep-alive^",
    "^Origin": "https://incois.gov.in^",
    "^Referer": "https://incois.gov.in/^",
    "^Sec-Fetch-Dest": "empty^",
    "^Sec-Fetch-Mode": "cors^",
    "^Sec-Fetch-Site": "same-site^",
    "^Sec-GPC": "1^",
    "^User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36^",
    "^sec-ch-ua": "^\^Chromium^^;v=^\^130^^, ^\^Brave^^;v=^\^130^^, ^\^Not?A_Brand^^;v=^\^99^^^",
    "^sec-ch-ua-mobile": "?0^",
    "^sec-ch-ua-platform": "^\^Windows^^^"
}

response = requests.request("GET", url, data=payload, headers=headers)

jsondata = json.loads(response.text)

currents_json = json.loads(jsondata['CurrentsJson'])

for current in currents_json:
    district = current['District']
    state = current['STATE']
    message = current['Message']
    alert = current.get('Alert', 'No alert')
    color = current.get('Color', 'No color specified')
    issue_date = current.get('Issue Date', 'No issue date specified')
    
    print(f"District: {district}")
    print(f"State: {state}")
    print(f"Message: {message}")
    print(f"Alert: {alert}")
    print(f"Color: {color}")
    print(f"Issue Date: {issue_date}")
    
print(f"Latest Currents Date: {jsondata['LatestCurrentsDate']}")