def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print(f"Move disk 1 from rod {source} to rod {destination}")
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print(f"Move disk {n} from rod {source} to rod {destination}")
    TowerOfHanoi(n-1, auxiliary, destination, source)

n = 5
TowerOfHanoi(n, 'A', 'C', 'B')  # A, B and C are names of rods
