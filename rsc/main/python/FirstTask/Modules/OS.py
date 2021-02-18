import os

# for roots, dirs, files in os.walk(r'C:\Users\User\PycharmProjects\pythonProject\rsc\main\python\FirstTask\FolderTree'):
#     print(f'Path: {roots} \n'
#           f'Packages: {dirs}\n'
#           f'Files: {files} \n\n')

# tree = os.walk(r'C:\Users\User\PycharmProjects\pythonProject\rsc\main\python\FirstTask\FolderTree')
# for i in tree:
#     print(i)


def read_folder(folder):
    for roots, dirs, files in os.walk(folder):
        level = roots.count(os.sep)
        intent = ' ' * 4 * level
        print(f'{intent}[{os.path.basename(roots)}]')
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            print(f'{sub_indent}{file}')




read_folder(r'C:\Users\User\PycharmProjects\pythonProject\rsc\main\python\FirstTask\FolderTree')







