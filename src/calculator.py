import re

pattern = re.compile(r'\/\/(.+)\\n(.+)')

def Add(numbers):
    if len(numbers) == 0:
        return 0 
    if numbers[0:2] == '//':
        for match in pattern.finditer(numbers):
            re_delimiter = match.group(1)
            re_numbers = match.group(2)
            return re_delimiter, re_numbers
    number_list= numbers.replace("\n", ",").split(',')
    int_list = [int(num) for num in number_list]
   
    return sum(int_list)