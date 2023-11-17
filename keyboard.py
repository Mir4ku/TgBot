from telebot import types

article = types.InlineKeyboardMarkup()
url_button = types.InlineKeyboardButton(text="Читать статью", url="https://teletype.in/@mariiabramova/5_oshibok_expertov")
article.add(url_button)

select = types.InlineKeyboardMarkup()
url_button = types.InlineKeyboardButton(text="Принять участие", url="https://sblnk.ru/317100762")
select.add(url_button)

buy = types.InlineKeyboardMarkup()
url_button = types.InlineKeyboardButton(text="Оплатить воркшоп", url="https://sblnk.ru/317106840")
buy.add(url_button)