import requests


def get_address(lat, lon):
    response = requests.get('http://nominatim.openstreetmap.org/reverse?lat=' + lat + '&lon=' + lon + '&format=json')
    data = response.json()
    street = data['address']['road']
    # Not all responses has a house_number field.
    try:
        number = data['address']['house_number']
    except KeyError:
        number = ''
    return street + ' ' + number
