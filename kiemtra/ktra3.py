#bai6-----------------------------------------
character = {
    "Name": "Light",
    "Age": "17",
    "Streghth": "8",
    "Defense": "10",
    "HP": "100",
    "Backpack": "Shield, Bread Loaf",
    "Gold": "100",
    "Level": "2",
}
character["Gold"]+=50
print("Gold:",character["Gold"])
character["Backpack"].append("Shield, Bread,Loaf,FlintStone")
print("Backpack:",.join(character["Backpack"]))
