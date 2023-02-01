def a_list(lst_1, lst_2):

    merged_list = [(lst_1[i], lst_2[i]) for i in range(0, len(lst_1))]
    return merged_list


lst_1 = ["a", "b", "c"]
lst_2 = [1, 2, 3]
print(a_list(lst_1, lst_2))