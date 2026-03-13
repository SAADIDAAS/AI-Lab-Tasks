import random

def calculate_fx(x):
    return -x*x + 6*x


def hill_climbing():

    current_x = random.randint(0, 6)

    print("initial x:", current_x)
    print("initial f(x):", calculate_fx(current_x))

    while True:

        neighbor_values = []

        if current_x - 1 >= 0:
            neighbor_values.append(current_x - 1)

        if current_x + 1 <= 6:
            neighbor_values.append(current_x + 1)

        best_neighbor = current_x
        best_value = calculate_fx(current_x)

        for neighbor in neighbor_values:

            neighbor_value = calculate_fx(neighbor)

            if neighbor_value > best_value:
                best_value = neighbor_value
                best_neighbor = neighbor

        if best_neighbor == current_x:
            break

        current_x = best_neighbor
        print("move to x:", current_x, "f(x):", calculate_fx(current_x))

    print("\nfinal optimal x:", current_x)
    print("final f(x):", calculate_fx(current_x))


hill_climbing()
