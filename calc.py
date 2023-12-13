
# konvertē datu mērvienības
def megabit_to_megabyte(megabit):
   megabyte = megabit * 8
   return megabyte

# saskaiti degvielas patēriņu uz 100 km
def fuel_consumption(litres, kilometers):
   result = 100 / kilometers * litres
   return result

# konvertē temperatūru
def celsius_to_fahrenheit(celsius):
    result = 9/5 * celsius + 32
    return result

# saliec visus skaitļus pirms dota skaitļa (izmanto for)
def sigma(tail):
    num = 0
    for i in range(tail):
        num = num + i
    return num + tail

# nokonvertē svaru uz tuvāko mērvienību - grams, kilograms, tonna (izmanto if)
def weight(grams):
    if grams > 1000 and grams < 99999:
        grams = grams / 1000
        return str(int(grams)) + "kg"
    elif grams > 100000 and grams < 999999:
        grams = grams / 100000
        return str(int(grams)) + "c"
    elif grams > 1000000:
        grams = grams / 1000000
        return str(int(grams)) + "t"
    else:
        return str(int(grams)) + "g"