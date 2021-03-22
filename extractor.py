import re


class Separator:
    """
    Класс для парсинга личных данных из текстов и файлов
    """
    def get_email(self, path):
        """
        Возвращает из файла emails
        :param path: путь к файлу в котором искать email
        :return: количество строк
        """
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()  # указываем размер считывания из файла
            pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+')  # создали шаблон
            result = pattern.findall(text)  # указываем что ищем и где ищем
            lister = []  # пустой список
            s = 0  # счетчик
            for i in result:
                lister.append(i)
                s += 1
        print("Количество строк = ", s)

        with open('output.txt', 'a') as file:
            for index in lister:
                file.write(index + '\n')
        return s


# Example
var = Separator()

var.get_email('ooo.txt')
