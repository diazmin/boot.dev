'''
You can print the results using list(range(...)):

- Create a list of numbers from 0 to 9.
- Create a list of even numbers from 2 to 20.
- Create a list of odd numbers from 1 to 19.
- Create a list of numbers from 10 down to 1.
- Create a list of every third number from 3 to 30.
- Create a list of numbers from 100 to 80, decreasing by 5.
- Create a list of all multiples of 4 from 0 to 40.

1. Numbers from 5 to 15 (inclusive).
2. All even numbers from 50 down to 30.
3. All numbers from -10 to 10.
4. Every 5th number from 0 to 100.
5. All odd numbers between 1 and 20, excluding 1 and 20.
6. A countdown from 10 to 1, then print "Liftoff! 🚀"
7. Create a list of the first 8 multiples of 7.
8. Print every third number from 100 down to 40.
9. All the perfect squares less than 100 (hint: use a range of square roots and square them).
10. Create a list of numbers between 1 and 50 that are divisible by both 3 and 4.
'''

def range_practice():
    print(f"list of number from 0 to 9: {list(range(0, 10))}")
    print(f"even numbers from 2 to 20: {list(range(2, 21, 2))}")
    print(f"odd numbers from 1 to 19: {list(range(1, 20, 2))}")
    print(f"numbers from 10 down to 1: {list(range(10, 0, -1))}")
    print(f"numbers of every third number from 3 to 30: {list(range(3, 31, 3))}")
    print(f"numbers from 100 to 80, decreasing by 5: {list(range(100, 79, -5))}")
    print(f"numbers fmultiples of 4 from 0 to 40: {list(range(0, 41, 4))}")

range_practice()