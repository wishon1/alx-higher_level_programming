* Project: 0x09. Python - Everything is object

* Resources
 - Read or watch:

+ [ Objects and values](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values)
+ [Aliasing](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing)
+ [Immutable vs mutable types](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)
+ [Mutation (Only this chapter](https://www.composingprograms.com/pages/24-mutable-data.html)
+ [Cloning lists](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists)
+ [Python tuples: immutable but potentially changing](http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html)

* Requirements
* Python Scripts
+ Allowed editors: vi, vim, emacs
+ All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
+ All your files should end with a newline character
+ The first line of all your script files should be exactly #!/usr/bin/python3
+  A README.md file, at the root of the folder of the project, is mandatory
+ Your code should use the pycodestyle (version 2.8.*)
+ All your files must be executable
+ The length of your files will be tested using wc
+ .txt Answer Files
+ Only one line
+ No Shebang
+ All your files should end with a new line

Tasks
0. Who am I?
+ What function would you use to get the type of an object?
+ Write the name of the function in the file, without ().
+ File: 0-answer.txt

1. Where are you?
+ How do you get the variable identifier (which is the memory address in the CPython implementation)?
+ Write the name of the function in the file, without ().
+ File: 1-answer.txt

2. Right count
+ In the following code, do a and b point to the same object? Answer with Yes or No.
+ >>> a = 89
  >>> b = 100
+ File: 2-answer.txt

3. Right count
+ In the following code, do a and b point to the same object? Answer with Yes or No.
  >>> a = 89
  >>> b = 89
+ File: 3-answer.txt

4. Right count
+ In the following code, do a and b point to the same object? Answer with Yes or No.
  >>> a = 89
  >>> b = a
+ File: 4-answer.txt

5. Right count
+ In the following code, do a and b point to the same object? Answer with Yes or No.
 >>> a = 89
 >>> b = a + 1
+ File: 5-answer.txt

6. What do these 3 lines print?
 >>> s1 = "Best School"
 >>> s2 = s1
 >>> print(s1 == s2)
+ File: 6-answer.txt

7. Is the same man
 >>> s1 = "Best"
 >>> s2 = s1
 >>> print(s1 is s2)
+ File: 7-answer.txt

8. Is really equal
+ What do these 3 lines print?
 >>> s1 = "Best School"
 >>> s2 = "Best School"
 >>> print(s1 == s2)
+ File: 8-answer.txt

9. Is really the same
+ What do these 3 lines print?
 >>> s1 = "Best School"
 >>> s2 = "Best School"
 >>> print(s1 is s2)
+ File: 9-answer.txt

10. And with a list, is it equal
+ What do these 3 lines print?
 >>> l1 = [1, 2, 3]
 >>> l2 = [1, 2, 3] 
 >>> print(l1 == l2)
+ File: 10-answer.txt

11. And with a list, is it the same
+ What do these 3 lines print?
 >>> l1 = [1, 2, 3]
 >>> l2 = [1, 2, 3] 
 >>> print(l1 is l2)
+ File: 11-answer.txt

12. And with a list, is it really equal
+ What do these 3 lines print?
 >>> l1 = [1, 2, 3]
 >>> l2 = l1
 >>> print(l1 == l2)
+ File: 12-answer.txt

13. And with a list, is it really the same
+ What do these 3 lines print?
 >>> l1 = [1, 2, 3]
 >>> l2 = l1
 >>> print(l1 is l2)
+ File: 13-answer.txt

14. List append
+ What does this script print?
+ l1 = [1, 2, 3]
+ l2 = l1
+ l1.append(4)
+ print(l2)
+ File: 14-answer.txt

15. List add
What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
+ File: 15-answer.txt

16. Integer incrementation
+ What does this script print?
def increment(n):
    n += 1
    a = 1
increment(a)
print(a)
+ File: 16-answer.txt

17. List incrementation
What does this script print?

def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
+ File: 17-answer.txt

18. List assignation
+ What does this script print?

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
+ File: 18-answer.txt

19. Copy a list object
+ Write a function def copy_list(l): that returns a copy of a list.
+ The input list can contain any type of objects
+ Your file should be maximum 3-line long (no documentation needed)
+ You are not allowed to import any module
+ File: 19-copy_list.py

20. Tuple or not?
+ a = ()
+ Is a a tuple? Answer with Yes or No.
+ File: 20-answer.txt

21. Tuple or not?
+ a = (1, 2)
+ Is a a tuple? Answer with Yes or No.
+ File: 21-answer.txt

22. Tuple or not?
+ a = (1)
+ Is a a tuple? Answer with Yes or No.







