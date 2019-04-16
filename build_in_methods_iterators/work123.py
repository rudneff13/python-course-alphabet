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

a = list(range(10))
print(a)

new_list = []
i = 1
for i in a:

    if a[i] % i == 0:
        new_list.append(i)
        i += 1
print(new_list)