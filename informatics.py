import re

#паттерн для HH:MM or HH:MM:SS
pattern = re.compile(r'([0-1][0-9]:[0-5][0-9]:[0-5][0-9])|(2[0-3]:[0-5][0-9]:[0-5][0-9])|([0-1][0-9]:[0-5][0-9])|(2[0-3]:[0-5][0-9])')

#паттерн для двусложных слов
two_syllables_words = re.compile(r'\b(?:[BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz])*[AEIOUYaeiouy](?:[BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz])*[AEIOUYaeiouy](?:[BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz])*\b')

#паттерн для двух гласных подряд
two_vowels_both = re.compile(r'\b(?:\w)*[AEIOUYaeiouy]{2}(?:\w)*\b')

#паттерн для менее трех гласных
lower_three_vowels = re.compile(r'\b(?:[BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz])*[AEIOUYaeiouy](?:[BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz])*[AEIOUYaeiouy](?:[BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz])*\b|\b(?:[BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz])*[AEIOUYaeiouy](?:[BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz])*\b')

#паттерн для слова, где 2 гласные подряд, а потом слово с 1-2 слогами
task3 = re.compile(r'\b(?:\w)*[AEIOUYaeiouy]{2}(?:\w)*\b\b(?:[BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz])*[AEIOUYaeiouy](?:[BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz])*[AEIOUYaeiouy](?:[BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz])*\b|\b(?:\w)*[AEIOUYaeiouy][AEIOUYaeiouy](?:\w)*\b \b(?:[BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz])*[AEIOUYaeiouy](?:[BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz])*[AEIOUYaeiouy](?:[BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz])*\b|\b(?:\w)*[AEIOUYaeiouy][AEIOUYaeiouy](?:\w)*\b \b(?:[BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz])*[AEIOUYaeiouy](?:[BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz])*\b')

def for_hamlet(a: list) -> bool:
    if len(a) != 6:
        return False
    check_two_words = False
    for i in range(0, 6):
        temp = a[i]
        if re.fullmatch(two_syllables_words, temp) != None:
            if check_two_words == True:
                return False
            else:
                check_two_words = True
    if check_two_words == True:
        return True
    else:
        return False


#тесты к 1 заданию

# test1 = """
# Уважаемые студенты! В эту субботу 15:00 планируется доп. занятие на 2 часа.
# То есть в 17:00:01 оно уже точно кончится.
# """
# print(re.sub(pattern, r'(TBD)', test1))

# test2 = """
# Казалось бы ложишься в кровать в 15:11, собираешься вставать в 15:15
# и продолжать работать дальше, но что-то идет не по плану, и при подъеме часы
# показывают 17:21
# """
# print(re.sub(pattern, r'(TBD)', test2))

# test3 = """
# Занятие по физике у всех начинается в 10:00:00,
# а у меня в 11:40:00
# """
# print(re.sub(pattern, r'(TBD)', test3))

# test4 = """
# Ложиться спать правильно в 23:00:00, а не в 02:38:54, говорю
# я себе каждый день
# """
# print(re.sub(pattern, r'(TBD)', test4))

# test5 = """
# Если ты не придешь в 08:30, а придешь позже 08:40, то
# может быть бо-бо!
# """
# print(re.sub(pattern, r'(TBD)', test5))

f = open("test.txt", "r")

#для задания 2

search = re.findall(r'\w+|\.|[\f\n\r\t\v]', f.read())
j = 0
t = list()
while j < len(search):
    if re.fullmatch(r'[\n\f\v\t\r\.]', search[j]) == None:
        t.append(search[j])
        j+= 1
    else:
        res = for_hamlet(t)
        if res == True:
            print(t)
        t.clear()
        while re.fullmatch(r'[\n\f\v\t\r\.]', search[j]) != None:
            j+= 1
            if j == len(search):
                break

#для задания 3

# res = re.findall(task3, f.read())
# for i in range(0, len(res)):
#     whitespace = res[i].find(' ')
#     print(f"{i} - {res[i][0:whitespace]}")
#     if i > 99: 
#         break

f.close()
