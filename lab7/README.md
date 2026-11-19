# Lab 7 – Fuzz Testing

**Student Name:** Rufus Thomas  
**SRN:** PES1UG24AM232

## Objective

Identify and fix input-validation bugs in the Recycling Rewards application using Hypothesis property-based fuzz testing.

## Application

`recycling_rewards.py`

## Test File

`test_recycling_rewards.py`

## Functions Tested

1. `parse_collection()`
2. `weight_average()`
3. `net_points()`

## Testing Tools

- Python
- Hypothesis
- pytest

## Testing Results

- Initial testing: 3 failed, 3 passed.
- After correction: 6 passed.

## Report

`PES1UG24AM232_LAB7_FuzzTesting_Report.pdf`

The PDF contains screenshots of the original application, failing fuzz tests, corrected application, and passing tests.