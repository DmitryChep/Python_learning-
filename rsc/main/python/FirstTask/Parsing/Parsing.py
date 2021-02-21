from GetHTML import SearchHTML
from SearchingTags import Tags
from Creature import CreatFile

search_html = SearchHTML('https://www.ua-football.com')

tags = Tags(search_html.get_URL)

creat_file = CreatFile(tags.get_tags)
creat_file.get_file()


