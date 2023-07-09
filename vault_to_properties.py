import requests
import json
import re
import sys

url = sys.argv[1]
application_properties_address = sys.argv[2]
vault_token = sys.argv[3]

querystring = {}
payload = ""
headers = {"X-Vault-Token": vault_token}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
data = json.loads(response.text)
properties = data["data"]["data"]

with open(application_properties_address, "r+") as application_properties:
    text = application_properties.read()
    file_str = text
    for property_name in properties:
        new_value = properties[property_name]
        print(property_name + " = " + new_value)
        if "vault." in property_name:
            pattern = fr"({re.escape(property_name)}:)(\w+)"
            file_str = re.sub(pattern, fr"\g<1>{new_value}", file_str)
        else:
            pattern = fr"({re.escape(property_name)}=).*"
            file_str = re.sub(pattern, fr"\g<1>{new_value}", file_str)

    with open("application.properties", "w+") as file2:
        file2.write(file_str)
