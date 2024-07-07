import requests

payloadData = {
    "sid": str("643"),
    "merchant_key": "9cj4aj2b53jmk6c534c2sufrop750ab39407e34jnh04bic07l9cyd2ziuytmn6kchka",
    "service": "deposit",
    "method" : "BankTransfer",
    "user_id": "ce7bb4d2-3377-4cf0-9ecb-64101e7b7635",
    "username": "Ömer Özhan",
    "amount": str("100"),
    "currency": "TRY",
    "transaction_id": "none",
    "status": "S",
    "data": "",
    "trx": "instance.trx",
    "siteId": "merchant.site_id",
    "siteName": "merchant.site"
}

headers = {
'Content-Type': 'application/json'
}

_PAYMENT_URL = "https://kadromilyon.com/api/kralpy"

response = requests.request("POST", _PAYMENT_URL, headers=headers, json=payloadData, verify=False)
status_code, text = response.status_code, response.text

print(status_code)
print(text)
