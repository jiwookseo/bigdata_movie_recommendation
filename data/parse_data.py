import requests
import json

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}


def create_users():
    user_data = open('./users.dat', 'r', encoding='ISO-8859-1')
    request_data = {'profiles': []}
    occupation_map = {
        0: "other", 1: "academic/educator", 2: "artist", 3: "clerical/admin", 4: "college/grad student",
        5: "customer service", 6: "doctor/health care", 7: "executive/managerial", 8: "farmer", 9: "homemaker",
        10: "K-12 student", 11: "lawyer", 12: "programmer", 13: "retired", 14: "sales/marketing",
        15: "scientist", 16:  "self-employed", 17: "technician/engineer", 18: "tradesman/craftsman",
        19: "unemployed", 20: "writer"
    }

    for line in user_data.readlines():
        [user_id, gender, age, occupation, zipcode] = line.split('::')
        username = 'user' + user_id
        age = int(age)
        occupation = occupation_map[int(occupation)]

        request_data['profiles'].append({
            'username': username,
            'password1': "uvuvuvuv",
            'password2': "uvuvuvuv",
            'age': age,
            'gender': gender,
            'occupation': occupation
        })

        if len(request_data['profiles']) == 1000:
            response = requests.post(
                API_URL + 'signup/', data=json.dumps(request_data), headers=headers)
            request_data = {'profiles': []}
    response = requests.post(
        API_URL + 'signup/', data=json.dumps(request_data), headers=headers)
    print(response.text)


def create_movies():
    movie_data = open('./movies.dat', 'r', encoding='ISO-8859-1')
    request_data = {'movies': []}
    for line in movie_data.readlines():
        [id, title, genres] = line.split('::')
        genres = genres[:-1].split('|')
        request_data['movies'].append({
            'id': id,
            'title': title,
            'genres': genres
        })

    requests.post(
        API_URL + 'movies/', data=json.dumps(request_data), headers=headers)


def create_ratings():
    rating_data = open("./ratings.dat", "r", encoding="ISO-8859-1")
    request_data = {"ratings": []}
    for line in rating_data.readlines():
        [user_id, movie_id, rating, timestamp] = line.split("::")
        request_data["ratings"].append({
            "username": 'user' + user_id,
            "movie_id": movie_id,
            "rating": rating,
            "timestamp": timestamp
        })
        if len(request_data['ratings']) == 1000:
            requests.post(API_URL + "ratings/",
                          data=json.dumps(request_data), headers=headers)
            request_data = {"ratings": []}
    requests.post(API_URL + "ratings/",
                  data=json.dumps(request_data), headers=headers)


def create_story():
    story_data = open("./ml_plot.dat", "r", encoding="ISO-8859-1")
    request_data = {"story": []}
    for line in story_data.readlines():
        [movie_id, story] = line.split("::")

        while "\t" in story:
            story = story.replace("\t", " ")
        while "|\n" in story:
            story = story.replace("|\n", "")

        if len(request_data['story']) == 1000:
            requests.post(
                API_URL + "movies/", data=json.dumps(request_data), headers=headers)
            request_data = {"story": []}

        request_data["story"].append({
            "movie_id": movie_id,
            "story": story
        })
    requests.post(
        API_URL + "movies/", data=json.dumps(request_data), headers=headers)


if __name__ == '__main__':
    # create_movies()
    # create_users()
    create_ratings()
    create_story()
    print('finish')
