from datetime import datetime
import os

def logoutput(string: str) -> None:
    # Получите текущее время в формате YYYY-MM-DD
    current_date = datetime.now().strftime('%Y-%m-%d')

    # Проверьте, есть ли файл с таким именем
    if os.path.exists(current_date + '.txt'):
        # Если файл существует, откройте его
        file = open(current_date + '.txt', 'a')
    else:
        # Если файла нет, создайте новый
        file = open(current_date + '.txt', 'w')

    # Работа с файлом
    file.write('\n' + string + '\n')
    file.close()

    return string