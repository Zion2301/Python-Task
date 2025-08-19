# Group sentences that are anagrams of each other, ignoring spaces and punctuation.
# Sample Input ['Listen to me', 'Enlist to me', 'The eyes', 'They see']
# Expected Output [['Listen to me', 'Enlist to me'], ['The eyes', 'They see']]
# Hint: Normalize sentences and use sorted characters or frequency counts as keys.

def normalize(sentence):
    # remove spaces
    no_spaces = sentence.replace(" ", "")
    # make lowercase
    lowered = no_spaces.lower()
    # sort letters
    sorted_letters = "".join(sorted(lowered))
    return sorted_letters

# print(normalize("Listen to me"))  # just testing
# print(normalize("Enlist to me"))  # should look the same


def isAnagram(sentences):

    groups = {}
    for s in sentences:
        key = normalize(s)
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())



print(isAnagram(["Listen to me", "Enlist to me", "The eyes", "They see"]))



