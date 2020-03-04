"""
https://www.hackerrank.com/challenges/the-minion-game/
"""

DRAW = 'Draw'
PLAYER_CONSONANTS = 'Stuart'
PLAYER_VOWELS = 'Kevin'


def minion_game(string):
    """Kevin and Stuart want to play the 'The Minion Game'.

    Game Rules
    Both players are given the same string, S    .
    Both players have to make substrings using the letters of the string S.
    Stuart has to make words starting with consonants.
    Kevin has to make words starting with vowels.
    The game ends when both players have made all possible substrings.

    Scoring
    A player gets +1 point for each occurrence of the substring in the string S.

    :type string: str
    :rtype: None
    """
    vowels = sum(len(string) - i for i, c in enumerate(string) if c in 'AEIOU')
    consonants = sum(len(string) - i for i, c in enumerate(string) if c not in 'AEIOU')

    if vowels == consonants:
        print(DRAW)
    elif vowels > consonants:
        print(f'{PLAYER_VOWELS} {vowels}')
    else:
        print(f'{PLAYER_CONSONANTS} {consonants}')


if __name__ == '__main__':
    s = input()
    minion_game(s)