'''
1. Cоздать модуль test_filemanager.py для тестирования функций консольного файлового менеджера
2. В файле написать тесты для каждой ""чистой"" функции, чем больше тем лучше.
 Это могут быть функции консольного файлового менеджера, а так же программы мой счет и программы викторина
'''
import os
import random
import shutil


def test_random_sample():  #проверка, что случайные знаменистости выбираются из списка
    date_birth_selebrity = {'Л.Н.Толстой': '09.09.1928', 'Ф.М.Достоевкий': '11.11.1821', 'М.Ю.Лермонтов': '15.10.1814',
                            'А.А. Ахматова': '23.06.1889', 'Н.Г. Гумилев': '15.04.1886', 'Ф.И. Ленин': '22.04.1870',
                            'А.А. Тарковский': '04.09.1932', 'П.И. Чайковский': '07.05.1840',
                            'Ю.А. Гагарин': '09.03.1934',
                            'Долорес О Риордан': '06.09.1971'}
    for selebrity in random.sample(list(date_birth_selebrity.keys()), 5):
        assert selebrity in list(date_birth_selebrity.keys()), 'test sample error'
def test_os_copy(): #проверяем существует ли скопированная папка
    if not os.path.exists('hello.txt'):
        text_file = open('hello.txt', 'w')
    if not os.path.exists('name_dir2'):
        os.mkdir('name_dir2')
    shutil.copy('hello.txt', 'name_dir2')
    assert 'hello.txt' in os.listdir('name_dir2'), 'test copy error'

