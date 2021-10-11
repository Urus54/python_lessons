# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

from random import choice, randrange

def some_jokes(n, repeat=False):
    """
           Возвращает n шуток, сформированных из трех случайных слов,
           взятых из трёх списков (по одному из каждого).

           :n - колличество шуток

    """

    nouns_copy, adverbs_copy, adjectives_copy= nouns.copy(), adverbs.copy(),adjectives.copy()
    joke_list = []
    l_min = min(nouns_copy,adverbs_copy,adjectives_copy)

    while n and len(l_min):
        num = randrange(len(l_min))
        if repeat:
            joke_list.append(f"{nouns_copy.pop(num)} {adverbs_copy.pop(num)} {adjectives_copy.pop(num)}")
        else:
            joke_list.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        n -= 1
    return joke_list

print(some_jokes(200,True))