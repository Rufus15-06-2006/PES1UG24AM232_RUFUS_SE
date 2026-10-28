"""Flight reservation system with improved quality and security."""

import hashlib
import json
import os
import secrets

FLIGHTS = {
    "AI101": {
        "destination": "London",
        "seats": 2,
        "fare": 450.0,
        "is_full": False,
    },
    "BA202": {
        "destination": "New York",
        "seats": 0,
        "fare": 600.0,
        "is_full": True,
    },
    "EK303": {
        "destination": "Dubai",
        "seats": 5,
        "fare": 320.0,
        "is_full": False,
    },
}

REVENUE = {"total": 0.0}


def book_flight_seat(
    flight_no, passenger, luggage_weight=15, baggage_tags=None
):
    """Book an available seat and record the booking."""
    if baggage_tags is None:
        baggage_tags = []

    flight = FLIGHTS.get(flight_no)
    if flight is None or flight["is_full"]:
        return False

    flight["seats"] -= 1
    if flight["seats"] <= 0:
        flight["is_full"] = True

    REVENUE["total"] += flight["fare"]
    baggage_tags.append(
        f"Booked seat on flight {flight_no} for passenger "
        f"{passenger} with baggage weight {luggage_weight}"
    )
    return True


def cancel_booking(flight_no):
    """Cancel a booking for a valid flight."""
    flight = FLIGHTS.get(flight_no)
    if flight is None:
        return False

    flight["seats"] += 1
    flight["is_full"] = False
    return True


def check_seat_availability(flight_no):
    """Return whether a flight has seats available."""
    flight = FLIGHTS.get(flight_no)
    return flight is not None and not flight["is_full"]


def calculate_baggage_fee(flight_no, surcharge_rate):
    """Calculate a baggage surcharge using a numeric rate."""
    flight = FLIGHTS.get(flight_no)
    if flight is None:
        raise ValueError(f"Unknown flight number: {flight_no}")

    if not isinstance(surcharge_rate, (int, float)):
        raise TypeError("Surcharge rate must be numeric.")

    if not 0 <= surcharge_rate <= 1:
        raise ValueError("Surcharge rate must be between 0 and 1.")

    return flight["fare"] * surcharge_rate


def generate_passenger_hash(passenger_id):
    """Generate a SHA-256 digest for a passenger identifier."""
    return hashlib.sha256(passenger_id.encode("utf-8")).hexdigest()


def generate_boarding_pin():
    """Generate a cryptographically secure four-digit PIN."""
    return secrets.randbelow(9000) + 1000


def export_flight_manifest(filename="flight_manifest.txt"):
    """Export flight details to a JSON manifest file."""
    with open(filename, "w", encoding="utf-8") as manifest:
        json.dump(FLIGHTS, manifest, indent=4)

    print(f"Boarding manifest printed: {filename}")


def get_flight_summary(flight_data):
    """Count flights that are not marked as full."""
    return sum(
        not details["is_full"]
        for details in flight_data.values()
    )


def main():
    """Run a demonstration of the flight reservation system."""
    book_flight_seat("AI101", "Kritika", 20)
    cancel_booking("BA202")

    print("Is AI101 open:", check_seat_availability("AI101"))
    print(
        "Baggage Fee:",
        calculate_baggage_fee("AI101", 0.15),
    )
    print(
        "Passenger Hash:",
        generate_passenger_hash("PASSPORT_IND_119"),
    )
    print("Boarding PIN:", generate_boarding_pin())

    export_flight_manifest()
    print("Available flights:", get_flight_summary(FLIGHTS))

    api_secret = os.getenv("AIRLINE_API_SECRET")
    print("API Token configured:", bool(api_secret))


if __name__ == "__main__":
    main()
