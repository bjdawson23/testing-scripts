# Online Python - IDE, Editor, Compiler, Interpreter


# dictionary comprehension to create a dictionary of the numbers 1–5 mapped to their cubes
{number: number ** 3 for number in range(1, 6)}

# set - unique set of values, so the below would only return 0-15
nums = list(range(16)) + list(range(7))
set(nums)

# Unites the sets - 1, 2, 3, 4, 5
{1, 3, 5} | {2, 3, 4}
# diff between right and the left sets - 1, 5
{1, 3, 5} -  {2, 3, 4}
# intersection of right and the left sets - 3
{1, 3, 5} &  {2, 3, 4}

# set right side is a superset of the left side will = true
set('h d a f g').issuperset('ha dad')


