# Iterations / Looping over a collection of values

## Looping over a list
ninjutsu_styles = ["Katon", "Raiton", "Doton", "Suiton", "Futon"]

for ninjustu_style in ninjutsu_styles:
    print(ninjustu_style)

print("-"*100)

## Looping over a set(list)
ninjutsu_styles = set(["Katon", "Raiton", "Doton", "Suiton", "Futon"])

for ninjustu_style in ninjutsu_styles:
    print(ninjustu_style)

print("-"*100)

## Looping over a dictionary
ninjutsu_styles = {
    "Katon":"Fire Style", "Raiton":"Lightning Style", "Doton": "Earth Style", "Suiton":"Water Style", "Futon":"Wind Style"
}

for k,v in ninjutsu_styles.items():
    print(f"{k} from Japanese is translated as {v} in English")