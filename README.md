# Tasks Python Strings Lists
Your task is to write programming code according to the requirements:
- your working directory is *src*;
- use files that are identified in the same way as tasks (functions); 
- write your solution within the appropriate functions;
- you may use different IDE, just copy paste your code to the files in repo;
- press 'commit changes' and check the tests


## Task 1. Is the Word Singular or Plural?
Create a function **is_plural()** that takes in a word and determines whether or not it is plural. A plural word is one that ends in "s".  
  
*Notes.* This is an oversimplification of the English language. We are ignoring edge cases like "goose" and "geese", "fungus" and "fungi", etc.  

*Examples*
```plaintext
is_plural("changes") ➞ True
is_plural("change") ➞ False
is_plural("dudes") ➞ True
is_plural("magic") ➞ False
```
    
## Task 2. Stuttering Function
Write a function **stutter()** that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis *...* and *space* after each, and then the word is pronounced with a question mark *?*.  
Assume all input is in lower case and at least two characters long.  

*Examples*
```plaintext
stutter("incredible") ➞ "in... in... incredible?"
stutter("enthusiastic") ➞ "en... en... enthusiastic?"
stutter("outstanding") ➞ "ou... ou... outstanding?"
```
    
## Task 3. Return the Index of All Capital Letters
Create a function **index_of_caps()** that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.  

