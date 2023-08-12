import sqlite3

connect = sqlite3.connect('cars.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS cars(
    id INTEGER PRIMARY KEY,
    number TEXT,
    mark TEXT,
    model TEXT,
    release_year INTEGER,
    work_description TEXT,
    status TEXT
    )''')


def add_cars(number, mark, model, release_year, work_description, status):
    cursor.execute('''
    INSERT INTO cars(number, mark, model, release_year, work_description, status) VALUES (?,?,?,?,?,?)''', (number, mark, model, release_year, work_description, status))
    connect.commit()


def update_cars(id, mark, model, release_year, work_description, status):
    cursor.execute('''
        UPDATE cars
        SET mark = ?, model = ?, release_year = ?, work_description = ?, status = ?
        WHERE id = ?''',(mark, model, release_year, work_description, status, id))
    connect.commit()
    
def service_cars():
    cursor.execute('SELECT * FROM cars WHERE status = "In Service"')
    cars = cursor.fetchall()
    return cars


def ready_cars():
    cursor.execute('SELECT * FROM cars WHERE status = "Ready"')
    cars = cursor.fetchall()
    return cars


while True:
    print('1.Добавление новых автомобилей на обслуживание')
    print('2.Обновление информации о марке, модели, годе выпуска, описании работ и статусе обслуживания автомобиля')
    print('3.Просмотр списка всех автомобилей на обслуживании')
    print('4.Просмотр списка автомобилей, которые уже обслужены и готовы к выдаче.')
    print('5.Выход')

    choice = int(input("Выберите действие:"))
    
    try:
        if choice == 1:
            number = input("Введите номер автомобиля: ")
            mark = input("Введите марку автомобиля: ")
            model = input("Введите модель автомобиля: ")
            release_year = int(input("Введите год выпуска: "))
            work_description = input("Введите описание работ: ")
            status = 'In Service'
            add_cars(number, mark, model, release_year, work_description, status)
            print("Автомобиль добавлен на обслуживание")

        elif choice == 2:
            id = int(input("Введите ID автомобиля для обновления: "))
            mark = input("Введите новую марку автомобиля: ")
            model = input("Введите новую модель автомобиля: ")
            release_year = int(input("Введите новый год выпуска: "))
            work_description = input("Введите новое описание работ: ")
            status = input("Введите новый статус (In Service/Ready): ")
            update_cars(id, mark, model, release_year, work_description, status)
            print("Информация об автомобиле обновлена")

        elif choice == 3:
            cars = service_cars()
            print("\nАвтомобил на обслуживании:")
            for car in cars:
                print(car)

        elif choice == 4:
            cars = ready_cars()
            print("\nГотовые автомобили:")
            for car in cars:
                print(car)

        elif choice == 5:
            break

        else:
            print("ошибка")

    except ValueError:
        print("Ошибка: Некорректный ввод числа. Пожалуйста, повторите попытку.")

connect.close()