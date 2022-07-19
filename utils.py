import json


def json_load() -> list[dict]:
    """
    Загружает cписок словарей из файла candidates.json
    :return: список json
    """
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_candidates_by_id(uid: int) -> dict:
    """
    Получает словарь с данными кандидата по ключу id.
    :param uid: значение ключа "id"
    :return: словарь с данными кандидата, или None если такого кандидата нет
    """

    for candidate in json_load():
        if candidate['id'] == uid:
            return candidate


def get_candidates_by_name(name: str) -> list[dict]:
    """
    Возвращает словарь с данными кандидата по ключу name.
    :param name: значение ключа "name"
    :return: Список с данными кандидата
    """
    return [candidate for candidate in json_load() if name in candidate['name'].lower()]


def get_candidate_by_skill(skill: str) -> list[dict]:
    """
    Возвращает словарь с данными кандидата по ключу skills
    :param skill: значение ключа "skills"
    :return: Список с данными кандидата
    """
    return [candidate for candidate in json_load() if skill in candidate['skills'].lower()]
###############################################################################################