*Notes.*
-  Return an empty list if no uppercase letters are found in the string.
-  Special characters ($#@%) and numbers will be included in some test cases.
-  Assume all words do not have duplicate letters.

*Examples*
```plaintext
index_of_caps("eQuINoX") ➞ [1, 3, 4, 6]
index_of_caps("determine") ➞ []
index_of_caps("STRIKE") ➞ [0, 1, 2, 3, 4, 5]
index_of_caps("sUn") ➞ [1]
```
    
## Task 4. Filter Strings from Array
Create a function **filter_list()** that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.

*Examples*
```plaintext
filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]
filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]) ➞ [0, 1729]
filter_list(["Nothing", "here"]) ➞ []
```

## Task 5. Alphabet Soup
Create a function **alphabet_soup()** that takes a string and returns a string with its letters in alphabetical order.
*Notes.*  
You can assume numbers and punctuation symbols won't be included in test cases. You'll only have to deal with single word, alphabetic characters.

*Examples*
```plaintext
alphabet_soup("hello") ➞ "ehllo"
alphabet_soup("hacker") ➞ "acehkr"
alphabet_soup("geek") ➞ "eegk"
alphabet_soup("javascript") ➞ "aacijprstv"
```

## Task 6. Probabilities
Given a *list of numbers* and a value *n*, write a function **probability()** that returns the probability of choosing a number greater than or equal to *n* from the list. The probability should be expressed as a percentage, rounded to one decimal place.
*Notes.*  
Percent probability of event = 100 * (num of favourable outcomes) / (total num of possible outcomes)

*Examples*
```plaintext
probability([5, 1, 8, 9], 6) ➞ 50.0
probability([7, 4, 17, 14, 12, 3], 16) ➞ 16.7
probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6) ➞ 70.0
```

## Task 7. Chat Room Status
Write a function **chatroom_status()** that returns the number of users in a chatroom based on the following rules:

- If there is no one, return "no one online".
- If there is 1 person, return "user1 online".
- If there are 2 people, return user1 and user2 online".
- If there are n>2 people, return the first two names and add "and n-2 more online".

For example, if there are 5 users, return:
```plaintext
"user1, user2 and 3 more online"
```

*Examples*
```plaintext
chatroom_status([]) ➞ "no one online"
chatroom_status(["paRIE_to"]) ➞ "paRIE_to online"
chatroom_status(["s234f", "mailbox2"]) ➞ "s234f and mailbox2 online"
chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"])
➞ "pap_ier44, townieBOY and 4 more online"
```

## Task 8. Nth Smallest Integer
Given an unsorted list, create a function **nth_smallest()** that returns the nth smallest integer (the smallest integer is the first smallest, the second smallest integer is the second smallest, etc).

*Notes.*  
- *n* will always be >= 1.
- Each number in the array will be distinct (there will be a clear ordering).
- Given an out of bounds parameter (e.g. a list is of size *k*), and you are asked to find the *m > k* smallest integer, return *None*.

*Examples*
```plaintext
nth_smallest([1, 3, 5, 7], 1) ➞ 1
nth_smallest([1, 3, 5, 7], 3) ➞ 5
nth_smallest([1, 3, 5, 7], 5) ➞ None
nth_smallest([7, 3, 5, 1], 2) ➞ 3
```

## Task 9. Date Format
Create a function **format_date()** that converts a date formatted as DD/MM/YYYY to YYYY-DD-MM.

*Notes.*  
Return value should be a string.

*Examples*
```plaintext
format_date("11/12/2019") ➞ "2019-12-11"
format_date("12/31/2019") ➞ "2019-31-12"
format_date("01/15/2019") ➞ "2019-15-01"
```

## Task 10. Stalactites or Stalagmites?
**Stalactites** hang from the ceiling of a cave while **stalagmites** grow from the floor.

Create a function **mineral_formation()** that determines whether the input represents *"stalactites"* or *"stalagmites"*. If it represents both, return *"both"*. Input will be a 2D list, with 1 representing a piece of rock, and 0 representing air space.

*Notes.*  
In other words, if the first list has 1s, return _"stalactites"_. If the last list has 1s, return _"stalagmites"_. If both have them, return _"both"_.

*Examples*
```plaintext
mineral_formation([
  [0, 1, 0, 1],
  [0, 1, 0, 1],
  [0, 0, 0, 1],
  [0, 0, 0, 0]
]) ➞ "stalactites"

mineral_formation([
  [0, 0, 0, 0],
  [0, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]) ➞ "stalagmites"

mineral_formation([
  [1, 0, 1, 0],
  [1, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]) ➞ "both"
```

## Task 11. Water Balloon
Once a water balloon pops, is soaks the area around it. The ground gets drier the further away you travel from the balloon.

The effect of a water balloon popping can be modeled using a list. Create a function **pops()** that takes a list which takes the pre-pop state and returns the state after the balloon is popped. The pre-pop state will contain at most a single balloon, whose size is represented by the only non-zero element.
*Notes.*  
- Length of input list is always odd.
- The input list will always be the exact length it takes for there to be exactly one border zero.
- If the input list consists only of zeroes, return the same list.

*Examples*
```plaintext
pops([0, 0, 0, 0, 4, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4, 3, 2, 1, 0]
pops([0, 0, 0, 3, 0, 0, 0]) ➞ [0, 1, 2, 3, 2, 1, 0]
pops([0, 0, 2, 0, 0]) ➞ [0, 1, 2, 1, 0]
pops([0]) ➞ [0]
```


## Task 12. Intersecting Intervals
Create a function **count_overlapping()** that takes in a list of intervals and returns how many intervals overlap with a given _point_.

An interval overlaps a particular point if the point exists inside the interval, or on the interval's boundary. For example the point 3 overlaps with the interval [2, 4] (it is inside) and [2, 3] (it is on the boundary).

To illustrate:
```plaintext
count_overlapping([[1, 2], [2, 3], [1, 3], [4, 5], [0, 1]], 2) ➞ 3
# Since [1, 2], [2, 3] and [1, 3] all overlap with point 2
```

*Notes.*  
- Each interval is represented as a list with a start point and an endpoint.
- Intervals count as intersecting even if they only intersect at one point, i.e. [2, 3] and [3, 4] both intersect at point 3.
- If it's helpful, you can draw these intervals on a line on a piece of paper.

*Examples*
```plaintext
count_overlapping([[1, 2], [2, 3], [3, 4]], 5) ➞ 0
count_overlapping([[1, 2], [5, 6], [5, 7]], 5) ➞ 2
count_overlapping([[1, 2], [5, 8], [6, 9]], 7) ➞ 2
```

## Task 13. Tallest Skyscraper
A city skyline can be represented as a 2-D list with 1s representing buildings. In the example below, the height of the tallest building is 4 (second-most right column).
```plaintext
[[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]]
```
Create a function **tallest_skyscraper()** that takes a _skyline_ (2-D list of 0's and 1's) and returns the height of the tallest skyscraper.

*Examples*
```plaintext
tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 3

tallest_skyscraper([
  [0, 1, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 4

tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [1, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 2
```

## Task 14. Sum of Prime Numbers
Create a function **sum_primes()** that takes a list of numbers and returns the sum of all prime numbers in the list.

_Notes_
- Given numbers won't exceed 101.
- A prime number is a number which has exactly two divisors.

_Examples_
```plaintext
sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 17
sum_primes([2, 3, 4, 11, 20, 50, 71]) ➞ 87
sum_primes([]) ➞ None
```

## Task 15. Sharing is Caring
Given a list of numbers, create a function **show_the_love()** that removes 25% from every number in the list except the smallest number, and adds the total amount removed to the smallest number.

_Notes_
- There will only be one smallest number in a given list.

_Examples_
```plaintext
show_the_love([4, 1, 4]) ➞ [3, 3, 3]
show_the_love([16, 10, 8]) ➞ [12, 7.5, 14.5]
show_the_love([2, 100]) ➞ [27, 75]
```



