# If the list is of length 0 or 1, then it is already sorted.
# Otherwise, divide the unsorted list into two sublists of about half the size.
# Recursively sort each sublist.
# Merge the two sorted sublists back into one sorted list.

def merge_sort(lst):
    # If the list is a single element or empty, it is already sorted
    if len(lst) <= 1:
        return lst

    # Divide the list in half
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    sorted_list = merge(left_half, right_half)

    return sorted_list


def merge(left, right):
    merged_list = []
    left_index = 0
    right_index = 0

    # Move through the lists until we have exhausted one
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1

    # If left_half still contains elements, add them
    if left_index < len(left):
        merged_list.extend(left[left_index:])

    # If right_half still contains elements, add them
    if right_index < len(right):
        merged_list.extend(right[right_index:])

    return merged_list


# Test the function
numbers = [34, 19, 47, 56, 2, 12, 98, 40, 37]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)  # Outputs: [2, 12, 19, 34, 37, 40, 47, 56, 98]
