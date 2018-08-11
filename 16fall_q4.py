def truncate_and_accumulate(values):
    """ (list of number) -> float

    Modify values so that each number is rounded down to the nearest integer
    value, and return the accumulated lost amount.

    >>> values = [1, 2.5, 3.3, 4.01]
    >>> truncate_and_accumulate(values)
    0.81
    >>> values
    [1, 2, 3, 4]
    >>> values = [0.25, 0.5, 0, 1, 33]
    >>> truncate_and_accumulate(values)
    0.75
    >>> values
    [0, 0, 0, 1, 33]
    >>> values = [10, 15, 20]
    >>> truncate_and_accumulate(values)
    0.0
    >>> values
    [10, 15, 20]
    """
    s = float(0)
    for i in range(len(values)):
        x = values[i] % 1
        s = s + x
        values[i] = int(values[i])
    return s 

if __name__ == '__main__':
    values = [0.25, 0.5, 0, 1, 33]
    print(truncate_and_accumulate(values))
