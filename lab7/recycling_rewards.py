
import math


def parse_collection(text):
    """Parse material and weight from a material:weight string."""

    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    if text.count(":") != 1:
        raise ValueError("Input must contain exactly one ':'")

    material, kg = text.split(":")
    material = material.strip()

    if not material:
        raise ValueError("Material cannot be empty")

    try:
        kg = float(kg.strip())
    except ValueError:
        raise ValueError("Weight must be a valid number")

    if not math.isfinite(kg) or kg < 0:
        raise ValueError("Weight must be finite and non-negative")

    return material.title(), kg


def weight_average(weights_csv):
    """Calculate the integer average of comma-separated weights."""

    if not isinstance(weights_csv, str):
        raise ValueError("Input must be a string")

    parts = weights_csv.split(",")

    if any(not part.strip() for part in parts):
        raise ValueError("Weight list cannot be empty")

    try:
        values = [int(part.strip()) for part in parts]
    except ValueError:
        raise ValueError("All weights must be integers")

    if any(value < 0 for value in values):
        raise ValueError("Weights cannot be negative")

    return sum(values) // len(values)


def net_points(text):
    """Calculate net reward points after applying a penalty."""

    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    if text.count("|") != 1:
        raise ValueError("Input must contain exactly one '|'")

    points, penalty = text.split("|")

    try:
        points = float(points.strip())
        penalty = float(penalty.strip())
    except ValueError:
        raise ValueError("Points and penalty must be valid numbers")

    if not math.isfinite(points) or not math.isfinite(penalty):
        raise ValueError("Values must be finite")

    if points < 0 or penalty < 0:
        raise ValueError("Points and penalty cannot be negative")

    total = points * 2 - penalty

    return max(total, 0)


def main():
    print("==== Running parse_collection ====")
    user_input = input(
        "Enter material:weight in kg (e.g. paper:12): "
    )
    result = parse_collection(user_input)
    print("Material and Weight:", result)

    print("\n==== Running weight_average ====")
    user_input = input(
        "Enter weights in kg as CSV (e.g. 5,12,20): "
    )
    result = weight_average(user_input)
    print("Average Weight:", result)

    print("\n==== Running net_points ====")
    user_input = input(
        "Enter points|penalty (e.g. 80|10): "
    )
    result = net_points(user_input)
    print("Net Points:", result)


if __name__ == "__main__":
    main()
