def hanoi (num_disks, from_rod, with_rod, to_rod):
    if num_disks >= 1:
        hanoi(num_disks - 1, from_rod, with_rod, to_rod)
        move_disk(from_rod, to_rod)
        hanoi(num_disks - 1, with_rod, from_rod, to_rod)

def move_disk(from_rod, to_rod):
    print(f"Moved disk from {from_rod} to {to_rod}")

def main():
    hanoi(3, "A", "B", "C")

main()