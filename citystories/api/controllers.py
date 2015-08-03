import requests


def get_address(location):
    response = requests.get('http://maps.googleapis.com/maps/api/geocode/json?latlng=' + location)
    data = response.json()
    street = data['results'][0]['address_components'][1]['long_name']
    number = data['results'][0]['address_components'][0]['long_name']
    return street + ' ' + number