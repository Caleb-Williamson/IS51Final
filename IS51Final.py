"""
This program calculates the number or grades, the average, and percentage of grades abouve average.

It does this by opening the file Final.txt and saving the scores in memory, then close the file. 
Next count the scores, print result.
Then, summ the scores and divide by the above count.
Lastly implement a loop that checks to see if each score is higher than the avg score. 
Then determine the percentage of scores that are above the average and display.

"""
"""
#calculate_percent_above_average function
def calculate_percent_above_average(ll,avg):
        cnt=0
        for a in ll:
                if(a>avg):
                        cnt+=1
        return ((cnt/len(ll))*100)

#main function

if __name__ == "__main__":
        opening python file
        f = open("Final.txt", "r")
        #spliting element by enter
        l=f.read().split("\n")
        ll = []
        for a in l:
                if(a!=''):
                        ll.append(int(a))
        #printing number of grades
        print("Number of grades : ",len(ll))

        calculate average grade
        avg=0
        for a in ll:
                avg+=a
        avg=avg/len(ll)
        print("Average of grades : ",avg)
        print("Percentage of grades above average: ",calculate_percent_above_average(ll,avg),"%")





"""




