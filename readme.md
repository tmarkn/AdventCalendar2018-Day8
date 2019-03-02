Advent Calendar 2018 Day 8
Written in Python

Stored the input as an array (stored in index 0) 
Used nodes with a value attribute and children array attribute (stored in index 1 when accessed)

Loop searches for a '0' in the array (the array has no more children)

if there is no node associated with it, value equals the sum up the meta data

if there is a node associated with it, try and add the value of the children in accordince to the meta data,

add current node to parent node,

then pop the current node and their metadata


Run loop until all values are popped

last value returned is the answer