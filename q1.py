# Question 1

# This is the complete working code
# Work in progress, It works, but always trying to improve

# Given two strings s and t, determine whether some anagram of t is a substring of s.
# For example: if s = "udacity" and t = "ad", then the function returns True. Your function
# definition should look like: question1(s, t) and return a boolean True or False."""

def question1(s, t):
  try:
    if s and t:
      found = []
      t = t.lower()
      s = s.lower()
      for c in t:
        if c in s:
          found.append(s.index(c))
          s = s.replace((c), "/", 1)
        else:
          return False
      return check_consecutive(found)
    else:
      return "did you supply the two words?"
  except TypeError:
    return "check the supplied information"

def check_consecutive(found):
    isTrue = True
    for i in found:
      if (i == max(found) and i - 1 in found) or (i == min(found) and i + 1 in found):
        isTrue = True
      elif i - 1 in found and i + 1 in found:
        isTrue = True
      else:
        isTrue = False
    return isTrue

# print "('udacity','AD') expected True: %s " % str(question1('udacity','AD'))
# print "('robin','robins') expected False: %s" % str(question1('robin','robins'))
# print "('taco cat','act taco') expected True: %s" % str(question1('taco cat','cat taco'))
# print "('','') expected Error Message: %s" % str(question1('',''))
# print "('udacity','city') expected True: %s" % str(question1('udacity','city'))
# print "('udaCity','city') expected True: %s" % str(question1('udaCity','city'))
# print "('marija','Raj') expected False: %s" % str(question1('marija','Raj'))
# print "('marija','mam') expected False: %s" % str(question1('marija','mam'))


# For this problem, I knew the input values would be strings and that I needed to
# search t to see if the value of s was not only in t, but that it could be
# an anagram (defined here as a consecutive substring in a different order)
# of a subset of t. So I needed to find a solution that would
# allow for the items to be out of order. I assumed that spaces provided in the
# anagram-substring should have a corresponding item in the main string. I am also
# assuming that the user will be inputting a legitimate word as the anagram and am
# disregarding case.

# I also thought of a few edge cases: What
# if the user inputs a number? Maybe they forget to enter a value. So, I checked for
# wrong data type issues using the try/except TypeError lines. Then I checked to make sure
# a value was supplied. Basically, the function searches through the supplied
# text (s) using the requested substring-anagram (t) and returns boolean True
# if the "word" is found, and False if it is not found. I would consider putting
# in a line that checks to see if the anagram-substring length is larger than the
# main string, in which case should return False right away, since the anagram
# can't contain more characters than the original string. I didn't include that
# in this solution; I think that may be overkill. In a real-world setting, I would
# need to balance adding that check (and the other checks above, for that matter) within
# the context of the application and the likelihood those instances would occur.

# Since we are looking for an anagram, I needed to make sure the function returned
# True for the items in any order. Therefore, I couldn't just search the main string
# for the substring as a whole. I needed to check to see if each letter was contained
# within the main string. One more thing I wanted to do was to create a constraint
# so that a letter appearing twice in the substring-anagram wouldn't return True
# if the letter wasn't contained twice within the main string.

# I decided that replacing string values in the searched string
# would allow me to keep track of items that have been already found.

# For each letter in the anagram-substring value, I checked to see if it is
# contained within the list created by the main string. If the item was in
# the list, the index of that item within s is appended to the found list
# so I could track where the item was found. This is repeated until there are
# no more letters to search or a match is not found, in which case returns False.
# If the anagram-substring has gone through and all letters are found, the "found"
# list is then sorted and checked to see if any index numbers are skipped so
# it can be assured that the found string is consecutive within s. If it passes
# this test, then the function returns True.

# In big O notation for time, there are about 4 lines in constant time.

# Worst case would be ~O(4n(2m) + 4). Where n is t and m is the *found* list.--O(nm)
