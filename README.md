# Simple Error Sample Repository

A simple demonstration repository containing intentional errors/bugs for testing debuggers, linters, or CI/CD pipelines.

## Code with Errors

The repository contains `app.py` with intentional runtime errors:

1. **`ZeroDivisionError`**: `calculate_average([])` divides by `len(numbers)` which is 0 when the list is empty.
2. **`TypeError`**: `"Result: " + avg` attempts to concatenate string with a float without type casting.

## How to Reproduce

Run the script using Python:

```bash
python app.py
```

### Expected Output
```text
Running buggy application...
Calculating average:
Traceback (most recent call last):
  File "app.py", line 22, in <module>
    main()
  File "app.py", line 17, in main
    avg = calculate_average(numbers)
  File "app.py", line 6, in calculate_average
    return total / len(numbers)
ZeroDivisionError: division by zero
```
