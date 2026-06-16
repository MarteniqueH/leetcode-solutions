class Solution(object):
    def convert(self, s, numRows):
        #if their is only 1 row or if the rows are more than the letters 

        if numRows == 1 or numRows >= len(s):
            return s

        #Now creating empty strings (spots) for each row

        rows = ["" for _ in range(numRows)]

        #Start at row 0 which is the top row 

        current_row = 0

        #this is the direction switch
        #False = we are going upward or starting direction setup
        #This will flip when needed

        going_down = False

        #Looping through the string one letter at a time 

        for char in s:

            #Put the current letter into the correct row

            rows[current_row] += char

            #Bounce back logic
            #If the top row (0) is reached or the bottom row (numRows - 1)
            #If at the top go down and if at the bottom go up

            if current_row == 0 or current_row == numRows - 1:

                #This flips the direction
                going_down = not going_down

            if going_down: 
                #Move to the next row below current row
                current_row += 1
            else: 
                #Move back up one row
                current_row -= 1

        #This takes all the rows and puts them together into one string
        return "".join(rows)



        