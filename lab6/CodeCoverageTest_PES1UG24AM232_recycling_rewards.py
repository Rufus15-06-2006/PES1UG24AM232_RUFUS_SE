
import pytest
from recycling_rewards import reward_points, collection_accepted, slot_status


def test_reward_points_below_minimum():
    assert reward_points("paper", 3, False) == 0


def test_reward_points_unknown_material():
    with pytest.raises(ValueError, match="unknown material"):
        reward_points("glass", 10, False)


def test_reward_points_negative_weight():
    with pytest.raises(ValueError, match="invalid weight"):
        reward_points("paper", -1, False)


def test_reward_points_bonus_and_high_extra_metal():
    assert reward_points("metal", 27, True) == 25 * 18


def test_reward_points_bonus_non_metal_and_high_extra():
    assert reward_points("paper", 25, True) == 21 * 10


def test_collection_accepted_hazardous():
    assert collection_accepted(5, 10, True) is True


def test_collection_rejected_non_hazardous_weight():
    assert collection_accepted(51, 1, False) is False


def test_collection_accepted_non_hazardous_bags():
    assert collection_accepted(20, 3, False) is True


def test_slot_status_open():
    assert slot_status(25, True, False) == "open"


def test_slot_status_late():
    assert slot_status(4, False, False) == "late"


def test_slot_status_missed():
    assert slot_status(-6, False, False) == "missed"


def test_slot_status_holiday_cutoff():
    assert slot_status(25, False, True) == "open"
