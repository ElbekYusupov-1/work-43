# ================= ARRAY25 =================
# Geometrik progressiya tekshirish
n = int(input("n: "))
a = list(map(int, input("Massiv: ").split()))

q = a[1] / a[0] if a[0] != 0 else None
is_gp = True

for i in range(1, n):
    if a[i-1] == 0 or a[i] / a[i-1] != q:
        is_gp = False
        break

print(0 if is_gp else q)


# ================= ARRAY26 =================
# Juft va toq ketma-ket kelishini tekshirish
for i in range(1, n):
    if (a[i] % 2) == (a[i-1] % 2):
        print(i)
        break
else:
    print(0)


# ================= ARRAY27 =================
# Musbat va manfiy ketma-ket
for i in range(1, n):
    if (a[i] > 0 and a[i-1] > 0) or (a[i] < 0 and a[i-1] < 0):
        print(i)
        break
else:
    print(0)


# ================= ARRAY28 =================
# Juft indekslar min
print(min(a[0:n:2]))


# ================= ARRAY29 =================
# Toq indekslar max
print(max(a[1:n:2]))


# ================= ARRAY30 =================
# O‘ng qo‘shnisidan katta indekslar
res = [i for i in range(n-1) if a[i] > a[i+1]]
print(len(res), res)


# ================= ARRAY31 =================
# Chap qo‘shnisidan katta indekslar
res = [i for i in range(1, n) if a[i] > a[i-1]]
print(len(res), sorted(res, reverse=True))


# ================= ARRAY32 =================
# Birinchi lokal minimum
for i in range(1, n-1):
    if a[i] < a[i-1] and a[i] < a[i+1]:
        print(i)
        break


# ================= ARRAY33 =================
# Oxirgi lokal maksimum
for i in range(n-2, 0, -1):
    if a[i] > a[i-1] and a[i] > a[i+1]:
        print(i)
        break


# ================= ARRAY34 =================
# Lokal minimumlar ichida eng kattasi
mins = [a[i] for i in range(1, n-1) if a[i] < a[i-1] and a[i] < a[i+1]]
print(max(mins) if mins else 0)


# ================= ARRAY35 =================
# Lokal maksimumlar ichida eng kichigi
maxs = [a[i] for i in range(1, n-1) if a[i] > a[i-1] and a[i] > a[i+1]]
print(min(maxs) if maxs else 0)


# ================= ARRAY36 =================
# Lokal min/max bo‘lmaganlar ichida max
lokal = set(i for i in range(1, n-1) if (a[i] < a[i-1] and a[i] < a[i+1]) or (a[i] > a[i-1] and a[i] > a[i+1]))
oddiy = [a[i] for i in range(n) if i not in lokal]
print(max(oddiy) if oddiy else 0)


# ================= ARRAY37 =================
# Monoton o‘suvchi oraliqlar soni
count = 0
i = 0
while i < n-1:
    if a[i] < a[i+1]:
        count += 1
        while i < n-1 and a[i] < a[i+1]:
            i += 1
    else:
        i += 1
print(count)


# ================= ARRAY38 =================
# Monoton kamayuvchi oraliqlar
count = 0
i = 0
while i < n-1:
    if a[i] > a[i+1]:
        count += 1
        while i < n-1 and a[i] > a[i+1]:
            i += 1
    else:
        i += 1
print(count)


# ================= ARRAY39 =================
# Har ikkala
# (array37 + array38)
# yuqoridagi ikkalasini qo‘shib ishlat


# ================= ARRAY40 =================
# R ga eng yaqin son
R = int(input("R: "))
print(min(a, key=lambda x: abs(x - R)))


# ================= ARRAY41 =================
# Eng katta yig‘indi qo‘shnilar
max_sum = a[0] + a[1]
pair = (a[0], a[1])

for i in range(1, n-1):
    if a[i] + a[i+1] > max_sum:
        max_sum = a[i] + a[i+1]
        pair = (a[i], a[i+1])

print(pair)


# ================= ARRAY42 =================
# R ga eng yaqin yig‘indi
best = (a[0], a[1])
min_diff = abs(a[0] + a[1] - R)

for i in range(1, n-1):
    diff = abs(a[i] + a[i+1] - R)
    if diff < min_diff:
        min_diff = diff
        best = (a[i], a[i+1])

print(best)


# ================= ARRAY43 =================
# Har xil elementlar soni
print(len(set(a)))


# ================= ARRAY44 =================
# 2 ta bir xil element indekslari
seen = {}
for i in range(n):
    if a[i] in seen:
        print(seen[a[i]], i)
        break
    seen[a[i]] = i
    
# ================= ARRAY45 =================
# Bir-biriga eng yaqin qo‘shni elementlar indekslari
# (ya'ni |a[i] - a[i+1]| eng kichik bo‘lsa)

min_diff = abs(a[0] - a[1])
index = 0

for i in range(1, n-1):
    diff = abs(a[i] - a[i+1])
    if diff < min_diff:
        min_diff = diff
        index = i

print(index, index + 1)