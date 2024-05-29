def duplicated(string):
    for char in string:
        if string.count(char) > 1:
            return False
    return True

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def countofchars(name):
    counter = {}
    for char in name:
        counter[char] = name.count(char)
    return counter


def substrs_counter(name, n):
    if n > len(name):
        return 0
    return factorial(len(name)) // (factorial(n) * factorial(len(name) - n))


def generate_combinations(s, n, start=0, curr_combination=""):
    combinations = []
    if len(curr_combination) == n:
        if duplicated(curr_combination):
            combinations.append(curr_combination)
            return combinations
    
    for i in range(start, len(s)):
        combinations += generate_combinations(s, n, i + 1, curr_combination + s[i])
    
    return combinations

def wordrate(ratings):
    frate = 0
    biggest = 0
    for i in range(len(ratings)):
        if ratings[i] > biggest:
            frate = 1
            biggest = ratings[i]
        elif ratings[i] == biggest:
            frate +=1
    return frate

def rateofsubs(subs,subc):
    ratings = {}
    i = 0
    for sub in subs:
        temp = 0
        for char in sub:
            temp += int(subc[char])
        ratings[i] = temp
        i += 1
    return ratings
        

def main():
    name = str(input())
    n = int(input())

    counter = countofchars(name)
    subc = substrs_counter(name, n)
    subs = generate_combinations(name, n)
#    print(subs)
    ratings = rateofsubs(subs,counter)
    print(wordrate(ratings))


main()
