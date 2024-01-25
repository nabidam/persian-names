def clean_arabic_chars(word):
    arabic_chars_map = {
        "ي": "ی",
        "ك": "ک",
        # '٠': '۰',
        # '١': '۱',
        # '٢': '۲',
        # '٣': '۳',
        # '٤': '۴',
        # '٥': '۵',
        # '٦': '۶',
        # '٧': '۷',
        # '٨': '۸',
        # '٩': '۹',
    }

    for arabic_char, persian_char in arabic_chars_map.items():
        word = word.replace(arabic_char, persian_char)

    return word


def clean_irabs(word):
    irabs = "ًٌٍَُِّْٰ"

    word.replace(irabs, "")

    return word
