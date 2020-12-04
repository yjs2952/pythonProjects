import re

input_array = ["3285-3764-9934-2453", "3285376499342453", "3285-3764-99342453", "328537649934245", "3285376499342459", "3285-3764-9934-2452"]
input_array2 = ["0000-1111-3333-9999", "000011113333999", "-0000-1111-3333-9999-", "9999111122225555", "1534758621345678", "1111222233334444", "1111--2222--3333-4444"]


def solution(card_numbers):
    answer = []
    for card_number in card_numbers:
        if not is_valid_format(card_number):
            answer.append(0)
            continue

        card_number = card_number.replace('-', '')

        if is_validated_by_luhn_formula(card_number):
            answer.append(1)
        else:
            answer.append(0)
    return answer


def is_valid_format(card_number):
    if card_number.find('-') >= 0:
        return re.search('^\d{4}-\d{4}-\d{4}-\d{4}$', card_number)
    else:
        return len(card_number) == 16


def is_validated_by_luhn_formula(card_number):
    luhn_number = 0
    for i in reversed(range(0, len(card_number))):
        if i % 2 == 0:
            temp = int(card_number[i]) * 2

            if temp >= 10:
                temp = sum(map(int, str(temp)))
            luhn_number += temp
        else:
            luhn_number += int(card_number[i])
    return luhn_number % 10 == 0


print(solution(input_array2))
