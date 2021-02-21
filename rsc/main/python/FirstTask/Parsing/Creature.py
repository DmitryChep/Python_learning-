class CreatFile:
    def __init__(self, creat):
        self.creat = creat

    def get_file(self):
        file = open('news111.txt', 'w', encoding='utf-8')
        i = 1
        for item in self.creat:
            file.write(
                f'Новость №{i}\n\n Название: {item["title"]}\n Описание: {item["desc"]}\n Ссылка: {item["href"]} \n\n'
                f'**********************************\n\n')
            i += 1

        file.close()
