import requests
import json
import haversine as hs
from geopy.geocoders import Nominatim
import urllib.parse
#with open ('data.json') as f:
    #data = json.load(f)

json_str = '''
{
    "Places": [
        {
            "STREET": "Av.Protasio Alves",
            "NUMBER": "795",
            "LAT": "-3003646",
            "LONG": "-512009800"
        },
        {
            "STREET": "Av.Assis Brasil",
            "NUMBER": "3940",
            "LAT": "-3000798",
            "LONG": "-5114780"
        },
        {
            "STREET": "R.dos Andradas",
            "NUMBER": "1107",
            "LAT": "-3002826",
            "LONG": "-5123067"
        },
        {
            "STREET": "Av.Eduardo Prado",
            "NUMBER": "1844",
            "LAT": "-3013242",
            "LONG": "-5121818"
        }
    ]
}
'''


data = json.loads(json_str)


def get_coordenates(address):
    geolocator = Nominatim(user_agent="Name")
    location = geolocator.geocode(address)
    x = location.longitude
    y = location.latitude
    return x,y

def calculate_smallest_distance(address):
    list = []
    loc1 = get_coordenates(address)
    for places in data['Places']:
        street = places['STREET']
        loc2 = get_coordenates(street)
        distance = round(hs.haversine(loc1, loc2))
        list.append(distance)
    return min(list)

def check_if_place_exists(address):
    list = []
    list2 = []
    list3 = []
    loc1 = get_coordenates(address)
    for places in data['Places']:
        street = places['STREET']
        loc2 = get_coordenates(street)
        distance = round(hs.haversine(loc1, loc2))
        list.append(distance)
        list2.append(street)
        list3.append(places['NUMBER'])
        minimun = list.index(min(list))
        if(min(list) > 10000):
            return ('Desculpe, não há agencias perto deste endereço')
    return('Agência mais próxima localizada em: ' + list2[minimun] + ' N ' + list3[minimun])

def get_place(address):
    if(isinstance(address, int)):
        return 'Input Invalido!'
    else:
        return(check_if_place_exists(address))

