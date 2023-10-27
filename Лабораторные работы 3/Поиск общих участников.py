# TODO Напишите функцию find_common_participants
def find_common_participants(a: str, b: str, r: str = ',') -> list:
    a_list = a.split(r)
    b_list = b.split(r)
    return sorted(list(set(a_list).intersection(set(b_list))))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))