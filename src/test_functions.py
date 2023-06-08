import requests

url = 'https://jsonplaceholder.typicode.com'

json_par = {
    'userId': '1',
    'title': 'title',
    'body': 'body'
}


def test_get_posts():
    assert get_posts().status_code == 200, 'something went wrong with getting posts'


def test_get_posts_id():
    get_num = 1
    get_posts_id_responce = get_posts_id(get_num)
    assert get_posts_id(get_num).status_code == 200, f'something went wrong with getting posts with id {get_num}'
    get_posts_id_data = get_posts_id_responce.json()
    assert get_posts_id_data['userId'] == get_num, f'something went wrong with getting posts with id {get_num}'


def test_post_posts():
    post_posts_responce = post_posts()
    assert post_posts_responce.status_code == 201, 'something went wrong with posting posts'


def test_delete_posts():
    assert delete_posts().status_code == 200, 'something went wrong with deleting posts'


def test_delete_posts_id():
    del_num = 1
    assert delete_posts_id(del_num).status_code == 200, f'something went wrong with deleting post {del_num}'


def get_posts():
    return requests.get(url + f'/posts/')


def get_posts_id(get_num):
    return requests.get(url + f'/posts/{get_num}')


def post_posts():
    return requests.post(url + '/posts', json=json_par)


def delete_posts():
    return requests.delete(url + '/posts/')


def delete_posts_id(del_num):
    return requests.delete(url + f'/posts/{del_num}')
