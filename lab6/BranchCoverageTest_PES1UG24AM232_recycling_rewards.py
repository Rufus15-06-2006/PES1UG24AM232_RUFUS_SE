
import pytest
from recycling_rewards import reward_points, collection_accepted, slot_status


def test_unknown_material_raises():
    with pytest.raises(ValueError, match="unknown material"):
        reward_points("glass", 10, False)


def test_negative_weight_raises():
    with pytest.raises(ValueError, match="invalid weight"):
        reward_points("paper", -1, False)


def test_bonus_applied_to_non_metal():
    assert reward_points("paper", 5, True) == 6


def test_bonus_not_applied_when_false():
    assert reward_points("paper", 6, False) == 6


def test_bonus_not_applied_to_metal():
    assert reward_points("metal", 3, True) == 12


def test_extra_equal_zero_returns_zero():
    assert reward_points("plastic", 3, False) == 0


def test_non_metal_rate_without_large_extra():
    assert reward_points("plastic", 4, False) == 6


def test_metal_rate_without_large_extra():
    assert reward_points("metal", 3, False) == 12


def test_large_extra_non_metal_increases_rate():
    assert reward_points("plastic", 24, False) == 210


def test_large_extra_metal_increases_rate_again():
    assert reward_points("metal", 23, False) == 378


def test_hazardous_weight_at_limit_is_accepted():
    assert collection_accepted(5, 99, True) is True


def test_hazardous_weight_over_limit_is_rejected():
    assert collection_accepted(6, 1, True) is False


def test_non_hazardous_weight_over_50_is_rejected():
    assert collection_accepted(51, 1, False) is False


def test_non_hazardous_weight_at_50_and_three_bags_is_accepted():
    assert collection_accepted(50, 3, False) is True


def test_non_hazardous_more_than_three_bags_is_rejected():
    assert collection_accepted(20, 4, False) is False


def test_morning_non_holiday_open():
    assert slot_status(20, True, False) == "open"


def test_evening_holiday_open():
    assert slot_status(25, False, True) == "open"


def test_morning_holiday_late():
    assert slot_status(20, True, True) == "late"


def test_evening_non_holiday_late():
    assert slot_status(9, False, False) == "late"


def test_morning_non_holiday_missed():
    assert slot_status(4, True, False) == "missed"


def test_evening_holiday_missed():
    assert slot_status(9, False, True) == "missed"
