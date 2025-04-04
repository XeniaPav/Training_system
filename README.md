# Training system

### Логика работы системы
Проект представляет собой площадку для размещения онлайн-курсов с набором уроков.
Доступ к курсу предоставляется после его покупки (подписки). 
Внутри курса студенты автоматически распределяются по группам.

### Функционал
1. Просмотр списка продуктов и уроков.
2. Регистрация и авторизация пользователей.
3. Оформление подписки.
4. Распределение ученика в учебную группу.
5. Админка.

### Права доступа
1. К списку продуктов имеют доступ неавторизованные пользователи. 
2. Осуществить покупку продукта может только авторизованный пользователь.
3. Начисление баллов на баланс пользователя производится только через панель администратора. 

### Стек
Django
DRF
PostgreSQL

### Зависимости
Для управления зависимостями в проекте используется pip. 
Список зависимостей хранится в файле requirements.txt

### Установка и запуск
1. Установите Python и pip, если они не установлены.
2. Установите все зависимости командой pip install.
3. Создайте в корне проекта файл .env и внесите в него все переменные окружения.
4. Запустите миграции.
5. Создайте администратора с помощью команды `python manage.py csu`
6. Запустите проект.

#### Docker
Для создания контейнера в docker нужно набрать в консоли следующие команды:
`docker network create drf_net`
`docker run -d --network=drf_net --name=postgres_container -p 5432:5432 -e POSTGRES_DB=dockerDRF -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=12345 postgres:latest`
`docker-compose up -d --build`
