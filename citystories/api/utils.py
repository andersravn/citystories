import requests


def get_address(lat, lon):
    response = requests.get('http://nominatim.openstreetmap.org/reverse?lat=' + lat + '&lon=' + lon + '&format=json')
    data = response.json()

    # Not all responses has a road field, some might have a field called pedestrian instead.
    try:
        street = data['address']['road']
    except KeyError:
        try:
            street = data['address']['pedestrian']
        except KeyError:
            street = ''

    # Not all responses has a house_number field.
    try:
        number = data['address']['house_number']
    except KeyError:
        number = ''
    return street + ' ' + number
