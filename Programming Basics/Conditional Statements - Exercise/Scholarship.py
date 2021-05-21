from math import floor

income = float(input())
grades = float(input())
salary = float(input())
social_scholarship = salary * 0.35
grades_scholarship = grades * 25

if income < salary and grades >= 5.50:
    if grades_scholarship > social_scholarship or grades_scholarship == social_scholarship:
        print(f'You get a scholarship for excellent results {floor(grades_scholarship)} BGN')
    else:
        print(f'You get a Social scholarship {floor(social_scholarship)} BGN')
elif income < salary and grades > 4.5:
    print(f'You get a Social scholarship {floor(social_scholarship)} BGN')
elif grades >= 5.50:
    print(f'You get a scholarship for excellent results {floor(grades_scholarship)} BGN')
else:
    print('You cannot get a scholarship!')
