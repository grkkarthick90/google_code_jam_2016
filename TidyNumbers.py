input = """4
132
1000
7
13216
"""

lines = input.splitlines()
numberOfCases = int(lines[0])

for number in range(numberOfCases):
    findTidy = lines[number+1]
    while True:
        if list(findTidy) == sorted(list(findTidy)):
            print 'Case #{}:'.format(number+1), findTidy
            break
        findTidy = str(long(findTidy) - 1)
