b = [1, 2]
g = [3, 4]


n = len(b)
result = []
start_with = 'boy' if (min(b)<min(g)) else 'girl'
if start_with == 'boy':
    for i in range(n*2):
        if i%2 == 0:
            result.append(min(b))
            b.remove(min(b))
        else:
            result.append(min(g))
            g.remove(min(g))
            
    
print(result)

for i in range(n*2-1):
    if not result[i] <= result[i+1]:
        print('NO')
        break
else:
    print('YES')