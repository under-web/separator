import re


# TODO: исправить класс чтобы он мог брать данные не только из файлов, но и из списков
# TODO: дописать еще один класс спамера сообщений на почту
# TODO: создать класс который будет работать с вотсапом

class Separator:
    """
    Класс для изъятия личных данных из обьектов
    """

    def get_email_file(self, path):
        """
        Возвращает из файла emails в output.txt
        :param path: путь к файлу в котором искать email
        :return: количество строк
        """

        with open(path, 'r', encoding='utf-8', errors='ignore') as file:
            s = 0
            for lin in file:
                pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+')  # создали шаблон
                result = pattern.findall(lin)  # указываем что ищем и где ищем
                with open('output_mail.txt', 'a') as file_out:
                    file_out.write(''.join(result) + '\n')
                    s += 1
            return s

    def get_phone_file(self, path, regex=r'\d{11,12}'):
        with open(path, 'r', encoding='utf-8', errors='ignore') as file:
            s = 0
            for lin in file:
                print(lin)
                pattern = re.compile(regex)  # создали шаблон
                result = pattern.findall(lin)  # указываем что ищем и где ищем
                if not result:
                    continue
                else:
                    with open('output_phone.txt', 'a') as file_out:
                        file_out.write(''.join(result) + '\n')
                        s += 1
            return s


if __name__ == '__main__':
    # Example
    # name_var = Separator()
    var = Separator()
    var.get_phone_file('/home/appdev/Рабочий стол/Текущая/Базы/VK_100M.txt')
