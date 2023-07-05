# get xkcd

[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)

A simple Django-based web application that fetches XKCD comics and displays them. Users can view a random comic, or navigate to the previous or next comic.

## How it Works

The application uses Django for the backend and JavaScript for the frontend. Here's a detailed explanation of how it works:

1. **Fetching the latest comic data:** The Django server sends a GET request to the XKCD API endpoint (`https://xkcd.com/info.0.json`). This endpoint returns a JSON object that contains the information of the latest comic, including its number (`num`).

    ```python
    # fetch json of latest comic
    response = requests.get("https://xkcd.com/info.0.json")
    ```

2. **Extracting the newest comic number:** The server extracts the newest comic number from the JSON response. This number represents the ID of the latest comic and is used to determine the range of IDs that can be randomly generated in the next step.

    ```python
    # extract newest comic number
    newest_comic_number = response.json()["num"]
    ```

3. **Generating a random comic number:** The server generates a random number between 1 (representing the first comic) and the newest comic number (inclusive). This random number represents the ID of the comic that will be fetched next.

    ```python
    # generate random comic number between 1 and the newest_comic_number
    random_comic_number = random.randint(1, newest_comic_number)
    ```

4. **Fetching the random comic data:** The server sends another GET request to the XKCD API endpoint, this time appending the randomly generated comic number to the base URL (`https://xkcd.com/{random_comic_number}/info.0.json`). This endpoint returns a JSON object that contains the information of the comic corresponding to the random comic number.

    ```python
    # fetch comic json
    response = requests.get(f"https://xkcd.com/{random_comic_number}/info.0.json")
    ```

5. **Parsing and displaying the comic data:** The server parses the JSON response to extract the comic data. This data is then sent to the frontend. The JavaScript on the frontend uses this data to update the comic displayed on the webpage. The comic image is displayed in a new tab using the `webbrowser.open_new_tab(comic["img"])` function.

    ```python
    # parse comic data
    comic = response.json()

    # display comic in new tab
    webbrowser.open_new_tab(comic["img"])
    ```

Thus, each time a user interacts with the frontend (e.g., by clicking the "Next" or "Previous" buttons), this process is repeated, fetching and displaying a new random comic each time.

## Installation

Follow these steps to get this project up and running:

1. Clone this repository:
    ```
    git clone https://github.com/faw01/get-xkcd.git
    ```

2. Change to the project directory:
    ```
    cd get-xkcd
    ```

3. Install the necessary requirements:
    ```
    pip install --U -r requirements.txt
    ```

4. Run the server:
    ```
    py manage.py runserver
    ```

5. Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the project running.

## Tech stack

- Python
- Django
- JavaScript
- HTML
- CSS
