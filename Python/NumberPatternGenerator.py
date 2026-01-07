def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    if n <= 0:
        return 'Argument must be an integer greater than 0.'
    last_line = ' '.join(str(j) for j in range(1, n + 1))
    return last_line

print(number_pattern(12))
