import random

item = ["normal", "deal", "item option", "HH"]

# Get one random array from the 'item' list
# get_random_item = str(random_item)

# Print the randomly selected array
# print(random_item)


# if random_item == "normal":
#     print("this is a normal item")
# elif random_item == "deal":
#     print("this is a deal item")
# elif random_item == "item option":
#     print("this is a normal item with item option")
# elif random_item == "HH":
#     print("this is an HH item")

def mtNormalItem():
    return print("this is normal item")


def mtDealItem():
    return print("this is deal item")


def mtItemOption():
    return print("this is item option")


def mtHH():
    return print("this is HH item")


enumsample = {
    "normal": mtNormalItem,
    "deal": mtDealItem,
    "item option": mtItemOption,
    "HH": mtHH
}

for i in range(200):
    random_item = random.choice(item)
    enumsample[random_item]()

