# Мини Книжный Магазин

## Описание проекта
Это проект, реализующий мини книжный магазин. В нем работает система администрации и пользователей, а также имеется личный кабинет пользователя с функциями логина и выхода. Если пользователь имеет статус администратора, он может добавлять категории книг и книги. В данном проекте также работает корзина, в которую пользователь может добавлять книги в разных количествах. Однако вкладка доставки пока не реализована.

## Запуск проекта
Чтобы запустить проект, выполните следующие шаги:

1. **Клонировать репозиторий:**
  ```
   git clone https://github.com/Anoglick/Mini-BookStore.git
  ```
Перейти в директорию проекта:

2. **Копировать код**
  ```
  cd Mini-BookStore
  ```
3. **Создать виртуальное окружение**:
```
python -m venv venv
```
4. Активировать виртуальное окружение:
  - Для Windows:
  ```
    venv\Scripts\activate
  ```
  - Для macOS и Linux:
  ```
    source venv/bin/activate
  ```
5. Установить зависимости:
  ```
  pip install -r requirements.txt
  ```
6. Запустить миграции:
  ```
  python manage.py migrate
  ```
7. Запустить сервер:
  ```
  python manage.py runserver
  ```
8. Теперь вы можете открыть ваш браузер и перейти по адресу http://127.0.0.1:8000, чтобы увидеть ваш проект в действии!

# Mini Book Store

### Project Description
This is a project implementing a mini book store. It features an administration and user system, as well as a user cabinet with login and logout functionalities. If a user has an administrator status, they can add book categories and books. The project also includes a shopping cart where users can add books in various quantities. However, the delivery tab is not yet implemented.

## Running the Project
To run the project, follow these steps:

1. Clone the repository:
  ```
  git clone <repository-URL>
  ```
2. Navigate to the project directory:
  ```
  cd <project_folder_name>
  ```
3. Create a virtual environment:
  ```
  python -m venv venv
  ```
4. Activate the virtual environment:
  - For Windows:
  ```
  venv\Scripts\activate
  ```
  - For macOS and Linux:
  ```
    source venv/bin/activate
  ```
6. Install dependencies:
  ```
  pip install -r requirements.txt
  ```
7. Run migrations:
  ```
  python manage.py migrate
  ```
8. Start the server:
  ```
  python manage.py runserver
  ```
Now you can open your browser and go to http://127.0.0.1:8000 to see your project in action!





