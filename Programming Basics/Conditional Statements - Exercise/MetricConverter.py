number = float(input())
metric_unit = input()
output_metric_unit = input()
result = 0

if metric_unit == 'mm' and output_metric_unit == 'cm':
    result = number / 10
elif metric_unit == 'mm' and output_metric_unit == 'm':
    result = number / 1000
elif metric_unit == 'cm' and output_metric_unit == 'mm':
    result = number * 10
elif metric_unit == 'cm' and output_metric_unit == 'm':
    result = number / 100
elif metric_unit == 'm' and output_metric_unit == 'mm':
    result = number * 1000
elif metric_unit == 'm' and output_metric_unit == 'cm':
    result = number * 100

print(f'{result:.3f}')

