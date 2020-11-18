n = input()
k = input()
a = [0 for x in range(int(n)*int(k))]
x = 0
for x in range(0, int(n)*int(k)):
    a[x] = input()
    x = x+1
mp = round((int(n))/2)
mp = mp - 1
x = 0
y = 0
top = 0
end = (int(n)*int(k))
end = end - 1
b = [[0 for x in range(int(n))]for y in range(int(k))]
x = 0
y = 0
for x in range(0, int(k)):
    for y in range(0, int(n)):
        if y < mp:
            b[y][x] = a[top]
            top = top+1
        else:
            b[y][x] = a[end]
            end = end - 1
        y = y+1
    x = x+1
x = 0
sum = 0
for x in range(0, int(k)):
    sum = sum + int(b[mp][x])
    print(b[x][mp])
print(sum)