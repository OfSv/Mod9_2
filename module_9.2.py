# "Списковые, словарные сборки"
#

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension',
                  'Java', 'Computer', 'Assembler']

# список созданный при помощи сборки состоящий из длин строк списка first_strings,
# при условии, что длина строк не менее 5 символов
first_result = [len(i) for i in first_strings if len(i) >= 5]

# список созданный при помощи сборки состоящий из пар слов(кортежей) одинаковой длины.
# Каждое слово из списка first_strings должно сравниваться с каждым из second_strings
second_result = [(first_strings[i], second_strings[j]) for i in range(len(first_strings))
                 for j in range(len(second_strings)) if len(first_strings[i]) == len(second_strings[j])]

# словарь созданный при помощи сборки, где парой ключ-значение будет строка-длина строки.
# Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings.
# Условие записи пары в словарь - чётная длина строки
third_result = {string: len(string) for string in (
    first_strings + second_strings) if len(string) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
