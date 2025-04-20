API_INSTANCE = "https://api.imgflip.com"

MEME_DATA = {
    "text": "тестовый мем",
    "url": "https://www.meme-arsenal.com/memes/3f2a7b338fcd49f8d1d03b3f2a4bb7f2.jpg",
    "tags": ["тест", "мем"],
    "info": {"colors": ["красный", "синий"]}
}

UPDATED_MEME_DATA = {
    "id": None,  # Будет установлено в тесте
    "text": "обновленный текст мема",
    "url": "https://www.meme-arsenal.com/memes/3f2a7b338fcd49f8d1d03b3f2a4bb7f2.jpg",
    "tags": ["новый", "тег"],
    "info": {"colors": ["новый цвет", "другой цвет"]}
}

INVALID_MEME_DATA = {
    "text": "",  # Пустой текст
    "url": "invalid_url",  # Невалидный URL
    "tags": "not_a_list",  # Теги не являются списком
    "info": "not_a_dict"  # Информация не является словарем
}
