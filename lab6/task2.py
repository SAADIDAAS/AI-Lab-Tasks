def heuristic_value(number):
    return abs(20 - number)


def beam_search(start_value, goal_value, beam_width=2):

    beam_states = [(start_value, [start_value])]
    level_number = 0

    while beam_states:

        print("\nlevel", level_number)

        candidate_states = []

        for current_number, path_taken in beam_states:

            if current_number == goal_value:
                return path_taken

            next_numbers = [
                current_number + 2,
                current_number + 3,
                current_number * 2
            ]

            for next_number in next_numbers:

                if next_number <= 40:
                    new_path = path_taken + [next_number]
                    candidate_states.append((next_number, new_path))

        candidate_states.sort(key=lambda state: heuristic_value(state[0]))

        beam_states = candidate_states[:beam_width]

        print("numbers kept:", [state[0] for state in beam_states])

        level_number += 1

    return None


final_path = beam_search(1, 20, 2)

print("\nfinal path to reach 20:", final_path)
