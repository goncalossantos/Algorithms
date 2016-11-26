
hash_table = {}

def hash_palindromes_of_word(word, i):

    hash_table[word[::-1]] = (i, word)

    hash_table[word[:-1][::-1]] = (i, word)

def hash_palindrome_possibilies(array):

    for i,word in enumerate(array):
        hash_palindromes_of_word(word, i)

def find_correct_combinations(array):

    combinations = []
    for i,word in enumerate(array):
        if word in hash_table:
            (index, combination) = hash_table[word]
            if index != i:
                combinations.append((word, combination))
    return combinations

def find_palindromes(array):

    hash_palindrome_possibilies(array)

    return find_correct_combinations(array)


a = ["abc", "cba", "ddd", "gfh", "fg", "hfg"]

result = find_palindromes(a)
import pdb; pdb.set_trace()  # breakpoint 7552d1b1 //
