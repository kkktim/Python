person = {'name':'홍길동', 'age': 35, 'address':'서울시'}
person['pay'] = 350


# (1) 요소 검사
print(person['age'])
print('age' in person)    #True

# (2) 요소 반복
for key in person.keys():    # key 넘김
    print(key)
for v in person.values():
    print(v)
for i in person.items():
    print(i)

