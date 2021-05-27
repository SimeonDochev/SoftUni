text = input()

symbols_count = {}

for sym in text:
    if sym not in symbols_count:
        symbols_count[sym] = 1
    else:
        symbols_count[sym] += 1

for sym, count in sorted(symbols_count.items(), key=lambda kvp: kvp[0]):
    print(f"{sym}: {count} time/s")
