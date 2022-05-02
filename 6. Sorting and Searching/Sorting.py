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

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insert_sort(a_list)
print(a_list)