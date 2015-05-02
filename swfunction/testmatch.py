def matchseq(seq1, seq2):
    '''
    match two sequences for complementation at each character
    +1 for match
    -1 for mismatch
    0 for gap i.e. -
    '''

    score = 0
    
    for character in range(len(seq1)):
        if seq1[character] == seq2[character]:
            score = score +1
        elif seq1[character] == '-' or seq2[character] == '-':
            score = score
        else:
            score = score -1
    return score