import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
         "Jack", "Queen", "King", "Ace"]

deck = [(suit, rank) for suit in suits for rank in ranks]

def simulate(trials=100000):
    red = heart_given_red = diamond_given_face = spade_or_queen = 0
    red_total = face_total = 0

    for _ in range(trials):
        card = random.choice(deck)
        suit, rank = card

        
        if suit in ["Hearts", "Diamonds"]:
            red += 1
            red_total += 1
            if suit == "Hearts":
                heart_given_red += 1

        
        if rank in ["Jack", "Queen", "King"]:
            face_total += 1
            if suit == "Diamonds":
                diamond_given_face += 1
            if suit == "Spades" or rank == "Queen":
                spade_or_queen += 1

    print("P(Red):", red / trials)
    print("P(Heart | Red):", heart_given_red / red_total)
    print("P(Diamond | Face):", diamond_given_face / face_total)
    print("P(Spade or Queen | Face):", spade_or_queen / face_total)

simulate()
