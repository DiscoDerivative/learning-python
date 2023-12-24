cat = "meow"
i = 0

while i < 3:
  print(cat)
  i += 1

cheese = ["cheddar", "gouda", "asiago"]
for x in cheese:
  if x == "gouda":
    continue
  print(x)

for x in "apple":
  print(x)


for x in range(5, 15, 3):
  print(x)
else: 
  print("Done")