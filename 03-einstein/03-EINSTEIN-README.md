# Einstein

Even if you haven’t studied physics (recently or ever!), you might have heard
that $ E=mc^2 $, wherein $ E $ represents energy (measured in Joules), $ m $
represents mass (measured in kilograms), and $ c $ represents the speed of light
(measured approximately as 300,000,000 meters per second), per [Albert
Einstein](https://en.wikipedia.org/wiki/Albert_Einstein) et al. Essentially, the
formula means that mass and energy are equivalent.

In the file called `einstein.py`, implement a program in Python that prompts the
user for mass as an integer (in kilograms) and then outputs the equivalent
number of Joules as an integer.

## Input

Prompt the user for mass as an integer (in kilograms). Something like:

```
Enter mass in kilograms:
```

## Expected Output

Calculate and output E in the form `E: value`. For example:

- If you type `1` and press Enter. Your program should output:
  ```
  E: 90000000000000000
  ```
- If you type `14` and press Enter. Your program should output:
  ```
  E: 1260000000000000000
  ```
- If you type `50` and press Enter. Your program should output:
  ```
  E: 4500000000000000000
  ```

## Hints
- Recall that $ mc^2 $ is simply m * c * c.
- Recall that `input` returns a `str`, per [Python's documentation on
  input](https://docs.python.org/3/library/functions.html#input).
- Recall that `int()` can convert a `str` to an `int`, per [Python's
  documentation on int](https://docs.python.org/3/library/functions.html#int).
- Recall that concatenating an number value to a string requres that you convert
  the number to a string using the `str()` function. See [Python's documentation
  on str()](https://docs.python.org/3/library/functions.html#func-str).

## Source

Adapted from CS50P