def item_get_info():
    category, item, item_info = input().split(' - ')
    quantity_info, quality_info = item_info.split(';')
    quantity = int(quantity_info.split(':')[1])
    quality = int(quality_info.split(':')[1])

    return category, item, quantity, quality


item_categories = input().split(', ')
n = int(input())

inventory = {category: [] for category in item_categories}
total_items_count = 0
total_items_quality = 0

for _ in range(n):
    category, item, quantity, quality = item_get_info()
    total_items_count += quantity
    total_items_quality += quality
    if item not in inventory[category]:
        inventory[category].append(item)

average_item_quality = total_items_quality / len(inventory)
print(f"Count of items: {total_items_count}")
print(f"Average quality: {average_item_quality:.2f}")
for category, items in inventory.items():
    print(f"{category} -> {', '.join(items)}")
