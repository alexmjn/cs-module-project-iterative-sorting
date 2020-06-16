def partition()


def quicksort(our_list):
    if len(our_list) <= 1:
        return our_list

    pivot = our_list[0]
    left = []
    right = []

    for current in our_list[1:]:
        if current > pivot:
            right.append(current)

        elif current <= pivot:
            left.append(current)

    return quicksort(left) + pivot + quicksort(right)
