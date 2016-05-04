def baseComparison(sec1, sec2):
    try:
        return get_base(sec1) ==  get_base(sec2)
    except ValueError:
        return False

def get_base(sec):
    check_valid_base(sec)
    result = dict()
    for genome in sec:
        result[genome] = sec.count(genome)
    return result

def check_valid_base(sec):
    for char in sec:
        if char not in ['A', 'T', 'C', 'G']:
            raise ValueError('Base not valid')
