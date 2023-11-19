import requests

AGIFY_ENDPOINT = "https://api.agify.io"
GENDER_ENDPOINT = "https://api.genderize.io"
BLOGS_API = "https://api.npoint.io/c790b4d5cab58020d391"


class APIGuesser:
    def __init__(self, name):
        self.name = name
        self.guessed_age = self.get_age()
        self.guessed_gender = self.get_gender()

    def get_age(self):
        response = requests.get(
            url=AGIFY_ENDPOINT,
            params={
                "name": self.name
            }
        )
        return response.json()['age']

    def get_gender(self):
        response = requests.get(
            url=GENDER_ENDPOINT,
            params={
                "name": self.name
            }
        )
        return response.json()['gender']


class BlogGetter:
    def __init__(self):
        self.blogs = None
        self.get_blogs()

    def get_blogs(self):
        response = requests.get(BLOGS_API)
        self.blogs: [] = response.json()
