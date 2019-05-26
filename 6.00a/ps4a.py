# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence)<= 1:
        return sequence
    else:
        perms = []
        for i in get_permutations (sequence[1:]):
            for j in range(len(i)+1):
                perms.append(i[:j]+sequence[0]+i[j:])
        return perms

if __name__ == '__main__':
    sequence = 'abc'
    print('Input:', 'abc')
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(sequence))
    
    sequence = 'bed'
    print('Input:', 'bed')
    print('Expected Output:', ['bed', 'ebd', 'edb', 'bde', 'dbe', 'deb'])
    print('Actual Output:', get_permutations(sequence))
    
    sequence = 'cat'
    print('Input:', 'cat')
    print('Expected Output:', ['cat', 'act', 'atc', 'cta', 'tca', 'tac'])
    print('Actual Output:', get_permutations(sequence))

