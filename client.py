# This script sends a POST request to an API endpoint with input data structured as a JSON object containing
# a topic. 
# It then extracts and prints the content from the JSON response received from the server

import requests


print("=======================================Essay===========================================")
try:
    # Invoking the api endpoint for the topic provided for essay
    response1 = requests.post(
        "http://localhost:8000/essay/invoke",
        json={'input':{'topic':"my best friend"}})
    # Check if the request was successful (status code 200)
    if response1.status_code == 200:
        print(response1.json()['output']['content'])
    else:
        print(f"Error: {response1.status_code} - {response1.reason}")

except requests.exceptions.ConnectionError as e:
    print(f"Connection Error: {e}")




print("=======================================Poem===========================================")

try:
    # Invoking the api endpoint for the topic provided for poem
    response2 = requests.post(
        "http://localhost:8000/poem/invoke",
        json={'input':{'topic':"my best friend"}})
    
    # Check if the request was successful (status code 200)
    if response2.status_code == 200:
        print(response2.json()['output']['content'])
    else:
        print(f"Error: {response2.status_code} - {response2.reason}")
    
except requests.exceptions.ConnectionError as e:
    print(f"Connection Error: {e}")