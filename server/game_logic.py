def determine_winner(c1, c2):
    if c1 == c2:
        return 'draw'
    rules = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    return 'player1' if rules[c1] == c2 else 'player2'
