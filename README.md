# Данный проект создан для поиска дубликатора действии пользователя.

---

## Стек:

* __Python__
* __Django__
* __Django Restframework__
* __Redis__
* __RabbitMQ__
* __Docker__
* __Postgres__

---

## Запуск проекта.

1. Клонирование проекта - git clone https://github.com/danpilnet/kion.git
2. Настройка переменных - copy example.env .env
3. Создаем виртуальное окружение python -m venv venv
4. Активируем виртуальное окружение venv/Scripts/activate
5. Устанавливаем зависимости из req.txt, команда pip install -r req.txt
6. Запускаем Docker, команда docker compose up --build