import requests
from pprint import pformat
import json


def get_from_url(url, headers):
    resp = requests.get(url=url, headers=headers)
    resp.raise_for_status()
    return resp.json()


def post_to_url(url, headers, data):
    data = json.dumps(data)
    resp = requests.post(url=url, headers=headers, data=data)
    resp.raise_for_status()
    return resp.json()


class CoopApi:
    user_id = None
    auth_token = None
    headers = None
    base_url = 'http://coop.apps.symfonycasts.com'
    data = None

    def __init__(self, auth_token=None):
        if not auth_token:
            raise AttributeError('Auth token is None')
        self.auth_token = auth_token
        self.headers = {
            'Accept': 'text/html,*/*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Bearer {self.auth_token}'
        }
        self.data = {
            'access_token': self.auth_token,
            'grant_type': 'authorization_code'
        }

        # Get my user id
        self.get_my_user()

    def get_my_user(self):
        endpoint = '/api/me'
        url = self.base_url + endpoint
        resp = get_from_url(url=url, headers=self.headers)
        self.user_id = resp['id']
        print(f'User id for the auth token is {self.user_id}')

    def unlock_the_barn(self):
        endpoint = '/api/' + self.user_id + '/barn-unlock'
        url = self.base_url + endpoint
        resp = post_to_url(url=url, headers=self.headers, data=self.data)
        success = resp.get('success', False)
        if success:
            print(f"Action: {resp['action']} passed, msg: {resp['message']}")
            return True
        else:
            print(f'Action failed, response : {pformat(resp)}')
            return False

    def put_the_toilet_seat_down(self):
        endpoint = '/api/' + self.user_id + '/toiletseat-down'
        url = self.base_url + endpoint
        resp = post_to_url(url=url, headers=self.headers, data=self.data)
        success = resp.get('success', False)
        if success:
            print(f"Action: {resp['action']} passed, msg: {resp['message']}")
            return True
        else:
            print(f'Action failed, response : {pformat(resp)}')
            return False

    def feed_the_chickens(self):
        endpoint = '/api/' + self.user_id + '/chickens-feed'
        url = self.base_url + endpoint
        resp = post_to_url(url=url, headers=self.headers, data=self.data)
        success = resp.get('success', False)
        if success:
            print(f"Action: {resp['action']} passed, msg: {resp['message']}")
            return True
        else:
            print(f'Action failed, response : {pformat(resp)}')
            return False

    def collect_eggs_from_your_chickens(self):
        endpoint = '/api/' + self.user_id + '/eggs-collect'
        url = self.base_url + endpoint
        resp = post_to_url(url=url, headers=self.headers, data=self.data)
        success = resp.get('success', False)
        if success:
            print(f"Action: {resp['action']} passed, msg: {resp['message']}")
            return True
        else:
            print(f'Action failed, response : {pformat(resp)}')
            return False

    def get_the_number_of_eggs_collected_today(self):
        endpoint = '/api/' + self.user_id + '/eggs-count'
        url = self.base_url + endpoint
        resp = post_to_url(url=url, headers=self.headers, data=self.data)
        success = resp.get('success', False)
        if success:
            print(f"Action: {resp['action']} passed, msg: {resp['message']}")
            return True
        else:
            print(f'Action failed, response : {pformat(resp)}')
            return False


if __name__ == '__main__':
    # get_my_user()
    # unlock_the_barn()
    coop = CoopApi('dd9481bf03925fc05aef311bc0dc9f816e55d741')
    coop.unlock_the_barn()
    coop.put_the_toilet_seat_down()
    coop.feed_the_chickens()
    coop.collect_eggs_from_your_chickens()
    coop.get_the_number_of_eggs_collected_today()
