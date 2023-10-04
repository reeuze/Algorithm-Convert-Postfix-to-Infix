Subject : Data structure and algorithm Assesment #5

Create a program that will change from infix to postfix.
This is the example of Infix convert to Postfix :

![alt text](https://github.com/reeuze/Algorithm-Convert-Postfix-to-Infix/blob/main/Image/Postfix%20to%20Infix.jpg?raw=true)

The Algorithm :
1. Convert the input from string to stack
2. Check the elements in the input stack one by one
3. If the element is an operator +,-,*,/, or ^; then combine it with the previous 2 numbers
4. Continue doing this until the length of the input stack is equal to 1
5. Display the input stack in string form as the final result