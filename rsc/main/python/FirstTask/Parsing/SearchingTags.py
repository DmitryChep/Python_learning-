class Tags:
    def __init__(self, tags):
        self.tags = tags

    @property
    def get_tags(self):
        results = []
        for item in self.tags:
            title = item.find('span', class_='heading').get_text(strip=True)
            desc = item.find('span', class_='name-dop').get_text(strip=True)
            href = item.a.get('href')
            results.append({'title': title,
                            'desc': desc,
                            'href': href,
                            })
            continue
        return results
