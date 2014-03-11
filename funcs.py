def accum_map(vals, init=0):
    def _truth_adjust(val):
        if val:
            return 1
        return -1
   
    accum = init
    for v in vals:
        accum += _truth_adjust(v)
        accum = max(accum, init)
        yield accum

