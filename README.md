Небольшое пояснение к проекту.
Окружение запаковано в docker-образ. Для хранения гео-данных (координаты точек) используется PostGIS. Для работы c PostGIS в контейнер устанавливается из исходников несколько нужных библиотек, поэтому образ разворачивается довольно долго (~30мин.)

Создать контейнер:
docker-compose up

Провести миграцию:
docker-compose exec web ./manage.py migrate

Создать администратора, если нужно.
Прошу обратить внимание, что в качестве логина используется email.
docker-compose exec web ./manage.py createsuperuser

Для удобсва добавил команду, создающую немного тестовых данных:
docker-compose exec web ./manage.py add_initial_data

Тесты:
docker-compose exec web ./manage.py test userdata
