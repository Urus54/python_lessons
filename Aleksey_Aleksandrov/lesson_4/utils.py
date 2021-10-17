from requests import get, utils



def currency_rates(code):

    """
    Функция запрашивает данные о курсе валюты с сайта http://www.cbr.ru
    и выводит текущий курс. Если данные отсутствуют, выдает "None".

    """
    source = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))
    information = source.split("<Valute ID=")
    for i in information:
        if code.upper() in i:
            print(code.upper(), end=" ")
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))

if __name__ == "__main__":
    print(currency_rates("UsD"))
    print(currency_rates("EuR"))
    print(currency_rates("JPY"))