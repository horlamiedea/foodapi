from django.conf import settings
import requests


class SendImg():
    def __init__(self):
        self.headers = {'content-tpye': 'application/json'}
        self.url = 'https://api.logmeal.es/v2/image/recognition/type/{model_version}'
