import numpy as np

states = ["Sunny", "Cloudy", "Rainy"]

transition_matrix = [
    [0.6, 0.3, 0.1],
    [0.3, 0.4, 0.3],
    [0.2, 0.5, 0.3]
]

def simulate(days):
    current = "Sunny"
    weather = [current]

    for i in range(days):
        if current == "Sunny":
            current = np.random.choice(states, p=transition_matrix[0])
        elif current == "Cloudy":
            current = np.random.choice(states, p=transition_matrix[1])
        else:
            current = np.random.choice(states, p=transition_matrix[2])

        weather.append(current)

    return weather


def count_rain(weather):
    return weather.count("Rainy")


result = simulate(10)

print("Weather Forecast for 10 Days:")
for i in range(len(result)):
    print("Day", i + 1, ":", result[i])


trials = 10000
success = 0

for i in range(trials):
    seq = simulate(10)
    if count_rain(seq) >= 3:
        success += 1

prob = success / trials

print("\nProbability Analysis:")
print("At least 3 rainy days =", round(prob, 3))
