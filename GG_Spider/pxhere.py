# https://pxhere.com/
import re

import requests

url = "https://pxhere.com/"
cookie = {
    "cf_clearance":"Aa4omzA5div5GFq.MgoXxQ2DASTkcxSNx7qJI3Me9bg-1761807048-1.2.1.1-dA_KjaUw3gKsif.JiOOu1H8gZ0bM5Wf2OEgltM0JJEtwwDAraYFkHeiFgN1mRprLRotMxB3w7le7O7P71EOD.hAZrxenOAjDlWBepCnXyePUZ0kVjR5a3l1xQB7XqK91oAFnfER0Pja.hWhPv0NSh6QpPjGekgkafDQBsFynNTg_Htmap_RxjPS99.JyC7D.Hb_qQ7PlCq.NTGQzFwe0Bc4wLXDAZsMP3gl1PE5gLSOKtTwxqmDC7dsud9xQhP3i",
    "PHPSESSID":"m5n595a5el2c6d76qk4gsh4ga7"
}
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
}
response = requests.get(url)
print(response.text)
