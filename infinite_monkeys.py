""" Simulating the Infinite Monkeys problem."""
import random


def string_generator(length):
    """ Generate a lower-case string of given length """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               ' ']
    random_string = ""
    for _ in range(length):
        rnd = random.randint(0, 26)
        random_string = random_string + letters[rnd]
    return random_string


def improved_string_generator(original_string, previous_string):
    """ Generate a lower-case string the same length
    as the original_string and save correct characters
    from previous guesses."""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               ' ']
    semi_random_string = ""
    for i, _ in enumerate(original_string):
        if (len(previous_string) == len(original_string)) \
           and (original_string[i] == previous_string[i]):
            semi_random_string = semi_random_string + original_string[i]
        else:
            rnd = random.randint(0, 26)
            semi_random_string = semi_random_string + letters[rnd]
    return semi_random_string


def string_comparer(s_1, s_2):
    """ Compare two strings and return the number of similar characters """
    if len(s_1) != len(s_2):
        raise RuntimeError("Strings must be of the same length to be",
                           "compared.")
    match_count = 0
    for i, _ in enumerate(s_1):
        if s_1[i] == s_2[i]:
            match_count = match_count + 1
    return match_count


def generate_matching_string_v1(original_string):
    """ Compare the original_string with randomly
    generated strings until there is a match. Count
    the number of attempts. """
    count = 1
    while True:
        new_string = string_generator(len(original_string))
        if new_string != original_string:
            print(new_string)
            print("Not a match on attempt %i" % (count))
            print(original_string)
            print(" ")
            count = count + 1
        else:
            print(new_string)
            print("Match! On attempt %i" % (count))
            return


def generate_matching_string_v2(original_string):
    """ Compare the original_string with randomly
    generated strings until there is a match. Count
    the number of attempts and track the length of
    the word that, so far,  has most closely matched
    the original string. """
    count = 1
    closest_match_count = 0
    while True:
        new_string = string_generator(len(original_string))
        print("\n")
        if new_string != original_string:
            print(new_string)
            print(original_string)
            print("Not a match on attempt %i" % (count))
            count = count + 1
            match_count = string_comparer(original_string, new_string)
            if match_count > closest_match_count:
                closest_match_count = match_count
            print("Closest match so far is %i/%i" % (closest_match_count,
                                                     len(original_string)))
        else:
            print(new_string)
            print("Match! On attempt %i" % (count))
            return


def generate_matching_string_v3(original_string):
    """ Compare the original_string with randomly
    generated strings until there is a match. Count
    the number of attempts and report the word that
    has, so far, most closely matched the
    original_string. """
    count = 1
    closest_match_count = 0
    closest_match = ""
    closest_match_list = []
    while True:
        new_string = string_generator(len(original_string))
        print("\n")
        if new_string != original_string:
            print(new_string)
            print(original_string)
            print("Not a match on attempt %i" % (count))
            count = count + 1
            match_count = string_comparer(original_string, new_string)
            if match_count > closest_match_count:
                closest_match_count = match_count
                closest_match = new_string
                closest_match_list.append(closest_match)
            print("Closest match so far: %s (%i/%i)" % (closest_match,
                                                        closest_match_count,
                                                        len(original_string)))
        else:
            print(original_string)
            print(new_string)
            print("Match! On attempt %i" % (count))
            print(closest_match_list)
            return


def generate_matching_string_v4(original_string):
    """ Compare the original_string with strings
    generated such that characters that don't match
    are randomly chosen in new iterations. """
    count = 1
    closest_match_count = 0
    closest_match = ""
    closest_match_list = []
    while True:
        new_string = improved_string_generator(original_string,
                                               closest_match)
        print("\n")
        if new_string != original_string:
            print(new_string)
            print(original_string)
            print("Not a match on attempt %i" % (count))
            count = count + 1
            match_count = string_comparer(original_string, new_string)
            if match_count > closest_match_count:
                closest_match_count = match_count
                closest_match = new_string
                closest_match_list.append(closest_match)
            print("Closest match so far: %s (%i/%i)" % (closest_match,
                                                        closest_match_count,
                                                        len(original_string)))
        else:
            print(original_string)
            print(new_string)
            print("Match! On attempt %i" % (count))
            closest_match_list.append(new_string)
            print("\nProgression: ")
            for string in closest_match_list:
                print(string)
            return


SEARCH_STRING = ("a fool thinks himself to be wise" +
                 " but a wise man knows himself to be a fool")
generate_matching_string_v4(SEARCH_STRING)
