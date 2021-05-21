movie_name = input()

seats_taken = 0
student_counter = 0
standard_counter = 0
kid_counter = 0

while movie_name != 'Finish':
    capacity = int(input())
    seats_taken = 0
    ticket_type = input()

    while ticket_type != 'End':
        seats_taken += 1
        if ticket_type == 'student':
            student_counter += 1
        elif ticket_type == 'standard':
            standard_counter += 1
        else:
            kid_counter += 1
        if seats_taken == capacity:
            break
        ticket_type = input()

    print(f'{movie_name} - {seats_taken / capacity * 100:.2f}% full.')
    movie_name = input()

total_tickets = student_counter + standard_counter + kid_counter

print(f'Total tickets: {total_tickets}')
print(f'{student_counter / total_tickets * 100:.2f}% student tickets.')
print(f'{standard_counter / total_tickets * 100:.2f}% standard tickets.')
print(f'{kid_counter / total_tickets * 100:.2f}% kids tickets.')