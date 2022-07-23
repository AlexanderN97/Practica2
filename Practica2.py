import pprint
from pprint import pp
import json
from urllib import response
import requests
import csv
import os

urlo = "https://api.meraki.com/api/v1/organizations"

payload = None
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

response = requests.request('GET', urlo, headers=headers, data = payload)
orgData= json.loads(response.text)


pp(orgData)

