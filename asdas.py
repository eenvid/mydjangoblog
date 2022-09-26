import requests

headers = {
    'sec-ch-ua': '"Microsoft Edge";v="105", " Not;A Brand";v="99", "Chromium";v="105"',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://hadis.vaghteghabli.com/order',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'employeeId': '14699',
    'serviceId': '823',
    'reserveDate': 'Tue Sep 27 2022',
}

response = requests.get('https://hadis.vaghteghabli.com/api/v1/order/free-time', params=params, headers=headers)
print(response.text)