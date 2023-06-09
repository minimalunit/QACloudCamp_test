# QACloudCamp_test
## Тестовое задание для QACloudCamp

Набор тестов <i>test_functions.py</i> содержит набор тестов на <b>GET /posts</b>, <b>POST /posts</b>, <b>DELETE /posts</b>. Добавлен вариант <b>GET /posts/id</b> и <b>DELETE /posts/id</b> (в спецификациях для <i>https://jsonplaceholder.typicode.com/</i> отсутствует DELETE /posts).

Набор тестов <i>test_functions_if.py</i> содержит аналогичный набор тестов, однако предполагает что изменения действительно происходят на сервере и их можно проверить, поэтому в нем вылезают ошибки (ведь сервер имитирует изменения, а не производит их).
