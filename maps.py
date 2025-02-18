import requests
import io


def get_map(coord_x, coord_y, scale):
    coord_x = coord_x
    coord_y = coord_y
    scale = scale

    apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
    map_params = {
        "ll": f"{coord_x},{coord_y}",
        "spn": f"{scale},{scale}",
        "l": "map",
        "apikey": apikey,
    }

    map_url = "https://static-maps.yandex.ru/1.x/"
    resp = requests.get(map_url, params=map_params)
    resp.raise_for_status()
    image = io.BytesIO()
    image.write(resp.content)
    return image
