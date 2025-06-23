x = int(input())
words = []
for _ in range(x):
  word = input().split()
  words.append([ch[0] for ch in word])
for word in words:
  print(''.join(word))
