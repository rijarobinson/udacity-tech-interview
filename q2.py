# O(nm)?

# Question 2
# Given a string a, find the longest palindromic substring contained in a.
# Your function definition should look like question2(a), and return a string.

# Notes for reviewer:
# I used "/" to replace characters to to keep track of letters found.
# This strikes me as being not a great practice, but I can't explain why
# If you have thoughts about this I'd love to hear

# Clarifying the Question/Assumptions:
# We want to determine if there are palindromes in the given string and
# return the text of the longest one


    # Assumptions:
    # Palindrome is at least 2 characters long, since any single character could
    #   potentially be a word, and we are not checking against a dictionary
    # Numbers and spaces within the string are ok, "/" is a reserved character
    # If there are multiple palindromes with the same length, the function
    #   will return the last one found
    # Case is disregarded
    # Any palindrome is acceptable, it doesn't need to be a
    #   legitimate English word

# Confirming input/output:
# We are taking in a string, a, containing only letters, numbers and spaces.
# Output is a string containing the longest palindrome

# Test Cases:
# Some examples of test cases might be:
    # a = 'tippit'
    # Checks for a proper return if the entire string is a palindrome. Return
    # should be 'tippit'. Edge case

    # a = 'tip pit'
    # Checks for proper return if a contains a space. Return should be 'tip pit'

    # a = 'xymmbc'
    # Tests for a 2-letter palindrome. Return should be 'mm'

    # a = 'zyjxjyzdmomomz'
    # Tests for a string having more than one palindrome. Should return
    # 'zyjxjyz'

    # a = 'xmoxmjomz'
    # Tests a string that has no palindromes > 1 character. Should return
    # designated error message "No palindromes found". Edge case


# Brainstorming

# For this problem, I know the input values would be strings and that I
# need to search a to find 1 or more palindromes and store those so I can
# determine which is the longest.

# I thought I could first reverse the string then find the first 2-letter
# substring and check if it is in the original string. If it is, I can
# keep adding to the string until it no longer matches, save the found
# string, then look for the next palindrome. Keep logging found palidromes
# until I run out of characters, then find the one with the longest length
# and return it.

# Edge cases: What if there are no palindromes within the string or
# there are multiple palindromes with the same length? I handled the first
# case by returning a message string and the 2nd case by simply returning
# the first palindrome found with that length.
# I decided not to check for wrong data type issues, but could
# using try/except TypeError lines. I decided to assume a value was supplied.

# I would consider checking to see if the entire string is a palindrome and
# return it right away. If not, I can proceed with checking for the
# palindromes within the string. However, I didn't include that check
# with this version.

# I decided that replacing string values in the searched string
# would allow me to keep track of items that have been already found. I am not
# sure if this was a good decision, and I appreciate feedback you might have.


#-------------------------M NEED TO DO THIS:------------------------------
# In big O notation for time, there are about 6 lines in constant time.
# Worst case would be ~O(3n log????? m) + 4). Where n is t and m is the
# *found* list.--O(n+m)



def question2(a):
    if "/" in a:
        return "'/' character not allowed"
    palin_build, found_palins = "", []
    # Reverse a to see if there are any matching substrings
    p = a[::-1]
    sps = 0
    # Only do this while a is not transformed to all '/' and we have checked
    # all items in p
    while (sps < len(p)) and (a != (len(a) * '/')):
        # Check to see if the first 3 characters of p are in the
        # original string
        if p[sps:sps+2] in a:
            # Add the characters to start of palindrome. Will need to
            # further check to see if additional charcters may be added
            palin_build = p[sps:sps+2]
            try:
                # Continue to try to build the matching string by checking
                # the found string plus the next character against a
                while (palin_build + p[sps+2]) in a:
                    # If it's in a, go ahead and add it to the palindrome found
                    # and increment to check the next character
                    palin_build += p[sps+2]
                    sps += 1
                # Finally, if the found palindrome is a verified palindrome and
                # a similar one was not already found, add it to the list of
                # found palindromes
                if (palin_build == palin_build[::-1] and
                        palin_build not in found_palins):
                    found_palins.append(palin_build)
                # Replace checked characters in a with '/'
                a = a.replace(palin_build, '/', 1)
            except IndexError:
                # If there is an index error, check it against a and add
                # it to palindromes found if matches and is not already there
                if (palin_build == palin_build[::-1] and len(palin_build) > 1 and
                        palin_build not in found_palins):
                    found_palins.append(palin_build)
                a = a.replace(palin_build, '/', 1)
                sps += 1
        else:
            # If the first three characters were not in a, replace the
            # checked characters with '/' so they cannot be found again
            a = a[::-1]
            a = a.replace(p[sps], '/', 1)
            a = a[::-1]
        sps += 1
    try:
        # Now check the list of found palindromes to see
        # which is the longest string
        return (max(found_palins, key=len))
    except ValueError:
        return "No palindromes found :("

print "test 1 should be tippit: %s" % question2('tippit')
print "test 1.1 should be tip pit: %s" % question2('tip pit')
print "test 1.2 should be mm: %s" % question2('xymmbc')
print "test 2 should be zyjxjyz: %s" % question2('zyjxjyzdmomomz')
print "test 3 should be No palindromes found: %s" % question2('xmoxmjomz')