"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    cnt = 0
    for paragraph in paragraphs:
        if select(paragraph):
            if cnt == k:
                return paragraph
            cnt += 1
    return ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    table = str.maketrans('', '', string.punctuation)

    def ignore_punctuation(s):
        return s.translate(table)

    def is_contain_topic(paragraph):
        splited = paragraph.split(' ')
        lowered = [ignore_punctuation(entry.lower()) for entry in splited]

        for entry in lowered:
            for wd in topic:
                if wd == entry:
                    print("DEBUG: ", wd, entry)
                    return True
        return False

    return is_contain_topic
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if not typed:
        return 0.0

    cnt = 0
    typed_split, reference_split = typed.split(), reference.split()
    for wd1, wd2 in zip(typed_split, reference_split):
        print('DEBUG: ', wd1, wd2)
        if wd1 == wd2:
            cnt += 1
    return cnt / len(typed_split) * 100
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return len(typed) / 5 * 60 / elapsed
    # END PROBLEM 4



def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word

    # most_similar = min(valid_words, key=lambda x: diff_function(user_word, x, limit))
    # print("DEBUG: ", key_distance_diff.call_count)
    # if diff_function(user_word, most_similar, limit) > limit:
    #     return user_word
    # else:
    #     return most_similar

    most_similar, min_diff = '', float('inf')
    for word in valid_words:
        tmp = diff_function(user_word, word, limit)
        if tmp < min_diff:
            most_similar = word
            min_diff = tmp

    if min_diff > limit:
        return user_word
    else:
        return most_similar
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    def helper(start, goal, limit, cnt=abs(len(start) - len(goal))):
        if cnt > limit or start == "" or goal == "":
            return cnt

        if start[0] != goal[0]:
            return helper(start[1:], goal[1:], limit, cnt + 1)
        else:
            return helper(start[1:], goal[1:], limit, cnt)
    return helper(start, goal, limit)
    # END PROBLEM 6


def meowstake_matches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""

    if limit < 0:
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 0
        # END
    elif goal == "" or start == "":
        return max(len(goal), len(start))
    elif start[0] == goal[0]:
        # BEGIN
        "*** YOUR CODE HERE ***"
        return meowstake_matches(start[1:], goal[1:], limit)
        # END

    else:
        add_diff = meowstake_matches(start, goal[1:], limit - 1)
        remove_diff = meowstake_matches(start[1:], goal, limit - 1)
        substitute_diff = meowstake_matches(start[1:], goal[1:], limit - 1)
        # BEGIN
        "*** YOUR CODE HERE ***"
        return min(add_diff, remove_diff, substitute_diff) + 1
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    cnt = 0
    for word1, word2 in zip(typed, prompt):
        if word1 != word2:
            break
        cnt += 1
    progress = cnt / len(prompt)
    send({'id': id, 'progress': progress})
    return progress
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    words_num, players_num = len(words), len(times_per_player)
    times = players_num * [[]]

    for i in range(players_num):
        for j in range(1, words_num + 1):
            # times[i] += ([times_per_player[i][j] - times_per_player[i][j - 1]])
            times[i] = times[i] + [times_per_player[i][j] - times_per_player[i][j - 1]]

    return game(words, times)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    players = range(len(all_times(game)))  # An index for each player
    words = range(len(all_words(game)))    # An index for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    words_num, players_scale = len(all_words(game)), len(all_times(game))
    fastest_per_player = [[]] * players_scale

    # for each word, select the player who typed fastest and then add the word to corresponding list for that player
    for i in range(0, words_num):
        least_time, corr_player = float("inf"), -1
        for j in range(0, players_scale):
            if time(game, j, i) < least_time:
                least_time = time(game, j, i)
                corr_player = j
        if corr_player != -1:
            fastest_per_player[corr_player] = fastest_per_player[corr_player] + [word_at(game, i)]

    return fastest_per_player
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you

##########################
# Extra Credit #
##########################

key_distance = get_key_distances()
def key_distance_diff(start, goal, limit):
    """ A diff function that takes into account the distances between keys when
    computing the difference score."""

    start = start.lower() #converts the string to lowercase
    goal = goal.lower() #converts the string to lowercase

    # BEGIN PROBLEM EC1
    "*** YOUR CODE HERE ***"

    if limit < 0 or abs(len(goal) - len(start)) > limit:
        return float("inf")

    elif start == goal:  # pruning
        return 0

    elif goal == "" or start == "":
        return max(len(goal), len(start))

    elif start[0] == goal[0]:
        return key_distance_diff(start[1:], goal[1:], limit)

    else:
        add_diff = key_distance_diff(start, goal[1:], limit - 1) + 1
        remove_diff = key_distance_diff(start[1:], goal, limit - 1) + 1
        substitute_diff = key_distance_diff(start[1:], goal[1:], limit - 1) + key_distance[start[0], goal[0]]
        return min(add_diff, remove_diff, substitute_diff)

    # def calc_diff(start, goal, limit):
    #     if limit < 0:
    #         return float("inf")
    #
    #     elif goal == "" or start == "":
    #         return max(len(goal), len(start))
    #
    #     elif start[0] == goal[0]:
    #         return calc_diff(start[1:], goal[1:], limit)
    #
    #     else:
    #         add_diff = calc_diff(start, goal[1:], limit - 1) + 1
    #         remove_diff = calc_diff(start[1:], goal, limit - 1) + 1
    #         substitute_diff = calc_diff(start[1:], goal[1:], limit - 1) + key_distance[start[0], goal[0]]
    #         return min(add_diff, remove_diff, substitute_diff)
    # calc_diff = memo(calc_diff)
    # return calc_diff(start, goal, limit)
    # END PROBLEM EC1

def memo(f):
    """A memoization function as seen in John Denero's lecture on Growth"""

    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return memoized

key_distance_diff = memo(key_distance_diff)
key_distance_diff = count(key_distance_diff)
autocorrect_cache = {}

def faster_autocorrect(user_word, valid_words, diff_function, limit):
    """A memoized version of the autocorrect function implemented above."""

    # BEGIN PROBLEM EC2
    "*** YOUR CODE HERE ***"
    # ??????????????????valid_words???????????????limit??????????????????word
    # 1.?????????cache?????????word??????valid_words, ??????cache
    # 2.?????????cache??????word???diff??????limit?????????user_word?????????autocorrect?????????
    print("DEBUG: ", key_distance_diff.call_count)
    if (user_word, diff_function) not in autocorrect_cache:
        autocorrect_cache[user_word, diff_function] = autocorrect(user_word, valid_words, diff_function, limit)
    print("DEBUG: ", key_distance_diff.call_count)
    return autocorrect_cache[user_word, diff_function]
    # END PROBLEM EC2


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)