# Rank students by average score, breaking ties alphabetically. Sample Input
# {'Alice':[90,85,88], 'Bob':[90,85,88], 'Charlie':[95,80,85]}
# Expected Output [('Alice', 87.67), ('Bob', 87.67), ('Charlie', 86.67)]
# Hint: Compute averages with sum()/len(). Sort with a lambda key (-average, name

#solution

student_scores = {'Alice':[90,85,88], 'Bob':[90,99,88], 'Charlie':[95,80,85]}

def countAverage(student_scores):
    averages = []
    for name in student_scores:
        scores = student_scores[name]
        each_average = (name, sum(scores)/len(scores))
        averages.append(each_average)

    return sorted(averages, key=lambda x: (-x[1], x[0]))


print(countAverage(student_scores))     
