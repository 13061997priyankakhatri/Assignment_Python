'''
Write a Python script to sort (ascending and descending) a
dictionary by value.
'''

my_dict = {'apple': 30, 'banana': 10, 'orange': 20}

sorted_dict_asc = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}

sorted_dict_desc = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)}

print("Ascending:", sorted_dict_asc)

print("Descending:", sorted_dict_desc)

