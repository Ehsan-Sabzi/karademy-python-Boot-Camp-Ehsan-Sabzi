def sum_numbers_equal_n(n):
    sum_numbers_n = list()
    for i in range(0, n//2+1):
        sum_numbers_n.append([i, n-i])
    return sum_numbers_n


def find_elements_in_list(sum_number_lst):
    for sum_number in sum_number_list:
        if str(sum_number[0]) in input_number_list and str(sum_number[1]) in input_number_list:
            print(f'The figures of {sum_number[0]} and {sum_number[1]} are in the position of '
                  f'{input_number_list.index(str(sum_number[0]))}'
                  f' and {input_number_list.index(str(sum_number[1]))} respectively')


if __name__ == '__main__':
    input_number_list_str = str(input("Please enter a series of number: ").split(',')).replace(' ', '')
    input_number_list = input_number_list_str.replace('[', '').replace(']', '').replace("'", "").split(',')
    input_number = input("Please enter a number: ")
    sum_number_list = sum_numbers_equal_n(int(input_number))
    find_elements_in_list(sum_number_list)
