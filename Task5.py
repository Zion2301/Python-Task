# Compress a sentence by replacing each unique word with an integer ID.
# Sample Input 'the cat sat on the mat'
# Expected Output encoded = [1,2,3,4,1,5], mapping = {1:'the',2:'cat',3:'sat',4:'on',5:'mat'}
# Hint: Use a dictionary to map words to IDs, assign IDs on first occurrence.

def assignInt(str):
    splitedstring = str.split()
    emptydic = {}
    emptylist = []
    next_id = 1
    for string in splitedstring:
        if string not in emptydic:
            emptydic[string]= next_id
            next_id += 1
        emptylist.append(emptydic[string])

    return emptylist

    


print(assignInt("the cat sat on the mat"))