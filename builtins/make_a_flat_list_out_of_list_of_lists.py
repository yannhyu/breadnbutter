# make_a_flat_list_out_of_list_of_lists.py

ls_of_lists = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]

first_layer = [sublist for sublist in ls_of_lists]
print(first_layer)

flat_ls = [item for sublist in ls_of_lists for item in sublist]
print(flat_ls)


flatten = lambda l: [item for sublist in l for item in sublist]
print(flatten)


transformed_ls = flatten(ls_of_lists)
print(transformed_ls)

# To understand what was going on before
for sublist in ls_of_lists:
    for item in sublist:
        print(item)