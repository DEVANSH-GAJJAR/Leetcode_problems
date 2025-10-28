def tower_of_hanoi_print(n, source='A', aux='B', target='C'):
    
    if n <= 0:
        return
    tower_of_hanoi_print(n-1, source, target, aux)
    # Move the nth (largest) disk from source to target
    print(f"Move disk {n} from {source} -> {target}")
    # Move the n-1 disks from aux to target
    tower_of_hanoi_print(n-1, aux, source, target)

# Example usage 
if __name__ == "__main__":
    n = int(input("Enter a number :- "))
    print(f"Number of moves required: {2**n - 1}\n")
    tower_of_hanoi_print(n)
