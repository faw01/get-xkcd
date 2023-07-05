from django.shortcuts import render
from django.http import JsonResponse
from .models import Comic, ComicView
from django.contrib.auth.decorators import login_required
import requests
import random

# Create your views here.
@login_required
def get_random_comic(request):
    # fetch json of latest comic
    response = requests.get("https://xkcd.com/info.0.json")

    # extract newest comic number
    newest_comic_number = response.json()["num"]

    comic_number = None
    while True:
        # generate random comic number between 1 and the newest_comic_number
        comic_number = random.randint(1, newest_comic_number)

        # check if this comic has been viewed by the current user
        comic, created = Comic.objects.get_or_create(comic_id=comic_number)
        if not ComicView.objects.filter(comic=comic, user=request.user).exists():
            # if it hasn't been viewed, create a new ComicView object for this user and comic, and break the loop
            ComicView.objects.create(comic=comic, user=request.user)
            break

    # fetch comic json
    response = requests.get(f"https://xkcd.com/{comic_number}/info.0.json")

    # parse comic data
    comic_data = response.json()

    return JsonResponse(comic_data)

@login_required
def get_previous_comic(request):
    # get the most recent ComicView object for this user
    last_view = ComicView.objects.filter(user=request.user).latest('viewed_at')
    # get the ComicView object before that one
    previous_view = ComicView.objects.filter(user=request.user, viewed_at__lt=last_view.viewed_at).latest('viewed_at')
    # fetch the comic corresponding to previous_view
    comic_data = fetch_comic(previous_view.comic.comic_id)
    return JsonResponse(comic_data)

@login_required
def get_next_comic(request):
    # get the most recent ComicView object for this user
    last_view = ComicView.objects.filter(user=request.user).latest('viewed_at')
    # get the ComicView object after that one
    next_view = ComicView.objects.filter(user=request.user, viewed_at__gt=last_view.viewed_at).earliest('viewed_at')
    # fetch the comic corresponding to next_view
    comic_data = fetch_comic(next_view.comic.comic_id)
    return JsonResponse(comic_data)

def fetch_comic(comic_id):
    # fetch comic json
    response = requests.get(f"https://xkcd.com/{comic_id}/info.0.json")
    # parse comic data
    comic_data = response.json()
    return comic_data
