def left_join(dict1, dict2):

    results = {}

    for key in dict1:
        results[key]=[dict1[key]]
        val = None
        if key in dict2:
            val = dict2[key]
        results[key].append(val)
    return results