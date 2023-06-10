import requests


url = 'https://jsonplaceholder.typicode.com'


def test_check_successful_receiving_posts():
    assert get_posts().status_code == 200, 'something went wrong with getting posts'


def test_check_successful_receiving_id_post():
    get_num = 1
    get_posts_id_response = get_posts_id(get_num)
    assert get_posts_id_response.status_code == 200, f'something went wrong with getting posts with id {get_num}'
    get_posts_id_data = get_posts_id_response.json()
    assert get_posts_id_data['userId'] == get_num, f'something went wrong with getting posts with id {get_num}'


def test_check_error_non_existent_id_post():
    get_nenum = 1112392111231
    assert get_posts_id(get_nenum).status_code == 404, f'post {get_nenum} doens\'t exist'


def test_check_successful_post_creation():
    post_posts_response = post_posts()
    assert post_posts_response.status_code == 201, 'something went wrong with posting posts'
    post_posts_data = post_posts_response.json()
    post_id = post_posts_data['id']
    get_posts_id_json_data = get_posts_id(post_id).json()
    assert get_posts_id_json_data['title'] == post_posts_data['title'], 'the title does not match'
    assert get_posts_id_json_data['body'] == post_posts_data['body'], 'the body does not match'
    assert get_posts_id_json_data['userId'] == post_posts_data['userId'], 'the userId does not match'


def test_check_error_creation_post_with_empty_id():
    post_posts_response = post_posts(jsonId='')
    assert post_posts_response.status_code == 400, 'no userId - no post'


def test_check_error_creation_post_with_empty_title():
    post_posts_response = post_posts(jsontitle='')
    assert post_posts_response.status_code == 400, 'no title - no post'


def test_check_error_creation_post_with_empty_body():
    post_posts_response = post_posts(jsonbody='')
    assert post_posts_response.status_code == 400, 'no body - no post'


def test_check_error_creation_post_with_space_id():
    post_posts_response = post_posts(jsonId=' ')
    assert post_posts_response.status_code == 400, 'only space in userId - no post'


def test_check_error_creation_post_with_space_title():
    post_posts_response = post_posts(jsontitle=' ')
    assert post_posts_response.status_code == 400, 'only space in title - no post'


def test_check_error_creation_post_with_space_body():
    post_posts_response = post_posts(jsonbody=' ')
    assert post_posts_response.status_code == 400, 'only space in body - no post'


def test_check_error_creation_post_with_letter_id():
    post_posts_response = post_posts(jsonId='one')
    assert post_posts_response.status_code == 400, 'letters in userId - no post'


def test_check_error_creation_post_with_spchar_id():
    post_posts_response = post_posts(jsonId='!?')
    assert post_posts_response.status_code == 400, 'special characters in userId - no post'


def test_check_delete_posts():
    assert delete_posts().status_code == 404, 'something went wrong with deleting posts because there is no such link as /posts for delete request'


def test_check_successful_delete_post():
    post_posts_response = post_posts()
    post_posts_data = post_posts_response.json()
    del_num = post_posts_data['id']
    print(del_num)
    assert delete_posts_id(del_num).status_code == 200, f'something went wrong with deleting post {del_num}'
    get_posts_id_response = get_posts_id(del_num)
    assert get_posts_id_response.status_code == 404, f'the post {del_num} has not been deleted'


def test_check_error_delete_post_non_existent_id():
    del_num = 14123465454
    assert delete_posts_id(del_num).status_code == 400, f'something went wrong with deleting post {del_num}'


def get_posts():
    return requests.get(url + f'/posts/')


def get_posts_id(get_num):
    return requests.get(url + f'/posts/{get_num}')


def post_posts(jsonId='1', jsontitle='title', jsonbody='body'):
    json_par = {
        'userId': jsonId,
        'title': jsontitle,
        'body': jsonbody
    }
    return requests.post(url + '/posts', json=json_par)


def delete_posts():
    return requests.delete(url + '/posts/')


def delete_posts_id(del_num):
    return requests.delete(url + f'/posts/{del_num}')


