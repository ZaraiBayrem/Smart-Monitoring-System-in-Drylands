import requests


def post_request(payload,DEVICE_LABEL,TOKEN):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
    # Makes the HTTP requests
    status = 400
    attempts = 0
    req = requests.post(url=url, headers=headers, json=payload)
    status = req.status_code    
    # Processes results
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False
    print("[INFO] request to ubidots made properly, your device is updated")
    return True

#post_request(dictionnaire)
    
