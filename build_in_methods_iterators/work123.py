# <<<<<<< HEAD
# def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
#     """
#     Return generator of simple numbers
#     Stop then iteration if returned value is more than 200
#     Examples:
#         a = task_10_generator_of_simple_numbers()
#         next(a)
#         >>> 2
#         next(a)
#         >>> 3
#     """
#     pass

# a = list(range(10))
# print(a)
#
# new_list = []
# i = 1
# for i in a:
#
#     if a[i] % i == 0:
#         new_list.append(i)
#         i += 1
# print(new_list)
# =======
# def task_1_fix_names_start_letter(data: DT) -> DT:
#     """
#     Make all `names` field in list of students to start from upper letter
#
#     Examples:
#         fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
#         >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
#     """
#     for info in data:
#         info['name'] = info['name'].capitalize()
#     return data

data = [
    {'age': 49, 'name': 'Roman'},
    {'age': 36, 'name': 'Godzilla'},
    {'age': 47, 'name': 'spike'},
    {'age': 31, 'name': 'SuperMan'},
    {'age': 49, 'name': 'Batman'},
    {'age': 37, 'name': 'cLaus'},
    {'age': 55, 'name': 'Frank'},
    {'age': 83, 'name': 'hOmer'}
]

data = [item for item in data]

print(data)
print(item)

