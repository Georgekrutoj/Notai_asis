def fileopen():
    write = input('Введите запись: ')
    try:
        with open('text.txt', 'w+') as f:
            f.write(write)
            f.seek(0)
            print(f.read())
    except FileNotFoundError:
        print("Файл не найден")
    except Exception as e:
        print("Произошла ошибка при записи в файл: ", e)