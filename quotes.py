import random

quotes = [
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Don't watch the clock; do what it does. Keep going.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "It does not matter how slowly you go as long as you do not stop.",
    "Everything you want is on the other side of fear.",
    "Believe you can and you're halfway there.",
    "The only impossible journey is the one you never begin.",
    "Success is the sum of small efforts repeated day in and day out.",
    "Your limitation—it's only your imagination."
]

def get_random_quote():
    return random.choice(quotes)
