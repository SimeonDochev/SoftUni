price_skumriq = float(input())
price_caca = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_shells = int(input())
price_palamud = price_skumriq * 1.6
price_safrid = price_caca * 1.8
price_shells = 7.5

total_bill = kg_safrid * price_safrid + kg_shells * price_shells + kg_palamud * price_palamud
print(f'{total_bill:.2f}')
