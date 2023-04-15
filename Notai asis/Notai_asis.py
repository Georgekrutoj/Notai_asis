import main, currency, fileopen, help, url_search, games

main.registration()
help.help()

while True:
    task = input('Ввод: ').capitalize()
    if task == 'Игра угадай число':
        games.random_number_game()
    elif task == 'Запиши в блокнот':
        fileopen.fileopen()
    elif task == 'Конвертировать в рубль':
        currency.convert_currency()
    elif task == 'help':
        help.help()
    elif task == 'Игра города':
        games.goroda()
    elif task == 'Поиск url':
        url_search.search_with_url()
    elif task == 'Тест на реакцию':
        games.reakcia_test()