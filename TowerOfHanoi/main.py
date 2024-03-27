def tower_of_hanoi(disks, source, auxiliary, target):
    # Base case: If there's only one disk, move it directly to the target.
    if disks == 1:
        print("Move disk 1 from source", source, "to target", target)
        return

    # Move top (disks-1) disks from source to auxiliary using target as temporary.
    tower_of_hanoi(disks - 1, source, target, auxiliary)

    # Move the bottom disk from source to target.
    print("Move disk", disks, "from source", source, "to target", target)

    # Move the (disks-1) disks from auxiliary to target using source as temporary.
    tower_of_hanoi(disks - 1, auxiliary, source, target)

def main():
    # Ask the user for the number of disks.
    disks = int(input("Enter the number of disks: "))
    # Start the Tower of Hanoi with 'A' as source, 'B' as auxiliary, and 'C' as target.
    tower_of_hanoi(disks, 'A', 'B', 'C')

if __name__ == "__main__":
    main()
