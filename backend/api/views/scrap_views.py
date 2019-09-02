from io import BytesIO
from PIL import Image
import os
import requests
import time
from bs4 import BeautifulSoup as bs
import webbrowser
from api.models import Movie
from rest_framework.response import Response

def scrap_poster(request):
    movies = Movie.objects.filter(poster="")
    print(len(movies), "개 스크래핑 해야합니다.")
    print("입력한 아이디", os.getenv("NAVER_ID"))
    
    headers = {"X-Naver-Client-Id": os.getenv("NAVER_ID"),
               "X-Naver-Client-Secret": os.getenv("NAVER_SECRET")}
    info_url = "https://openapi.naver.com/v1/search/movie.json"
    for movie in movies:
        end = movie.title.index("(")
        year = movie.title[end + 1: -1]
        params = {"query": movie.title[:end - 1],
                  "yearfrom": year, "yearto": year}
        doc = requests.get(info_url, params=params,
                           headers=headers).json()
        if doc.get("total"):
            link = doc["items"][0]["link"]

            # Get poster
            poster = link.replace(
                "basic.nhn?code", "photoViewPopup.nhn?movieCode")
            res = requests.get(poster).text
            doc2 = bs(res, 'html.parser')
            res = doc2.find("img")
            if res:
                poster_url = res.get("src")
                movie.poster = poster_url
                # webbrowser.open_new_tab(poster_url)

            # Get still-cut
            still_cut = link.replace(
                "basic", "photoView")
            res = requests.get(still_cut).text
            doc2 = bs(res, 'html.parser')
            res = doc2.find_all(alt="STILLCUT")
            for img in res:
                still_cut_url = img.get("src")
                end = still_cut_url.find("?")
                if end == -1:
                    continue
                still_cut_url = still_cut_url[:end]
                response = requests.get(still_cut_url, stream=True)
                im = Image.open(BytesIO(response.content))
                if im.size[0] / im.size[1] > 1.33:
                    movie.still_cut = still_cut_url
                    # webbrowser.open_new_tab(still_cut_url)
                    break
            print(movie.id, "finish")
            movie.save()
    return Response()
