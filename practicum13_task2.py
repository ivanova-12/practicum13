num_of_students = int(input())

curses1 = set(input().lower().split())
for i in range(1, num_of_students):
    curses = set(input().lower().split())
    curses1 &= curses

print(f'Кол-во курсов выбранных всеми студентами: {len(curses1)}')












