from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(num) for num in input().split()]
locks = deque([int(num) for num in input().split()])
intelligence_value = int(input())

money_spent_on_bullets = 0
unlocked_locks = 0

bullets_counter = gun_barrel_size

while locks:
    if bullets:
        current_bullet = bullets.pop()
        money_spent_on_bullets += bullet_price
        current_lock = locks.popleft()
        if current_bullet <= current_lock:
            print("Bang!")
            bullets_counter -= 1
            if bullets_counter == 0 and bullets:
                print("Reloading!")
                bullets_counter = gun_barrel_size
            unlocked_locks += 1
            if not locks:
                print(f"{len(bullets)} bullets left. Earned ${intelligence_value - money_spent_on_bullets}")
                break
        else:
            print("Ping!")
            bullets_counter -= 1
            if bullets_counter == 0 and bullets:
                print("Reloading!")
                bullets_counter = gun_barrel_size
            locks.appendleft(current_lock)
    else:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break
