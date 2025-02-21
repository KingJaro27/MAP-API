import requests
import io
from PIL import Image


def get_map(coord_x, coord_y, scale):
    
    apikey = "0fb296a1-6cd6-486e-bb8b-b680e29d3080" 
    '''f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'''
    map_params = {
        "ll": f"{coord_x},{coord_y}",
        "z": f"{scale}",
        "l": "map",
        "size": "650,450",
        #"apikey": apikey,
    }

    map_url = "https://static-maps.yandex.ru/1.x/"
    resp = requests.get(map_url, params=map_params)
    resp.raise_for_status()
    image = io.BytesIO()
    image.write(resp.content)
    ii = Image.open(image)
    ii.show()
    return image


#get_map(4, 44, 11)
