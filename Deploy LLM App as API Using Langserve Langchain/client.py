import requests

responce = requests.post(
    'http://localhost:8000/essay/invoke',
    json={'input':{'topic':'apple'}})

print(responce.json()['output']['content'])

print("__________________________________________________________________________")
responce1 = requests.post(
    'http://localhost:8000/poem/invoke',
    json={'input':{'topic':'apple'}})

print(responce1.json()['output']['content'])


