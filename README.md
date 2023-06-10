# QACloudCamp_test
## Тестовое задание для QACloudCamp

Набор тестов <i>test_functions.py</i> содержит набор тестов на <b>GET /posts</b>, <b>POST /posts</b>, <b>DELETE /posts</b>. Добавлен вариант <b>GET /posts/id</b> и <b>DELETE /posts/id</b> (в спецификациях для <i>https://jsonplaceholder.typicode.com/</i> отсутствует DELETE /posts).

Набор тестов <i>test_functions_if.py</i> содержит аналогичный набор тестов, однако предполагает что изменения действительно происходят на сервере и их можно проверить, поэтому в нем вылезают ошибки (ведь сервер имитирует изменения, а не производит их).

Список тестов:

1. <b>test_get_posts</b> - GET /posts

2. <b>test_get_posts_id</b> - GET /posts/id с существующим id

3. <b>test_get_posts_non_existent_id</b> - GET /posts/id с несуществующим id

4. <b>test_post_posts</b> - POST /posts 

5. <b>test_post_posts_empty_id</b> - POST /posts с пустым вводом в поле userId

6. <b>test_post_posts_empty_title</b> - POST /posts с пустым вводом в поле title

7. <b>test_post_posts_empty_body</b> - POST /posts с пустым вводом в поле body

8. <b>test_post_posts_space_id</b> - POST /posts с вводом пробелов в поле userId

9. <b>test_post_posts_space_title</b> - POST /posts с вводом пробелов в поле title

10. <b>test_post_posts_space_body</b> - POST /posts с вводом пробелов в поле body

11. <b>test_post_posts_letter_id</b> - POST /posts с вводом букв в поле userId

12. <b>test_post_posts_spchar_id</b> - POST /posts с вводом спецсимволов в поле userId

13. <b>test_delete_posts</b> - DELETE /posts

14. <b>test_delete_posts_id</b> - DELETE /posts с существующим Id

15. <b>test_delete_posts_non_existent_id</b> - DELETE /posts с несуществующим Id
