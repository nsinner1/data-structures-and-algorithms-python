# data-structures-and-algorithms-python

## Reverse an Array

## Challenge
- Write a function called reverseArray which takes an array as an argument. Without utilizing any of the built-in methods available to your language, return an array with elements in reversed order.
## Approach & Efficiency
- Takes users data for the array they want to fill 
- While loop that remains infinite as long as two requirements are meant 
- While loop so the user can add as many things to the index as they want next we reverse the array by a slice method by taking the array filled with the user input data and prints it backwards
## Solution
- While loop to populate the array with inputs and uses a slice method that reverses the array so that the data that is appended shows up backwards

[Whiteboard](/Users/nataliesinner/codefellows/401/data-structures-and-algorithms-python/assets/array_reverse.jpeg)

## Array Shift

## Challenge
- Write a function called insertShiftArray which takes in an array and the value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.
## Approach & Efficiency
- My approach was to allow the user to pick the item they want inserted in middle of the array then found the midpoint and inserted them between the index numbers
## Solution
- Find midpoint in array then insert the item you want in the middle of the array
[Whiteboard](/Users/nataliesinner/codefellows/401/data-structures-and-algorithms-python/assets/array_shift.jpeg)

## Array Binary Search

## Challenge
- Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the search key, or -1 if the element does not exist.
## Approach & Efficiency
- My approach was to allow the user to pick a number and be able to tell if that number was in the array by showing a 2 if it was and a -1 if it was not. 
## Solution
- Find if user picked number that was in array by showing 2 if it is and -1 if it is not. 
[Whiteboard/Google Doc](https://docs.google.com/document/d/1sBieMTDNo6zWNvBqY8s-5npQkK0uGUZemvrp6tvqasE/edit?usp=sharing) 

# Singly Linked List

## Challenge
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.

## Approach & Efficiency
I followed the demo code and worked off of that. 

## API
<!-- Description of each method publicly available to your Linked List -->

# Merge two linked lists
- Merge teo linked list together. 

## Challenge Description
- Write a function called mergeLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. Try and keep additional space down to O(1). You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Approach & Efficiency
- My approach was to merge two linked list together to create one new linked list. Time = O(n); space = O(n)

## Solution
![Whiteboard](assets/Challenge08.png)

# Stacks and Queues
Python: a folder named stacks_and_queues which contains a file called stacks_and_queues.py

## Challenge
Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
Create a Stack class that has a top property. It creates an empty Stack when instantiated.
This object should be aware of a default empty value assigned to top when the stack is created.
Define a method called push which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
Define a method called pop that does not take any argument, removes the node from the top of the stack, and returns the node’s value.
Should raise exception when called on empty stack
Define a method called peek that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.
Should raise exception when called on empty stack
Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the stack is empty.
Create a Queue class that has a front property. It creates an empty Queue when instantiated.
This object should be aware of a default empty value assigned to front when the queue is created.
Define a method called enqueue which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
Define a method called dequeue that does not take any argument, removes the node from the front of the queue, and returns the node’s value.
Should raise exception when called on empty queue
Define a method called peek that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.
Should raise exception when called on empty queue
Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the queue is empty.
Be sure to follow your languages best practices for naming conventions.
You have access to the Node class and all the properties on the Linked List class.

Structure and Testing
Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write tests to prove the following functionality:

Can successfully push onto a stack
Can successfully push multiple values onto a stack
Can successfully pop off the stack
Can successfully empty a stack after multiple pops
Can successfully peek the next item on the stack
Can successfully instantiate an empty stack
Calling pop or peek on empty stack raises exception
Can successfully enqueue into a queue
Can successfully enqueue multiple values into a queue
Can successfully dequeue out of a queue the expected value
Can successfully peek into a queue, seeing the expected value
Can successfully empty a queue after multiple dequeues
Can successfully instantiate an empty queue
Calling dequeue or peek on empty queue raises exception
Ensure your tests are passing before you submit your solution.

## Approach & Efficiency
O(1) for both Stacks and Queues.

## API
<!-- Description of each method publicly available to your Stack and Queue-->
