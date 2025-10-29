import sqlite3

db = sqlite3.connect("turizm.db")
cursor = db.cursor()

# Удаление существующих таблиц (в обратном порядке создания)
cursor.executescript('''
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS tours;
DROP TABLE IF EXISTS services;
DROP TABLE IF EXISTS clients;
''')

# Создание таблиц-справочников
cursor.executescript('''
-- Таблица клиентов
CREATE TABLE IF NOT EXISTS clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    passport_number TEXT UNIQUE NOT NULL,
    phone_number TEXT NOT NULL
);

-- Таблица услуг
CREATE TABLE IF NOT EXISTS services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL
);

-- Таблица туров
CREATE TABLE IF NOT EXISTS tours (
    tour_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tour_name TEXT NOT NULL,
    country TEXT NOT NULL,
    duration_days INTEGER NOT NULL
);

-- Таблица сотрудников
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    position TEXT NOT NULL
);

-- Таблица заказов (основная таблица переменной информации)
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    tour_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    order_date DATE NOT NULL DEFAULT (CURRENT_DATE),
    total_amount DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (tour_id) REFERENCES tours(tour_id),
    FOREIGN KEY (service_id) REFERENCES services(service_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);
''')

# Тестовые данные
cursor.executescript('''
INSERT INTO clients (full_name, passport_number, phone_number) VALUES
    ('Иванов Иван Иванович', '1234567890', '+7-999-123-45-67'),
    ('Петрова Анна Сергеевна', '0987654321', '+7-917-555-44-33');

INSERT INTO services (service_name, description, price) VALUES
    ('Проживание', 'Проживание в отеле 4*', 5000.00),
    ('Экскурсия', 'Обзорная экскурсия по городу', 1500.00),
    ('Страховка', 'Медицинская страховка на время тура', 1000.00);

INSERT INTO tours (tour_name, country, duration_days) VALUES
    ('Золотое кольцо', 'Россия', 7),
    ('Отдых в Сочи', 'Россия', 10),
    ('Горнолыжный курорт', 'Абхазия', 14);

INSERT INTO employees (full_name, position) VALUES
    ('Сидорова Ольга Петровна', 'Менеджер по туризму'),
    ('Васильев Дмитрий Николаевич', 'Агент по продажам');

INSERT INTO orders (client_id, tour_id, service_id, employee_id, total_amount)
VALUES
    (1, 1, 1, 1, 6500.00),
    (2, 3, 3, 2, 2500.00);
''')

# Проверка содержимого таблиц
print("Клиенты:")
for row in cursor.execute("SELECT * FROM clients"):
    print(row)

print("\nУслуги:")
for row in cursor.execute("SELECT * FROM services"):
    print(row)

print("\nТуры:")
for row in cursor.execute("SELECT * FROM tours"):
    print(row)

print("\nСотрудники:")
for row in cursor.execute("SELECT * FROM employees"):
    print(row)

print("\nЗаказы:")
for row in cursor.execute("SELECT * FROM orders"):
    print(row)

db.commit()
db.close()
