from datetime import datetime, timedelta
import locale

import top as top

# today = datetime.today()
# print(today)
# print(today.year)
# print(today.month)
# print(today.day)
# print(today.weekday())

# days = ['Monday', ' Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#
# locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
#
# print(today.strftime('%a'))
# print(today.strftime("%B"))
#
# print(f'Дата: {today.strftime("%a. " "%d. " "%B " "%Y г.")} ')
# print(f'Время: {today.strftime("%H:" "%M:" "%S:")} ')
# print(today.strftime('%X'))
# d = today + timedelta(days=1, hours=4, minutes=34)
# print(today.strftime('%c'))
# print(d.strftime('%c'))

# Task 1

import os

for roots, dirs, files in os.walk(r'C:\Users\User\PycharmProjects\pythonProject\rsc\main\python\FirstTask\FolderTree'):
    print(f'Path: {roots} \n'
          f'Packages: {dirs}\n'
          f'Files: {files} \n\n')

print()