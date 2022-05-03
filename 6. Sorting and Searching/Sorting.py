def bubble_sort(a_list):
    for i in range(len(a_list) - 1, 0, -1):
        exchanges = False
        for j in range(i):
            if a_list[j] > a_list[j + 1]:
                exchanges = True
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
            else:
                exchanges = False
        
        if not exchanges:
            break

def selection_sort(a_list):
    for i in range(len(a_list) - 1, 0, -1):
        biggest = i
        for j in range(i):
            if a_list[j] > a_list[biggest]:
                 biggest = j
            
        if biggest != i:
            a_list[biggest], a_list[i] = a_list[i], a_list[biggest]

def insert_sort(a_list):
    for i in range(1, len(a_list)):
        cur_pos = i
        cur_val = a_list[i]

        while cur_pos > 0 and a_list[cur_pos - 1] > cur_val:
            a_list[cur_pos] = a_list[cur_pos - 1]
            cur_pos -= 1
        a_list[cur_pos] = cur_val

def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for i in range(sublist_count):
            insertion_gap_sort(a_list, i, sublist_count)
        print("After increments of size", sublist_count, "the list is", a_list)
        sublist_count = sublist_count // 2

def insertion_gap_sort(a_list, start, gap):
    for j in range(start + gap, len(a_list), gap):
        cur_pos = j
        cur_val = a_list[j]
        while cur_pos >= gap and a_list[cur_pos - gap] > cur_val:
            a_list[cur_pos] = a_list[cur_pos - gap]
            cur_pos -= gap
        a_list[cur_pos] = cur_val

def merge_sort(a_list):
    if len(a_list) > 1:
        print("Splitting", a_list)
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                a_list[k] = left_half[i]
                i += 1
            else:
                a_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j += 1
            k += 1
        print("Merging", a_list)

def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)

def quick_sort_helper(a_list, first, last):
    if first < last:
        split = partition(a_list, first, last)
        partition(a_list, first, split - 1)
        partition(a_list, split + 1, last)

def partition(a_list, first, last):
    mid = a_list[len(a_list[first:last + 1]) // 2]
    pivot_list = [a_list[first], mid, a_list[last]]
    pivot_list.sort()
    pivot = pivot_list[len(pivot_list) // 2]
    pivot_pos = a_list.index(pivot)

    if pivot_pos == first:
        left = first + 1
        right = last
    elif pivot_pos == last:
        left = first
        right = last - 1
    else:
        left = first
        right = last

    done = False

    while not done:
        while a_list[left] <= a_list[right] and a_list[right] >= pivot:
            right -= 1
        while a_list[left] <= a_list[right] and a_list[left] <= pivot:
            left += 1
        if right < left:
            done = True
        else:
            a_list[left], a_list[right] = a_list[right], a_list[left]
    if pivot >= a_list[right] and pivot_pos <= right:
        a_list[pivot_pos], a_list[right] = a_list[right], a_list[pivot_pos]
    else:
        a_list[pivot_pos], a_list[right + 1] = a_list[right + 1], a_list[pivot_pos]

    return right

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(a_list)
print(a_list)