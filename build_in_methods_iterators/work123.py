
data = [

    {'age': 49, 'name': 0},
    {'age': 37, 'name': None},
    {'sxx': 55, "ololo": "nax"},
    {'ssx': 83, 'name': 'hOmer'}
]


redundant_keys = ['age', 'nax']

# for info in data:
#     for point in redundant_keys:
#         if point in info:
#             del (info[point])


# data = [({k: v for k,v in info.items() if k not in redundant_keys}) for info in data]
# #

data = [({k: v for k, v in info.items() if k in redundant_keys}) for info in data]



print(data)
