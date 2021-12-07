# Similar to std::transform. map, but convert to list after
def transform(function, iterable):
    return list(map(function, iterable))
