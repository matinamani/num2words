UNITS = ["", "یک", "دو", "سه", "چهار", "پنج", "شش", "هفت", "هشت", "نه"]
EXCEPTIONS = [
    "",
    "یازده",
    "دوازده",
    "سیزده",
    "چهارده",
    "پانزده",
    "شانزده",
    "هفده",
    "هجده",
    "نوزده",
]
TENS = [
    "",
    "ده",
    "بیست",
    "سی",
    "چهل",
    "پنجاه",
    "شصت",
    "هفتاد",
    "هشتاد",
    "نود",
]
HUNDREDS = [
    "",
    "صد",
    "دویست",
    "سیصد",
    "چهارصد",
    "پانصد",
    "ششصد",
    "هفتصد",
    "هشتصد",
    "نهصد",
]
SCALES = [
    "",
    "هزار",
    "میلیون",
    "میلیارد",
    "تریلیون",
    "کوادریلیون",
    "کوینتیلیون",
    "سکستیلیون",
    "سپتیلیون",
    "اکتیلیون",
    "نونیلیون",
    "دسیلیون",
    "آندسیلیون",
    "دودسیلیون",
    "تریدسیلیون",
    "کواتردسیلیون",
    "کویندسیلیون",
    "سیکسدسیلیون",
    "سپتمدسیلیون",
    "اکتودسیلیون",
    "نوندسیلیون",
]


def has_exception(num):
    num %= 100
    return num >= 11 and num <= 19


def num_to_digits(num):
    digits = []
    while num > 0:
        digits.append(num % 1000)
        num //= 1000

    return digits


def num_to_word(num):
    if num == 0:
        return "صفر"

    result = ""
    digits = num_to_digits(num)

    for i in range(len(digits)):
        if digits[i] == 0:
            continue

        partial = ""

        hundreds_digit = digits[i] // 100
        tens_digit = (digits[i] % 100) // 10
        units_digit = (digits[i] % 10) // 1

        if has_exception(digits[i]):
            partial += HUNDREDS[hundreds_digit] + (
                f" و {EXCEPTIONS[digits[i] % 10]}"
                if hundreds_digit != 0
                else EXCEPTIONS[digits[i] % 10]
            )
        else:
            partial += (
                HUNDREDS[hundreds_digit]
                + (
                    f" و {TENS[tens_digit]}"
                    if hundreds_digit != 0 and tens_digit != 0
                    else TENS[tens_digit]
                )
                + (
                    f" و {UNITS[units_digit]}"
                    if (hundreds_digit != 0 and units_digit != 0)
                    or (tens_digit != 0 and units_digit != 0)
                    else UNITS[units_digit]
                )
            )

        scale = SCALES[i]
        if scale != "":
            partial += " " + scale

        result = partial if result == "" else partial + " و " + result

    return result


number = int(input("Enter a number: "))

print(num_to_word(number))
