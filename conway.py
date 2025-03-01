import copy, random, time, os

#function to clear screen
def clear_screen():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

#fixing the height and width of our display
WIDTH = 10
HEIGHT = 10

#intializing the list which will display the data
nextCells =[]

#filling the cells randomly with either "#" or " "
for h in range(HEIGHT):
    #new row
    row = []
    for w in range(WIDTH):
        #filling the data column-wise
        if random.randint(0,1) == 0:
            #live cells
            row.append("[*]")
        else:
            #dead cells
            row.append("[ ]")
    #adding the columns to list
    nextCells.append(row)


while True:
    currentCells = copy.deepcopy(nextCells)
    clear_screen()
    for h in range(HEIGHT):
        for w in range(WIDTH):
            print(currentCells[h][w],end="")
        print()
    print('\n\n\n\n')
    for h in range(HEIGHT):
        for w in range(WIDTH):
            leftCoord  = (w-1) % WIDTH
            rightCoord = (w+1) % WIDTH
            aboveCoord = (h-1) % HEIGHT
            belowCoord = (h+1) % HEIGHT

            liveNeighbours = 0
            if currentCells[aboveCoord][leftCoord]== '[*]': #top-left
                liveNeighbours += 1
            if currentCells[aboveCoord][w] == '[*]': #top
                liveNeighbours += 1
            if currentCells[aboveCoord][rightCoord] == '[*]': #top-right
                liveNeighbours += 1
            if currentCells[h][leftCoord] == '[*]': #left
                liveNeighbours += 1
            if currentCells[h][rightCoord] == '[*]': #right
                liveNeighbours += 1
            if currentCells[belowCoord][leftCoord] == '[*]': #bottom-left
                liveNeighbours += 1
            if currentCells[belowCoord][w] == '[*]': #bottom
                liveNeighbours += 1
            if currentCells[belowCoord][rightCoord] == '[*]': #bottom-right
                liveNeighbours += 1



            #setting the cells for next iteration

            if currentCells[h][w]=="[*]" and (liveNeighbours==3 or liveNeighbours==2):
                nextCells[h][w]="[*]"

            elif currentCells[h][w]=="[ ]" and (liveNeighbours==3):
                nextCells[h][w]="[*]"

            else:
                nextCells[h][w]="[ ]"
    time.sleep(1)