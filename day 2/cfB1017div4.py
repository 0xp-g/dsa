ls = []
x = int(input())
for _ in range(x):
   ls.append(list(map(int, input().split())))
for n, m, ll, rl in ls:
   count =r = l = 0
   while count < m:
      if count % 2 == 0 and r < rl:
         r += 1
      elif l > ll:
         l -= 1
      count += 1
   print(l, r)