#Write an algorithm that will calculate the amount of paint required to paint a room. The user will enter the dimensions of the room, the total dimensions of the unpaintable areas (such as windows, doors or brickwork) and the number of coats of paint required.

#Assume that 1 litre of paint covers 11 sq m.

#Using a bedroom for this project

rdim = int(input('Enter the total dimensions of your room (in sqm): '))
udim = int(input('Enter the total dimensions of your rooms unpaintable areas (in sqm): '))
coats = int(input('Enter the amount of coats of paint required: '))

# 1l of paint per bucket

tdim = rdim - udim
tpr = tdim/11
tpr = tpr * coats

print(f'The total amount of paint required is: {tpr}')
