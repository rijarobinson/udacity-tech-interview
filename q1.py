# Question 1

# This is the complete working code
# Work in progress, It works, but always trying to improve

# Given two strings s and t, determine whether some anagram of t is a
# substring of s.
# For example: if s = "udacity" and t = "ad", then the function returns True.
# Your function definition should look like: question1(s, t) and return a
# boolean True or False."""

# this solution is "faster" but seems to be more time complex. O(n+m)?

# Clarifying the Question/Assumptions:
# We want to determine if t is contained within s in a different order (anagram)

    # Assumptions:
    # Letters and spaces only will be entered as a string
    # Spaces can be included
    # Case is disregarded
    # Any anagram is acceptable, it doesn't need to be a legitimate English word

# Confirming input/output:
# We are taking in 2 strings, s and t, containing only letters and spaces.
# Output is boolean True or False

# Test Cases:
# Some examples of test cases might be:
    # s = 'udacity'
    # t = 'AD'
    # Checks to see if the algorithm meets basic requirement of t being a
    # substring of s in any order and case is disregarded

    # s = 'robin'
    # t = 'robins'
    # Tests a case where t is longer than s, in which case, False could
    # immediately be returned (this check was not built into my example)
    # It could be included if case expects to be handled often

    # s = 'taco cat'
    # t = 'cat taco'
    # Included to check handling of spaces

    # s = ''
    # t = ''
    # Included to handle empty input

    # s = 'udacity'
    # t = 'city'
    # Included as an example where t is a substring but not necessarily
    # an anagram, should return False since it is not an anagram, but
    # simply a substring

    # s = 'udaCity'
    # t = 'tyci'
    # Included to check case handling and longer anagram

    # s = 'marija'
    # t = 'Raj'
    # Checks case handling and also checks that t's characters are contiguous
    # in s

    # s = 'marija'
    # t = 'mam'
    # A case where not all of the letters in t are in s (make sure a letter in
        # s can't get counted more than the actual number of times it appears)

# Brainstorming

# For this problem, I know the input values would be strings and that I
# needed to search s to see if the value of t was not only in s, but that
# it could be an anagram (defined here as a consecutive substring in a
# different order) of a subset of s. So I need to find a solution that will
# allow (and actually require) the items to be a different order than they
# appear in s.

# Edge cases: What if the user inputs a number? Maybe they forget to enter a
# value. I decided not to check for wrong data type issues, but could
# using try/except TypeError lines. I did decide I would like to make sure
# a value was supplied.

# I would consider checking to see if the anagram-substring length is larger
# than the main string, in which case should return False right away, since
# the anagram can't contain more characters than the original string. I won't
# include that in this solution; It might be overkill. In a real-world setting,
# I would need to balance adding that check (and the other checks above) within
# the context of the application and the likelihood those instances would occur.

# Since we are looking for an anagram, I need to make sure the function returned
# True for the items in any order. Therefore, I can't just search the main
# string for the substring as a whole. I need to check to see if each letter is
# contained within the main string in a contiguous fashion. One more thing I
# want to do was to create a constraint so that a letter appearing twice in
# t won't return True if the letter wasn't contained twice within s.

# I decided that replacing string values in the searched string
# would allow me to keep track of items that have been already found. I am not
# sure if this was a good decision, and I appreciate feedback you might have.


# In big O notation for time, there are about 4 lines in constant time.
# Worst case would be ~O(3n + m) + 4). Where n is t and m is the
# *found* list.--O(n+m)


def question1(s, t):
    # check to see if inputs were not empty, and if they are
    # return error message below
    if s and t:
        t, s = t.lower(), s.lower()
        # if t is in s in the same order, it is not an anagram, return False
        if t in s:
            return False
        # otherwise, continue. Initialize a list to hold indices
        # of matched letters in s
        found = []
        # for each item in t, check to see if the item exists in s
        # if it does, append the index of the found letter to found list
        # and then replace it in the original string with '/'. This ensures
        # the letter cannot be found again
        for c in t:
            if c in s:
                found.append(s.index(c))
                s = s.replace((c), "/", 1)
            # if no characters are found, return False
            else:
                return False
        # check to see if the letter found are consecutive within s
        return check_consecutive(found)
    else:
        return "did you supply the two words?"


def check_consecutive(found):
    # check each index of letters found in s to make sure it
    # is adjacent to the other letters found and return True if so
    for i in found:
        return ((((i == max(found) and i - 1 in found) or
                (i == min(found) and i + 1 in found))) or
                (i - 1 in found and i + 1 in found))


print "('udacity', 'AD') expected True: %s " % str(question1('udacity', 'AD'))
print "('robin', 'robins') expected False: %s" % str(question1('robin',
                                                               'robins'))
print "('taco cat', 'act taco') expected True: %s" % str(question1('taco cat',
                                                                   'cat taco'))
print "('', '') expected Error Message: %s" % str(question1('', ''))
print "('udacity', 'city') expected False: %s" % str(question1('udacity',
                                                              'city'))
print "('udaCity', 'tyci') expected True: %s" % str(question1('udaCity',
                                                              'tyci'))
print "('marija', 'Raj') expected False: %s" % str(question1('marija', 'Raj'))
print "('marija', 'mam') expected False: %s" % str(question1('marija',
                                                             'mam'))
