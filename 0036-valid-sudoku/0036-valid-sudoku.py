class Solution(object):
    def isValidSudoku(self, board):
        #Create row sets , their will be 9 sets
        #row[0] = {}
        #row[1] = {}
        #and so on

        rows = [set() for _ in range(9)]
        #Create column sets same principle as the rows 
        columns = [set() for _ in range(9)]

        #Create box sets same principle
        boxes = [set() for _ in range(9)]

        #Visit evey cell
        #loop through each row
        for row in range(9):
            #loop through columns
            for column in range(9):

            #Read current value 
                value = board[row][column]

            #Ignore empty cells
                if value == ".":
                    continue
            
            #Computer the box number to determine which of the 9 boxes this cell belongs to 

                box = ((row // 3) * 3 + (column // 3))

            #If the number is already seen in the current row the board is invalid 

                if value in rows[row]:
                    return False 

            #If the number is already seen in the current column the board is invalid 

                if value in columns[column]:
                    return False 

            #if the number has already been seen in the 3 x 3 box the board is invalid 

                if value in boxes[box]:
                    return False

            #Store the number in the row 
                rows[row].add(value)

            #Store the number in the column 

                columns[column].add(value)

            #Store the number in the box 

                boxes[box].add(value)
        #No duplicates !! Yay 
        return True

        