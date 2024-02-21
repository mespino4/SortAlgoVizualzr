# sorting_algorithms.py
import constants

# bubble sort
def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_info.draw_list({j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                yield True

    return lst

# insertion sort
def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(1, len(lst)):
        current = lst[i]

        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current
            draw_info.draw_list({i - 1: draw_info.GREEN, i: draw_info.RED}, True)
            yield True

    return lst

# Quick sort algorithm
def quick_sort(draw_info, ascending=True):
    def partition(lst, low, high):
        pivot = lst[high]
        i = low - 1

        for j in range(low, high):
            if (lst[j] <= pivot and ascending) or (lst[j] >= pivot and not ascending):
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
                draw_info.draw_list({i: draw_info.GREEN, j: draw_info.RED}, True)
                yield True

        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        draw_info.draw_list({i + 1: draw_info.GREEN, high: draw_info.RED}, True)
        yield True
        return i + 1

    def quick_sort_helper(lst, low, high):
        if low < high:
            pi = yield from partition(lst, low, high)
            yield from quick_sort_helper(lst, low, pi - 1)
            yield from quick_sort_helper(lst, pi + 1, high)

    yield from quick_sort_helper(draw_info.lst, 0, len(draw_info.lst) - 1)


# Shell sort algorithm
def shell_sort(draw_info, ascending=True):
    n = len(draw_info.lst)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = draw_info.lst[i]
            j = i

            while j >= gap and (draw_info.lst[j - gap] > temp) == ascending:
                draw_info.lst[j] = draw_info.lst[j - gap]
                j -= gap

            draw_info.lst[j] = temp
            draw_info.draw_list({j: draw_info.GREEN, i: draw_info.RED}, True)
            yield True

        gap //= 2

# Heap sort algorithm
def heap_sort(draw_info, ascending=True):
    def heapify(lst, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and (lst[left] > lst[largest]) == ascending:
            largest = left

        if right < n and (lst[right] > lst[largest]) == ascending:
            largest = right

        if largest != i:
            lst[i], lst[largest] = lst[largest], lst[i]
            draw_info.draw_list({i: draw_info.RED, largest: draw_info.GREEN}, True)
            yield True
            yield from heapify(lst, n, largest)

    n = len(draw_info.lst)

    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(draw_info.lst, n, i)

    for i in range(n - 1, 0, -1):
        draw_info.lst[i], draw_info.lst[0] = draw_info.lst[0], draw_info.lst[i]
        draw_info.draw_list({0: draw_info.RED, i: draw_info.GREEN}, True)
        yield True
        yield from heapify(draw_info.lst, i, 0)

# Selection sort algorithm
def selection_sort(draw_info, ascending=True):
    n = len(draw_info.lst)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if (draw_info.lst[j] < draw_info.lst[min_idx]) == ascending:
                min_idx = j

        draw_info.lst[i], draw_info.lst[min_idx] = draw_info.lst[min_idx], draw_info.lst[i]
        draw_info.draw_list({i: draw_info.GREEN, min_idx: draw_info.RED}, True)
        yield True

# Bucket sort algorithm
def bucket_sort(draw_info, ascending=True):
    def bucket_sort_helper(lst, ascending):
        buckets = [[] for _ in range(len(lst))]
        max_val = max(lst)
        min_val = min(lst)
        range_val = (max_val - min_val) / len(lst)

        for val in lst:
            index = min(int((val - min_val) / range_val), len(lst) - 1)  # Ensure index is within bounds
            buckets[index].append(val)

        sorted_list = []
        for bucket in buckets:
            sorted_list.extend(sorted(bucket))

        if not ascending:
            sorted_list = sorted_list[::-1]

        for i, val in enumerate(sorted_list):
            draw_info.lst[i] = val
            draw_info.draw_list({}, True)
            yield True

    yield from bucket_sort_helper(draw_info.lst, ascending)


"""
# Merge sort algorithm
def merge_sort(draw_info, ascending=True):
    def merge(lst, left, right, ascending):
        result = []
        left_index = right_index = 0

        while left_index < len(left) and right_index < len(right):
            if (left[left_index] <= right[right_index] and ascending) or \
               (left[left_index] >= right[right_index] and not ascending):
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result

    def merge_sort_helper(lst, ascending):
        if len(lst) <= 1:
            return lst

        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        left = yield from merge_sort_helper(left, ascending)
        right = yield from merge_sort_helper(right, ascending)

        # Merge the sorted left and right halves
        merged = merge(lst, left, right, ascending)

        # Update the original list in draw_info with the merged result
        for i, val in enumerate(merged):
            lst[i] = val

        # Visualize the merging process after merging both halves
        draw_info.draw_list({}, True)
        yield True

        return merged

    yield from merge_sort_helper(draw_info.lst, ascending)

"""