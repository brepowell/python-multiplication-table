# Created by  Breanna Powell
# 3. Canvas Assignment - Loops
# 02/13/2021

#Write a program in python to display a multiplication table.
#Use Loops to print this table.

#Tips: You will need to use loops
#check when it gets to the last line (if statement) so that the code can continue printing on subsequent lines.
#Table goes from 1 to 10

#HEADER ROW FOR THE COLUMNS (JUST TO LOOK NICE!):
print('   x|  1|   2|   3|   4|   5|   6|   7|   8|   9| 10 | ')

#OUTER LOOP - ROWS (ADDED A LINE OF UNDERSCORES TO SEPARATE VISUALLY):
for a in range (1,11):
    if a < 10:
        print ('______________________________________________________\n',' ', a, end='|')
    if a == 10:
        print ('______________________________________________________\n',a , end=' |')

    #INNER LOOP - COLUMNS (ADDED VERTICAL LINES TO SEPARATE VISUALLY):
    for b in range (1,11):
        result = a * b
        # DECIDED TO EXPERIMENT WITH THE SPACING TO MAKE IT LOOK NICER):
        if result >= 10 and result < 100:
            print (result, end=' | ')
        if result < 10:
            print (' ',result, end='| ')
        if result == 100:
            print (result, end='|')
    print()