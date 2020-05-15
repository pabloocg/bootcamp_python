def ft_reduce(function, sequence, initial=None):
    if isinstance(sequence[0], int):
        ret = 0
    elif isinstance(sequence[0], str):
        ret = ""
    if initial:
        ret = initial
    iret = function(sequence[0], sequence[1])
    ret = function(ret, iret)
    for i in range(2, len(sequence)):
        ret = function(ret, sequence[i])
    return ret
