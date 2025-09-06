# Arrays / Basic Array Operations

## `len()`

ninjas = ["Kakashi Hatake", "Tobirama Senju", "Minato Namikaze", "Itachi Uchiha", "Madara Uchiha"]

print(len(ninjas))

## indexing

hokages = ninjas[:3]
print(hokages)

## repitition

print(["Naruto Uzumaki"]*10)

## concatenation

konoha = ["Tobirama Senju", "Hashirama Senju"] + ["Madara Uchiha"]
print(konoha)

## subset `in` operation

uchihas = ["Itachi", "Madara", "Obito", "Sasuke", "Shishui", "Fugaku"]
print("Sasuke" in uchihas)