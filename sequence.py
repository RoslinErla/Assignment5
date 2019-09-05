#Design an algorithm that generates the first n numbers 
# in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …


n = int(input("Enter the length of the sequence: ")) # Do not change this line
#We know the first three integers so we put them as a start.
first=1
second =2
third =3 


for i in range (n):
    if i==0:
        print(first)
    if i==1:
        print(second)
    if i == 2:
        print(third)
    if i >= 3:
        #We know that the sequence works by adding together the three integers before so we calculate that.
        #Then we update the variables first, second, and third. Now all of them move up. The second integer is now the first
        #the third integer is now the second, and the fourth integer is now the third. 
        fourth= first+second+third
        first=second
        second=third
        third=fourth
        print(fourth)