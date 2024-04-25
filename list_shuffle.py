import random


def shuffle_list(lst):
    """
    Moves each item in the list to a different position.
    Args:
        lst (list): The input list.
    Returns:
        list: A new list with the items in different positions.
    """
    shuffled_lst = lst[:]

    for i in range(len(lst)):
        item = shuffled_lst.pop(i)
        new_index = random.randint(0, len(shuffled_lst))
        shuffled_lst.insert(new_index, item)
    return shuffled_lst


my_list = [1, 2, 3, 4, 5]
shuffled_list = shuffle_list(my_list)
print("Original list:", my_list)
print("Shuffled list:", shuffled_list)