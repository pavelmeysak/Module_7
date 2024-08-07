def custom_write(file_name, strings: list):
    file = open(file_name, 'w')
    file.close()
    file = open(file_name, 'a', encoding='utf-8')
    strings_positions: dict = {}
    for i in range(0, len(strings)):
        strings_positions.update({(i+1, file.tell()): strings[i]})
        file.write(f'{strings[i]}\n')
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
