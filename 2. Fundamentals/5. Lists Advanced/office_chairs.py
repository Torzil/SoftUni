def chair_counter(rooms):
    total_free_chairs = 0
    for room_number in range(1, total_rooms + 1):
        chairs_and_visitors = input().split()
        free_chairs = len(chairs_and_visitors[0]) - int(chairs_and_visitors[1])
        if free_chairs < 0:
            print(f"{abs(free_chairs)} more chairs needed in room {room_number}")
        total_free_chairs += free_chairs
    return total_free_chairs


total_rooms = int(input())
chairs_left = chair_counter(total_rooms)
if chairs_left >= 0:
    print(f"Game On, {chairs_left} free chairs left")


