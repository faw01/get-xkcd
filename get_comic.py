import requests
import webbrowser
import random

def get_xkcd():
    # fetch json of latest comic
    response = requests.get("https://xkcd.com/info.0.json")

    # extract newest comic number
    newest_comic_number = response.json()["num"]

    # generate random comic number between 1 and the
    random_comic_number = random.randint(1, newest_comic_number)

    # fetch comic json
    response = requests.get(f"https://xkcd.com/{random_comic_number}/info.0.json")

    # parse comic data
    comic = response.json()

    # display comic in new tab
    webbrowser.open_new_tab(comic["img"])

    return
