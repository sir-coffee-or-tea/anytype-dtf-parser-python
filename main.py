import functions as func

print('Добро пожаловать в программу для парсинга статей из DTF, в Anytype.\n 1 - Перенос статьи на Anytype \n 2 - Проверка x и y мыши')
command = input()
if command == '1':
    func.start()
elif command == '2':
    func.output_mouse_coordinates()
