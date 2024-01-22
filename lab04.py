def main():
    number = int(input("Введите сумму от 1 до 100000: "))
    print(convert_to_words(number) + " " + add_rubles_ending(number))

def convert_to_words(number):
    if number == 0:
        return "Ноль"
    ones = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять",
            "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
    words = ""
    if number // 1000 > 0:
        words += hundreds[number // 1000 // 100] + " " if number // 1000 // 100 > 0 else ""
        words += tens[number // 1000 % 100 // 10] + " " if number // 1000 % 100 // 10 > 1 else ""
        words += ones[number // 1000 % 100] + " " if number // 1000 % 100 < 20 else ""
        words += "тысяч "
    words += hundreds[number // 100 % 10] + " " if number // 100 % 10 > 0 else ""
    words += tens[number // 10 % 10] + " " if number // 10 % 10 > 1 else ""
    words += ones[number % 10] if number % 10 < 10 or number % 100 >= 20 else ones[number % 100]
    return words.strip().capitalize()

def add_rubles_ending(number):
    if number % 100 in [11, 12, 13, 14]:
        return "рублей"
    if number % 10 == 1:
        return "рубль"
    if number % 10 in [2, 3, 4]:
        return "рубля"
    return "рублей"

if __name__ == "__main__":
    main()