words = [f"{word} -> {len(word)}" for word in input().split(', ')]

print(*words, sep=', ')
