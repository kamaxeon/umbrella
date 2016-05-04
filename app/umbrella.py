
def baseComparison(sec1, sec2):
    valid_genome=['A', 'T', 'C', 'G']
    try:
        return get_base(sec1, valid_genome) ==  \
            get_base(sec2, valid_genome)
    except ValueError:
        return False

def get_base(sec, valid_genome):
    check_valid_base(sec, valid_genome)
    result = dict()
    for genome in valid_genome:
        result[genome] = sec.count(genome)
    return result

def check_valid_base(sec, valid_genome):
    for char in sec:
        if char not in valid_genome:
            raise ValueError('Base not valid')
