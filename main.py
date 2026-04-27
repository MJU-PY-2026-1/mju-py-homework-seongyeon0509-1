# 파일이름 : 대륙을 구하는 용사 RPG(임시)
# 작 성 자 : 이성연
nickname = input("닉네임을 입력하세요 : ")

stat_names = ['힘' , '민첩', '지능', '운']

stats = []

for stat in stat_names:
  Value = int(input(f'{stat} 스텟을 입력하십시오 : '))
  stats.append(Value)

total = stats[0] + stats[1] + stats[2] + stats[3]

if total != 200:
  print(f'총 스텟의 합이 200이 아닙니다. (현재 합: {total})')
else:
  strength = stats[0]
  agility = stats[1]
  intelligence = stats[2]
  luck = stats[3]

  if strength >= agility and strength >= intelligence and strength >= luck:
    job = '전사'
  elif agility >= strength and agility >= intelligence and agility >= luck:
    job = '궁수'
  elif intelligence >= strength and intelligence >= agility and intelligence >= luck:
    job = '마법사'
  else:
    job = '도적'

print('\n=== 캐릭터 생성 완료 ===')
print(f'닉네임 : {nickname}')
print(f'직업 : {job}')

for i in range(4):
  print(f'{stat_names[i]} : {stats[i]}')

