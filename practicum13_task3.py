favorites_of_sladkoeshkin = set(input().lower().split())
num_friends = int(input())

for i in range(num_friends):
    friends_favorites = set(input().lower().split())
    favorites_of_sladkoeshkin -= friends_favorites

print(f'Только Сладкоежкину нравится: {len(favorites_of_sladkoeshkin)}')











