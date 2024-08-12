import os
import time
if os.path.exists('Module_7_5'):
    os.chdir('Module_7_5')
else:
    os.mkdir('Module_7_5')
    os.chdir('Module_7_5')
directory = os.getcwd()
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(directory, file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(directory)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, '
              f'Размер: {filesize} байт, Время изменения: {formatted_time},'
              f' Родительская директория: {parent_dir}')


