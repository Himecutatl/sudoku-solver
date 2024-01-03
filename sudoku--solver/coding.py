board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]


def solve(bo): #recursive function to implement backtracking
    find = find_empty(bo)
    if not find:
        return True #if all 0's are filled, we are done. This is the base case of recursion 
    else:
        row, col = find

    for i in range(1,10): #goes through values 1-9 inclusively
        if valid(bo, i, (row, col)):
            bo[row][col] = i #Function will loop through values 1 to 10 then make sure that if we add them to the board that they're a valid solution; if solution is valid it will add it into the board

            if solve(bo): #recursively try to solve problem by calling 'solve' on new board and keep trying until solution found or until all numbers looped through and none valid and return False and resetting loop. Essentially if we can't finish solution based on the value we added, keep trying
                return True
            
            bo[row][col] = 0
    return False



def valid(bo, num, pos): #Takes 3 params: board, number and position. Needs to check row, column and position that we're in
    #Checks row
    for i in range(len(bo[0])): 
        if bo[pos[0]][i] == num and pos[1] != i: #Checks each element in the row, seeing if its equal to the number we just input; code after 'and' portion omits check if it's the position we just input into
            return False

    #Checks column
    for i in range(len(bo[0])): 
        if bo[i][pos[1]] == num and pos[0] != i: 
            return False
        
    #Checks which box we're in
    box_x = pos[1] // 3 
    box_y= pos[0] // 3

    for i in range(box_y * 3, box_y*3 + 3): #We are multipying by 3 bc box_x and y are expecting return values of 0, 1 or 2 and since there are 9 elements in each row/column thats how it will find the index
            for j in range(box_x * 3, box_x*3 + 3):
                if bo[i][j] == num and (i,j) != pos: #Will check if elements in box are = to value we just input
                    return False

    return True

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0: 
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")



def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) #returns row, columns
            
    return None #if there are no blank squares left, return None so the 'solve' function can verify the base/True case

print_board(board)
solve(board)
print("___________________________________")
print_board(board)

