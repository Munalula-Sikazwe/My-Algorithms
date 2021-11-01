def tower_of_hanoi(number_of_rods, destination_rod, location_rod, auxiliary_rod):
    if number_of_rods == 1:
        print(f"moving rod number {number_of_rods} to {destination_rod} from {location_rod} ")
    else:
        tower_of_hanoi(number_of_rods - 1, auxiliary_rod, location_rod, destination_rod)
        print(f"moving rod number {number_of_rods} to {auxiliary_rod} from {location_rod}.")
        tower_of_hanoi(number_of_rods - 1, destination_rod, auxiliary_rod, location_rod)


tower_of_hanoi(4, "X", "Y", "Z")
