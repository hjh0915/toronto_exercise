def find_population(continent_info):
    """ (dict of {str: dict of {str: dict of {str: int}}}) -> dict of {str: int}

    Precondition: continent_info has keys representing continents, and the
    values are dictionaries where the keys represent countries on that
    continent and the values are dictionaries where the keys represent cities
    in that country and the values represent city populations.

    Return a dictionary where the keys are continents from continent_info
    and the values are the total population of all cities on that continent.

    >>> data = {'Europe': {'France': {'Paris': 100, 'Nice': 50, 'Lyon': 4}, \
    'Bulgaria': {'Sofia': 3000}}}
    >>> result = find_population(data)
    >>> result == {'Europe': 3154}
    True
    >>> data = { \
    'North America': {'Canada': {'Toronto': 5000, 'Ottawa': 200}, \
    'USA': {'Portland': 400, 'New York': 5000, 'Chicago': 1000}, \
    'Mexico': {'Mexico City': 10000}}, \
    'Asia': {'Thailand': {'Bangkok': 456}, \
    'Japan': {'Tokyo': 10000, 'Osaka': 5000}}, \
    'Antarctica': {}}
    >>> result = find_population(data)
    >>> result == {'North America': 21600, 'Asia': 15456, 'Antarctica': 0}
    True
    """
    d = {}
    for continent in continent_info:
        d[continent] = 0
        for x in continent_info[continent]:
            for y in continent_info[continent][x]:
                d[continent] = d[continent] + continent_info[continent][x][y]
    return d

if __name__ == '__main__':
    data = { \
    'North America': {'Canada': {'Toronto': 5000, 'Ottawa': 200}, \
    'USA': {'Portland': 400, 'New York': 5000, 'Chicago': 1000}, \
    'Mexico': {'Mexico City': 10000}}, \
    'Asia': {'Thailand': {'Bangkok': 456}, \
    'Japan': {'Tokyo': 10000, 'Osaka': 5000}}, \
    'Antarctica': {}}

    result = find_population(data)

    print(result == {'North America': 21600, 'Asia': 15456, 'Antarctica': 0})