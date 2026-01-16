def text_analyzer():
    """
    Анализ введённого текста: символы, слова, предложения, 
    самое длинное слово, проценты заглавных/строчных букв и количество цифр.
    """
    import re

    text = input("Введите текст: ").strip()
    if not text:
        print("Пустой ввод — анализировать нечего.")
        return

    # Подсчёт символов
    symbols = len(text)

    # Слова (учитываем русские и латинские буквы, цифры в словах)
    words = re.findall(r"\b[\wЁёА-Яа-я'-]+\b", text)
    word_count = len(words)

    # Предложения
    sentences = re.findall(r"[.!?]+", text)
    sentence_count = len(sentences)

    # Самое длинное слово
    longest_word = max(words, key=len) if words else ""
    longest_len = len(longest_word)

    # Буквы
    letters = [ch for ch in text if ch.isalpha()]
    upper_count = sum(ch.isupper() for ch in letters)
    lower_count = sum(ch.islower() for ch in letters)
    total_letters = len(letters) or 1  # чтобы не делить на ноль

    # Цифры
    digit_count = sum(ch.isdigit() for ch in text)

    # Вывод
    print(f"Символов: {symbols}, Слов: {word_count}, Предложений: {sentence_count}")
    if longest_word:
        print(f"Самое длинное слово: '{longest_word}' ({longest_len} символов)")
    print(f"Заглавные: {upper_count/total_letters*100:.1f}%")
    print(f"Строчные: {lower_count/total_letters*100:.1f}%")
    print(f"Цифр в тексте: {digit_count}")


text_analyzer()
