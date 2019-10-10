import requests
import json
import os

NODE_ENV = os.environ.get("NODE_ENV", "develop")
API_URL = 'http://52.78.81.59:8000/api/' if NODE_ENV == "production" else 'http://localhost:8000/api/'
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
    count = 0
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
            requests.post(
                API_URL + 'signup/', data=json.dumps(request_data), headers=headers)
            request_data = {'profiles': []}
            count += 1
            print("Finish creating {} users".format(count * 1000))
    requests.post(
        API_URL + 'signup/', data=json.dumps(request_data), headers=headers)
    print("Finish creating {} users".format(
        count * 1000 + len(request_data['profiles'])))


def create_movies():
    movie_data = open('./movies.dat', 'r', encoding='ISO-8859-1')
    request_data = {'movies': []}
    count = 0
    for line in movie_data.readlines():
        [id, title, genres] = line.split('::')
        genres = genres[:-1].split('|')
        request_data['movies'].append({
            'id': id,
            'title': title,
            'genres': genres
        })
        if len(request_data['movies']) == 1000:
            requests.post(
                API_URL + 'movies/', data=json.dumps(request_data), headers=headers)
            request_data = {'movies': []}
            count += 1
            print("Finish creating {} movies".format(count * 1000))
    requests.post(
        API_URL + 'movies/', data=json.dumps(request_data), headers=headers)
    print("Finish creating {} movies".format(
        count * 1000 + len(request_data['movies'])))


def create_ratings():
    rating_data = open("./ratings.dat", "r", encoding="ISO-8859-1")
    request_data = {"ratings": []}
    count = 0
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
            request_data = {'ratings': []}
            count += 1
            print("Finish creating {} ratings".format(count * 1000))
    requests.post(API_URL + "ratings/",
                  data=json.dumps(request_data), headers=headers)
    print("Finish creating {} ratings".format(
        count * 1000 + len(request_data['ratings'])))


def create_story():
    story_data = open("./ml_plot.dat", "r", encoding="ISO-8859-1")
    request_data = {"story": []}
    count = 0
    for line in story_data.readlines():
        [movie_id, story] = line.split("::")

        while "\t" in story:
            story = story.replace("\t", " ")
        while "|\n" in story:
            story = story.replace("|\n", "")

        request_data["story"].append({
            "movie_id": movie_id,
            "story": story
        })
        if len(request_data['story']) == 1000:
            requests.post(API_URL + "movies/",
                          data=json.dumps(request_data), headers=headers)
            request_data = {'story': []}
            count += 1
            print("Finish creating {} stories".format(count * 1000))
    requests.post(
        API_URL + "movies/", data=json.dumps(request_data), headers=headers)
    print("Finish creating {} stories".format(
        count * 1000 + len(request_data['story'])))


if __name__ == '__main__':
    # create_movies()
    # create_users()
    create_ratings()
    create_story()
