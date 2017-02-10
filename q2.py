# You should write up a clean and efficient answer in Python, as well as a text
# explanation of the efficiency of your code and your design choices.
# A qualified reviewer will look over your answer and give you feedback
# on anything that might be awesome or lacking-is your solution the most
# efficient one possible? Are you doing a good job of explaining your thoughts?
# Is your code elegant and easy to read?

# Answer the following questions:



# O(nm)?

# """Question 2
# Given a string a, find the longest palindromic substring contained in a. Your function
# definition should look like question2(a), and return a string."""

# This is the complete working code
# Work in progress, It works, but always trying to improve

# Assumptions:
# Palindrome is at least 2 characters long, since any single character could
#   potentially be a word, and we are not checking against a dictionary
# Numbers and spaces are ok, "/" is a reserved character
# If there are multiple palindromes with the same length, the function
#   will return the last one found


def question2(a):
    if "/" in a:
        return "'/' character not allowed"
    palinBuild = ""
    foundPalins = []
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
            palinBuild = p[sps:sps+2]
            try:
                # Continue to try to build the matching string by checking
                # the found string plus the next character against a
                while (palinBuild + p[sps+2]) in a:
                    # If it's in a, go ahead and add it to the palindrome found
                    # and increment to check the next character
                    palinBuild += p[sps+2]
                    sps += 1
                # Finally, if the found palindrome is a verified palindrome and
                # a similar one was not already found, add it to the list of
                # found palindromes
                if (palinBuild == palinBuild[::-1] and
                        palinBuild not in foundPalins):
                    foundPalins.append(palinBuild)
                # Replace checked characters in a with '/'
                a = a.replace(palinBuild, '/', 1)
            except IndexError:
                # If there is an index error, check it against a and add
                # it to palindromes found if matches and is not already there
                if (palinBuild == palinBuild[::-1] and len(palinBuild) > 1 and
                        palinBuild not in foundPalins):
                    foundPalins.append(palinBuild)
                a = a.replace(palinBuild, '/', 1)
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
        return (max(foundPalins, key=len))
    except ValueError:
        return "No palindromes found :("

print "test 1 should be tippit: %s" % question2('tippit')
print "test 1 should be mm: %s" % question2('xymmbc')
print "test 2 should be zyjxjyz: %s" % question2('zyjxjyzdmomomz')
print "test 3 should be No palindromes found: %s" % question2('xmoxmjomz')