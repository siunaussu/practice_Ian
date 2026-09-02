from collections import namedtuple, defaultdict, Counter

User = namedtuple('User', ['id', 'name', 'age'])
user = User(id=1, name='ydc', age=20)
print(user.id)


# 值为list，key不存在自动给空list
groups = defaultdict(list)
data = [("a",1), ("b",2), ("a",3)]
for k,v in data:
    groups[k].append(v)

print(groups)


res = Counter([1,1,2,2,2,3])
print(res) # Counter({2: 3, 1: 2, 3: 1})

print(res[2]) # 获取计数
# most_common(n) 取topN
print(res.most_common(2)) # [(2, 3), (1, 2)]

# 两个Counter可以做加减运算，非常适合断言
c1 = Counter([1,2,2])
c2 = Counter([2,1,1,1])
res = c1 - c2
print(res)
