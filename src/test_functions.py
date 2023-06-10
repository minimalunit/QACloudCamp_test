import requests


url = 'https://jsonplaceholder.typicode.com'


def test_check_successful_receiving_posts():
    assert get_posts().status_code == 200, 'something went wrong with getting posts'


def test_check_successful_receiving_id_post():
    post_id_number = 10
    get_posts_id_response = get_posts_id(post_id_number)
    assert get_posts_id(post_id_number).status_code == 200, f'something went wrong with getting posts with id {post_id_number}'
    get_posts_id_data = get_posts_id_response.json()
    assert get_posts_id_data['id'] == post_id_number, f'something went wrong with getting posts with id {post_id_number}'


def test_check_error_non_existent_id_post():
    non_existent_post_id_number = 1112392111231
    assert get_posts_id(non_existent_post_id_number).status_code == 404, f'post {non_existent_post_id_number} doens\'t exist'


def test_check_successful_post_creation():
    post_posts_response = post_posts()
    assert post_posts_response.status_code == 201, 'something went wrong with posting posts'


def test_check_successful_post_creation_with_numbers_in_title():
    post_posts_response = post_posts(jsontitle='124436')
    assert post_posts_response.status_code == 201, 'something went wrong with posting posts'


def test_check_successful_post_creation_with_spchar_in_title():
    post_posts_response = post_posts(jsontitle='!?/')
    assert post_posts_response.status_code == 201, 'something went wrong with posting posts'


def test_check_successful_post_creation_with_numbers_in_body():
    post_posts_response = post_posts(jsonbody='124436')
    assert post_posts_response.status_code == 201, 'something went wrong with posting posts'


def test_check_successful_post_creation_with_spchar_in_body():
    post_posts_response = post_posts(jsonbody='!?/')
    assert post_posts_response.status_code == 201, 'something went wrong with posting posts'


def test_check_error_creation_post_with_empty_id():
    post_posts_response = post_posts(jsonid='')
    assert post_posts_response.status_code == 400, 'no userId - no post'


def test_check_error_creation_post_with_empty_title():
    post_posts_response = post_posts(jsontitle='')
    assert post_posts_response.status_code == 400, 'no title - no post'


def test_check_error_creation_post_with_empty_body():
    post_posts_response = post_posts(jsonbody='')
    assert post_posts_response.status_code == 400, 'no body - no post'


def test_check_error_creation_post_with_space_id():
    post_posts_response = post_posts(jsonid=' ')
    assert post_posts_response.status_code == 400, 'only space in userId - no post'


def test_check_error_creation_post_with_space_title():
    post_posts_responce = post_posts(jsontitle=' ')
    assert post_posts_responce.status_code == 400, 'only space in title - no post'


def test_check_error_creation_post_with_space_body():
    post_posts_response = post_posts(jsonbody=' ')
    assert post_posts_response.status_code == 400, 'only space in body - no post'


def test_check_error_creation_post_with_letter_id():
    post_posts_response = post_posts(jsonid='one')
    assert post_posts_response.status_code == 400, 'letters in userId - no post'


def test_check_error_creation_post_with_spchar_id():
    post_posts_response = post_posts(jsonid='!?')
    assert post_posts_response.status_code == 400, 'special characters in userId - no post'


def test_check_delete_posts():
    assert delete_posts().status_code == 404, 'something went wrong with deleting posts because there is no such link as /posts for delete request'


def test_check_successful_delete_post():
    delete_id = 1
    assert delete_posts_id(delete_id).status_code == 200, f'something went wrong with deleting post {delete_id}'


def test_check_error_delete_post_non_existent_id():
    delete_non_existent_id = 14123465454
    assert delete_posts_id(delete_non_existent_id).status_code == 400, f'something went wrong with deleting post {delete_non_existent_id}'


def get_posts():
    return requests.get(url + f'/posts/')


def get_posts_id(get_num):
    return requests.get(url + f'/posts/{get_num}')


def post_posts(jsonid='1', jsontitle='title', jsonbody='body'):
    json_par = {
        'userId': jsonid,
        'title': jsontitle,
        'body': jsonbody
    }
    return requests.post(url + '/posts', json=json_par)


def delete_posts():
    return requests.delete(url + '/posts/')


def delete_posts_id(del_num):
    return requests.delete(url + f'/posts/{del_num}')
