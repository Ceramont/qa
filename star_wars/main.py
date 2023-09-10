import requests

dart_friends = []


class Star_request:

    """Метод записи листа в файл"""
    @staticmethod
    def dart_file_write(lines):
        with open("dart_friends.txt", "r+", newline='', encoding="utf-8") as file:
            file.writelines(line + "\n" for line in lines)

    """Метод для GET запроса и возвращения данных по фильтру"""
    @staticmethod
    def get_smth(url, star_filter):
        res = requests.get(url)
        print(res.json()['url'])
        return res.json()[star_filter]
    """Метод для получения персонажей"""
    def dart_cycle(self):
        url = "https://swapi.dev/api/people/4"
        """Поиск всех фильмов, в котором играл Дарт Вейдер"""
        for film in self.get_smth(url, "films"):
            """Поиск персонажей которые играли в данных фильмах"""
            for character in self.get_smth(film, "characters"):
                """Добавляем в лист имена персонажей"""
                dart_friends.append(self.get_smth(character, "name"))
        """Оставляем в массиве персонажей только уникальные имена"""
        dart_friends1 = list(set(dart_friends))
        dart_friends1.remove('Darth Vader')
        """Записываем лист уникальных значений в файл"""
        self.dart_file_write(dart_friends1)


vader = Star_request()
vader.dart_cycle()