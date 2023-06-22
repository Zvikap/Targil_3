# import datetime
# print(datetime.datetime.now())
#
# import requests
# response = requests.get("https://githun.com")
# if response. == 200:
#     print('OK')

def print_names():
    names_file = open('names.txt')
    for line in names_file.readlines():
        print(line, end='')

def save_name(name):
    names_file = open('names.txt', 'a')
    names_file.write(f'\n{name}')
    names_file.close()


save_name('doron')
save_name('yuval')
save_name('sharon')
print_names()