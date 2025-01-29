# Python: Handling Non-Numeric Elements in Average Calculation

This repository demonstrates a common error in Python when calculating the average of a list that may contain non-numeric elements. The code attempts to calculate the average of a list, and it handles an empty list, but it doesn't gracefully handle non-numeric elements. The solution shows how to implement robust error handling to prevent this error.

## Bug

The `calculate_average` function does not check if the list contains non-numeric elements before attempting to calculate the average. This leads to a `TypeError` if the list contains non-numeric values.

## Solution

The solution addresses this by using a `try-except` block to catch the `TypeError` and handle it appropriately, either by returning an error message or providing alternative handling.
