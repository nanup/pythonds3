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

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(a_list)
print(a_list)