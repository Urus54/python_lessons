# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена,
# начинающиеся с соответствующей буквы. Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"],
#     "П": ["Петр"]
# }
#
#
# Подумайте: полезен ли будет вам оператор распаковки?
# Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?




def thesaurus(*args):
    """
        Функция принимает в качестве аргумента имена сотрудников и возвращает словарь,
        в котором ключи — первые буквы имён, а значения — списки, содержащие имена,
        начинающиеся с соответствующей буквы.
        Например:
        :>>> thesaurus("Иван", "Мария", "Петр", "Илья")
    {
     "И": ["Иван", "Илья"],
     "М": ["Мария"],
     "П": ["Петр"]
    }
    """
    dict_names = {}
    args = sorted(args)
    for i in (args):
        n = i[0]
        if n in dict_names:
            dict_names[n] += [i]
        else:
            dict_names[n] = [i]
    print(dict_names)


thesaurus("Иван", "Мария", "Петр", "Илья","Алексей","Яна")