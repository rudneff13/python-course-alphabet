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

    {'age': 49, 'name': 'batman'},
    {'age': 37, 'name': 'cLaus'},
    {'age': 55, 'name': 'Frank'},
    {'age': 83, 'name': 'hOmer'}
]

data = [{k: v.title() if k == 'name' else v for k, v in info.items()} for info in data]


print(data)
