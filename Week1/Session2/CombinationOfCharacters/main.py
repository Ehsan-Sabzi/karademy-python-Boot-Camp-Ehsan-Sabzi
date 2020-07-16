def combination_string(chars, n):
    if n == 1:
        return [char for char in chars]
    return [i + j for i in chars for j in combination_string(chars, n-1)]


if __name__ == '__main__':
    print(combination_string('abc', 3))