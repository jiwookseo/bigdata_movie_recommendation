import jwt
import datetime
from rest_framework import status


SECRET = "Honeybee"

def create_token(username):
    encoded = jwt.encode(
        {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
            "username": username
        },
        SECRET + username, algorithm="HS256",
    )
    return encoded


def validate_token(token, username):
    try:
        jwt.decode(token, SECRET + username, algorithms="HS256")
    except jwt.ExpiredSignatureError:
        return status.HTTP_401_UNAUTHORIZED
    except jwt.InvalidTokenError:
        return status.HTTP_401_UNAUTHORIZED
    else:
        return True