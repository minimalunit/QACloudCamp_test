## QACloudCamp_test
### Тестовое задание для QACloudCamp

Набор тестов <i>test_functions.py</i> содержит набор тестов на <b>GET /posts</b>, <b>POST /posts</b>, <b>DELETE /posts</b>. Добавлен вариант <b>GET /posts/id</b> и <b>DELETE /posts/id</b> (в спецификациях для <i>https://jsonplaceholder.typicode.com/</i> отсутствует DELETE /posts).

Набор тестов <i>test_functions_if.py</i> содержит аналогичный набор тестов, однако предполагает что изменения действительно происходят на сервере и их можно проверить, поэтому в нем вылезают ошибки (ведь сервер имитирует изменения, а не производит их).

Для запуска Dockerfile в директории проекта необходимо ввести команду "<i>docker build -t qacloudcamp_test &nbsp;.</i>", для запуска тестирования ввести команду "<i>docker run qacloudcamp_test</i>".

Список тестов:

1. <b>test_check_successful_receiving_posts</b> - проверка успешного запроса GET /posts для получения всех постов
2. <b>test_check_successful_receiving_id_post</b> - проверка успешного запроса GET /posts/id с существующим id для получения поста с заданным id
3. <b>test_check_error_non_existent_id_post</b> - проверка ошибки для запроса GET /posts/id с несуществующим id
4. <b>test_check_successful_post_creation</b> - проверка успешного запроса POST /posts для создания поста
5. <b>test_check_successful_post_creation_with_numbers_in_title</b> - проверка успешного запроса POST /posts для создания поста с цифрами в поле title
6. <b>test_check_successful_post_creation_with_spchar_in_title</b> - проверка успешного запроса POST /posts для создания поста с спецсимволами в поле title 
7. <b>test_check_successful_post_creation_with_numbers_in_body</b> - проверка успешного запроса POST /posts для создания поста с цифрами в поле body
8. <b>test_check_successful_post_creation_with_spchar_in_body</b> - проверка успешного запроса POST /posts для создания поста с спецсимволами в поле body
9. <b>test_check_error_creation_post_with_empty_id</b> - проверка ошибки для запроса POST /posts с пустым вводом в поле userId
10. <b>test_check_error_creation_post_with_empty_title</b> - проверка ошибки для запроса POST /posts с пустым вводом в поле title
11. <b>test_check_error_creation_post_with_empty_body</b> - проверка ошибки для запроса POST /posts с пустым вводом в поле body
12. <b>test_check_error_creation_post_with_space_id</b> - проверка ошибки для запроса POST /posts с вводом пробелов в поле userId
13. <b>test_check_error_creation_post_with_space_title</b> - проверка ошибки для запроса POST /posts с вводом пробелов в поле title
14. <b>test_check_error_creation_post_with_space_body</b> - проверка ошибки для запроса POST /posts с вводом пробелов в поле body
15. <b>test_check_error_creation_post_with_letter_id</b> - проверка ошибки для запроса POST /posts с вводом букв в поле userId
16. <b>test_check_error_creation_post_with_spchar_id</b> - проверка ошибки для запроса POST /posts с вводом спецсимволов в поле userId
17. <b>test_check_delete_posts</b> - проверка ошибки для запроса DELETE /posts
18. <b>test_delete_posts_id</b> - проверка успешного запроса DELETE /posts с существующим Id для удаления поста с заданным id
19. <b>test_delete_posts_non_existent_id</b> - проверка ошибки для запроса DELETE /posts с несуществующим Id
