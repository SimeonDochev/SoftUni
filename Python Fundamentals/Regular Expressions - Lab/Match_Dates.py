import re

dates = input()
pattern = r"(?P<day>\d{2})(?P<separator>[\.\-/])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"

valid_dates = [match_obj.groupdict() for match_obj in re.finditer(pattern, dates)]

print('\n'.join([f"Day: {data['day']}, Month: {data['month']},"f" Year: {data['year']}" for data in valid_dates]))
