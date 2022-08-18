import re

pattern = "\/\/(.+)\\n(.+)"


def Add(numbers):
    if len(numbers) == 0:
        return 0
    if numbers[0:2] == "//":
        matches = re.finditer(pattern, numbers)
        for match in matches:
            for index in range(0, match.lastindex + 1):
                delimiter = match.group(1)
                items = match.group(2)

        print(delimiter, items)
        number_list = items.split(delimiter)
        int_list = [int(num) for num in number_list]
        for number in int_list:
            if number < 0:
                raise Exception("negatives not allowed")

        return sum(int_list)

    number_list = numbers.replace("\n", ",").split(",")
    int_list = [int(num) for num in number_list]
    for number in int_list:
        if number < 0:
            raise Exception("negatives not allowed")

    return sum(int_list)
