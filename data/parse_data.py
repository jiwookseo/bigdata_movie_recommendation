import requests
import json

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}


def create_users(num_users):
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
            'password': username,
            'age': age,
            'gender': gender,
            'occupation': occupation
        })

        if len(request_data['profiles']) >= num_users:
            break

    requests.post(
        API_URL + 'users/', data=json.dumps(request_data), headers=headers)


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


def create_ratings(num_users):
    rating_data = open("./ratings.dat", "r", encoding="ISO-8859-1")
    request_data = {"ratings": []}
    for line in rating_data.readlines():
        [user_id, movie_id, rating, timestamp] = line.split("::")
        if user_id > num_users:
            break
        request_data["ratings"].append({
            "username": 'user' + user_id,
            "movie_id": movie_id,
            "rating": rating,
            "timestamp": timestamp
        })

    requests.post(
        API_URL + "ratings/", data=json.dumps(request_data), headers=headers)


def create_story(num_movies):
    story_data = open("./ml_plot.dat", "r", encoding="ISO-8859-1")
    request_data = {"story": []}
    for line in story_data.readlines():
        [movie_id, story] = line.split("::")

        while "\t" in story:
            story = story.replace("\t", " ")
        while "|\n" in story:
            story = story.replace("|\n", "")

        if len(request_data["story"]) > 0 and int(movie_id) > num_movies:
            break

        request_data["story"].append({
            "movie_id": movie_id,
            "story": story
        })
    requests.post(
        API_URL + "movies/", data=json.dumps(request_data), headers=headers)


if __name__ == '__main__':
    num_users = 200
    num_movies = 3952
    # create_movies()
    # create_users(num_users)
    create_ratings(num_users)
    # create_story(num_movies)
    print('finish')
