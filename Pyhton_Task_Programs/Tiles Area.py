Area1_width = int(input("Enter width of area1 : ")) #Taking an input from user
Area1_length = int(input("Enter length of area1 : "))
Area1 = Area1_width * Area1_length
print("Area1 is :",Area1)

Area2_width = int(input("\nEnter width of area2 : "))
Area2_length = int(input("Enter length of area2 : "))
Area2 = Area2_width * Area2_length
print("Area2 is :",Area2)

Total = Area1 + Area2 # 1. How many tiles are needed?
print("\nTotal tiles are :",Total)
print("There are 98 tiles needed.\n")

Tiles = (17 * 6) # 2.You buy 17 packages of tiles containing 6 tiles each.
print("Tiles are :",Tiles)
print("You buy 17 packages of tiles containing 6 tiles each.\n")

Left_Tiles = Tiles - Total # 2. How many tiles will be left over? 
print("Left tiles are :",Left_Tiles)




