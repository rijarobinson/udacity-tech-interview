# You should write up a clean and efficient answer in Python, as well as a text
# explanation of the efficiency of your code and your design choices.
# A qualified reviewer will look over your answer and give you feedback
# on anything that might be awesome or lacking-is your solution the most
# efficient one possible? Are you doing a good job of explaining your thoughts?
# Is your code elegant and easy to read?

# Answer the following questions:



# """Question 2
# Given a string a, find the longest palindromic substring contained in a. Your function
# definition should look like question2(a), and return a string."""

# This is the complete working code
# Work in progress, It works, but always trying to improve

def question2(a):
    palinBuild = ""
    foundPalins = []
    p = a[::-1]
    sps = 0
    while (sps < len(p)) and (a != (len(a) * '/')):
        if p[sps:sps + 3] in a:
            palinBuild = p[sps:sps + 3]
            try:
                while (palinBuild + p[sps+3]) in a:
                    palinBuild += p[sps+3]
                    sps += 1
                if palinBuild == palinBuild[::-1] and palinBuild not in foundPalins:
                    foundPalins.append(palinBuild)
                a = a.replace(palinBuild, '/', 1)
            except IndexError:
                if palinBuild == palinBuild[::-1] and len(palinBuild) > 2 and palinBuild not in foundPalins:
                    foundPalins.append(palinBuild)
                a = a.replace(palinBuild, '/', 1)
                sps += 1
        else:
            a = a[::-1]
            a = a.replace(p[sps], '/', 1)
            a = a[::-1]
        sps += 1
    try:
        maxItem = foundPalins[0]
        for item in foundPalins:
            if len(item) > len(maxItem):
                maxItem = item
        return "The first longest palindrome is: " + maxItem
    except IndexError:
        return "No palindromes found :("

# print question2('tippit')
# print question2('zyjxjyzdmomomz')
# print question2('xmoxmjomz')