import re


# TODO: исправить класс чтобы он мог брать данные не только из файлов, но и из списков
# TODO: дописать еще один класс спамера сообщений на почту
# TODO: создать класс который будет работать с вотсапом

class Separator:
    """
    Класс для изъятия личных данных из обьектов
    """

    def get_email(self, path):
        """
        Возвращает из файла emails в output.txt
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
        # print("Количество строк = ", s)

        with open('output.txt', 'a') as file:
            for index in lister:
                file.write(index + '\n')
        return s

    def get_phone(self, path):
        pass


if __name__ != '__main__':
    pass
else:
    # Example
    # name_var = Separator()
    var = Separator
    var.get_email('ooo.txt')
