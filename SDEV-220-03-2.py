
def good():
    return ['Harry', 'Ron', 'Hermione']


def get_odds():
    for number in range(1, 10, 2):
        yield number


for i, odd_number in enumerate(get_odds()):
    if i == 2:
        print("Third odd number:", odd_number)
        break
