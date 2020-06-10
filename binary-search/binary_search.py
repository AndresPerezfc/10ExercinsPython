def find(search_list, value):
    left = -1
    right = len(search_list)

    while left < right - 1:
        guess = left + ((right - left) // 2)
        if value == search_list[guess]:
            return guess
        elif search_list[guess] < value:
            left = guess
        else:
            right = guess

    raise ValueError("Not found")
