def flights(*args):
    flights_dict = {}

    for idx in range(0, len(args) - 1, 2):
        if args[idx] == "Finish":
            break
        destination = args[idx]
        if destination not in flights_dict:
            flights_dict[destination] = 0
        flights_dict[destination] += args[idx+1]

    return flights_dict
