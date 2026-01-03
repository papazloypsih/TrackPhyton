# TODO Напишите функцию find_common_participants
def find_common_participants(first_group_str, second_group_str, separator=","):
    common_set = set(first_group_str.split(separator)) & set(second_group_str.split(separator))
    return sorted(list(common_set))
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group)
print(f"Общие участники (разделитель-запятая): {common_participants}")
# TODO Провеьте работу функции с разделителем отличным от запятой
participants_first_group = "Иванов Петров Сидоров"
participants_second_group = "Петров Сидоров Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group, separator=" ")
print(f"Общие участники (разделитель-пробел): {common_participants}")
