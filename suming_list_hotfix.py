def summing_list(a_list):
    sum = 0
    for i in a_list:
        if i.isnumeric():
            sum = sum + i
        else:
            pass