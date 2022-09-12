from pprint import pprint
import requests
class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
    def upload_file_url(self, path, url_fail):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': path,
                  'url': url_fail
                  }
        response = requests.post(url,headers=headers , params=params)
        if response.status_code == 202:
            print("Success")
def get_photo_user(TOKEN_VK, user_id):
    url = 'https://api.vk.com/method/photos.get'
    params = {
        'access_token': TOKEN_VK,
        'owner_id': user_id,
        'album_id': 'profile',
        'extended': 1,
        'v': '5.131'
    }
    response = requests.get(url, params=params)
    return response.json()
def sort_sizes_photo(ph):
    ex = []
    all_url = []
    for photo in ph['response']['items']:
        max_size = 0
        max_size_type = ''
        for size in photo['sizes']:
            size_photo = size['height'] * size['width']
            if size_photo > max_size:
                max_size = size_photo
                max_size_type = size['type']
                max_size_url = size['url']
        all_url.append({'name': f'{photo["likes"]["count"]}.jpg','url': max_size_url}) 
        ex.append({'file_name': f'{photo["likes"]["count"]}.jpg', 'size': max_size_type})
    return ex, all_url
TOKEN_YA = ''
TOKEN_VK = ''
user_id = ''
user = YandexDisk(TOKEN_YA)
profile_photo = get_photo_user(TOKEN_VK, user_id)
sort_sizes_profile_photo, sort_url = sort_sizes_photo(profile_photo)
for unit in sort_url:
    user.upload_file_url(unit['name'], unit['url'])
pprint(sort_sizes_profile_photo)