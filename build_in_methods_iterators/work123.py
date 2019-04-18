
data = [

    {'age': 49, 'name': 0},
    {'age': 37, 'name': None},
    {'age': 55, "ololo": 123},
    {'age': 83, 'name': 'hOmer'}
]


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    # try:
    #     for point in redundant_keys:
    #         for info in data:
    #             del (info[point])
    # except KeyError:
    #     pass
    # return data


    # [info.update({'name': info.get('name').title() if type(info.get('name')) == str else info.get('name')})
    #  for info in data]
    # return data
redundant_keys = ['age']

[info.update({key(): value.get() if key, value in redundant_keys else key, value}) for info in data]