# (1) 입력 자료 생성
import random
dataset = []
for i in range(10):
    r = random.randint(1, 100)
    dataset.append(r)

print(dataset)

# (2) 변수 초기화
vmax = vmin = dataset[0]
print(vmax)
print(vmin)

# (3) 최댓값/최소값 구하기
for i in dataset:
    if vmax < i:
        vmax = i
    if vmin > i:
        vmin = i

print('max = ', vmax, 'min = ', vmin)
