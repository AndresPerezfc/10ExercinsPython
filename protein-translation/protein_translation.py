def proteins(strand):
    if (not(isinstance(strand, str)) or not(len(strand) % 3 == 0)):
        raise Exception('Invalid Input')
    dict = {'AUG': 'Methionine', 'UUU': 'Phenylalanine',
            'UUC': 'Phenylalanine', 'UUA': 'Leucine',
            'UUG': 'Leucine', 'UCU': 'Serine', 'UCC': 'Serine',
            'UCA': 'Serine', 'UCG': 'Serine', 'UAU': 'Tyrosine',
            'UAC': 'Tyrosine', 'UGU': 'Cysteine',
            'UGC': 'Cysteine', 'UGG': 'Tryptophan',
            'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'}

    codon_list = []

    for i in range(0, len(strand), 3):
        codon_list.append(strand[i] + strand[i+1] + strand[i+2])

    result = []
    for x in codon_list:
        translation = dict.get(x)
        if translation == "STOP":
            break
        result.append(translation)

    return result
