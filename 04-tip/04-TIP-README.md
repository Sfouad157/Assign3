
# Tip Calculator

> And now for my Wizard tip calculator.
>
> — Morty Seinfeld

In the United States, it’s customary to leave a tip for your server after dining
in a restaurant, typically an amount equal to 15% or more of your meal’s cost. 

In tip.py, write a Python program that helps you calculate the correct amount to tip at a
restaurant. The program should ask you how much your meal cost and what
percentage you want to tip. Then, it will calculate the tip amount and tell you
how much to leave.

## Inputs

Prompt the user to enter the following information:

- Meal coast
    - Assume that the user will input only numeric values, such: `10` for $10.00
      or `25.43` for $25.43 (i.e., a float)
- Tip percent
    - Assume that the user will input only integer values, such: `10` for 10% or
      `15` for 15% (i.e., an int)

## Expected Output

- If you enter `100` for the meal `15` for the tip, your program should output
  exactly:
  ```
  A 15% tip on $100.0 is $15.0
  ```

- If you enter `45.62` for the meal `20` for the tip, your program should output
  exactly:
  ```
  A 20% tip on $45.62 is $9.124
  ```

> For now, we're just letting the decimal places run wild. The tip percent has
> zero places since it's an int. The meal and tip amounts have one or more
> digits after the decimal because they are floats. We'll learn the ins and outs
> of rounding and formatting and such later.

## Hints
- The tip amount is check amount times tip percent. BUT, remember that 15% is
  ACTUALLY 0.15.
- SO, the calculation is check amount times tip percent divided by 100.
- Don't forget about order of operations: PEMDAS.
- Recall that `input()` returns a `str`, per
  [docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input).
- Recall that `int()` can convert a `str` to a `int`, per
  [docs.python.org/3/library/functions.html#float](https://docs.python.org/3/library/functions.html#int).
- Recall that `float()` can convert a `str` to a `float`, per
  [docs.python.org/3/library/functions.html#float](https://docs.python.org/3/library/functions.html#float).
- Recall that concatenating an number value to a string requres that you convert
  the number to a string using the `str()` function. See [Python's documentation
  on str()](https://docs.python.org/3/library/functions.html#func-str).

## Source
- Adapted from CS50P
