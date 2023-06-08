import requests
import uuid

url = 'https://jsonplaceholder.typicode.com'


def test_get_posts():
    assert get_posts().status_code == 200, 'something went wrong with getting posts'


def test_get_posts_id():
    get_num = 1
    get_posts_id_responce = get_posts_id(get_num)
    assert get_posts_id_responce.status_code == 200, f'something went wrong with getting posts with id {get_num}'
    get_posts_id_data = get_posts_id_responce.json()
    assert get_posts_id_data['userId'] == get_num, f'something went wrong with getting posts with id {get_num}'


def test_post_posts():
    post_posts_responce = post_posts()
    assert post_posts_responce.status_code == 201, 'something went wrong with posting posts'
    post_posts_data = post_posts_responce.json()
    post_id = post_posts_data['id']
    get_posts_id_json_data = get_posts_id(post_id).json()
    assert get_posts_id_json_data['title'] == post_posts_data['title'], 'the title does not match'
    assert get_posts_id_json_data['body'] == post_posts_data['body'], 'the body does not match'


def test_delete_posts():
    assert delete_posts().status_code == 200, 'something went wrong with deleting posts because there is no such link as /posts for delete request'


def test_delete_posts_id():
    post_posts_responce = post_posts()
    post_posts_data = post_posts_responce.json()
    del_num = post_posts_data['id']
    print(del_num)
    assert delete_posts_id(del_num).status_code == 200, f'something went wrong with deleting post {del_num}'
    get_posts_id_responce = get_posts_id(del_num)
    assert get_posts_id_responce.status_code == 404, f'the post {del_num} has not been deleted'


def get_posts():
    return requests.get(url + f'/posts/')


def get_posts_id(get_num):
    return requests.get(url + f'/posts/{get_num}')


def post_posts():
    return requests.post(url + '/posts', json=new_json())


def delete_posts():
    return requests.delete(url + '/posts/')


def delete_posts_id(del_num):
    return requests.delete(url + f'/posts/{del_num}')


def new_json():
    genid = uuid.uuid4().hex
    gentitle = f'text title for user {genid}'
    genbody = f'text body for user {genid}'

    return {
        'userId': genid,
        'title': gentitle,
        'body': genbody
    }