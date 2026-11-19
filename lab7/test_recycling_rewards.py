import math
from hypothesis import given, strategies as st

from recycling_rewards import (
    parse_collection,
    weight_average,
    net_points
)


# 1. parse_collection tests

@given(st.text() | st.none())
def test_parse_collection_no_crash(s):
    try:
        result = parse_collection(s)
    except ValueError:
        return

    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert result[0] != ""
    assert isinstance(result[1], float)
    assert math.isfinite(result[1])
    assert result[1] >= 0


@given(
    st.text(
        alphabet=st.characters(
            whitelist_categories=("L", "N")
        ),
        min_size=1
    ),
    st.floats(
        min_value=0,
        max_value=1000000,
        allow_nan=False,
        allow_infinity=False
    )
)
def test_parse_collection_valid(material, kg):
    result = parse_collection(f"{material}:{kg}")

    assert result[0] == material.title()
    assert math.isclose(result[1], kg)


# 2. weight_average tests

@given(st.text() | st.none())
def test_weight_average_no_crash(s):
    try:
        result = weight_average(s)
    except ValueError:
        return

    assert isinstance(result, int)
    assert result >= 0


@given(
    st.lists(
        st.integers(min_value=0, max_value=100000),
        min_size=1,
        max_size=100
    )
)
def test_weight_average_valid(weights):
    csv_input = ",".join(map(str, weights))
    result = weight_average(csv_input)

    assert result == sum(weights) // len(weights)


# 3. net_points tests

@given(st.text() | st.none())
def test_net_points_no_crash(s):
    try:
        result = net_points(s)
    except ValueError:
        return

    assert isinstance(result, float)
    assert math.isfinite(result)
    assert result >= 0


@given(
    st.floats(
        min_value=0,
        max_value=1000000,
        allow_nan=False,
        allow_infinity=False
    ),
    st.floats(
        min_value=0,
        max_value=1000000,
        allow_nan=False,
        allow_infinity=False
    )
)
def test_net_points_valid(points, penalty):
    result = net_points(f"{points}|{penalty}")

    assert math.isclose(
        result,
        max(points * 2 - penalty, 0)
    )