def possible_permutations(lst):
    """Version with self-made generator"""
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in possible_permutations(remLst):
            l.append([m] + p)
    return l


# def possible_permutations(lst):
#     """Version with itertools -> permutations"""
#     from itertools import permutations
#     all_perms = permutations(lst)
#     for perm in all_perms:
#         yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]
