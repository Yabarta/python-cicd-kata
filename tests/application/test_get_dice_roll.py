from app.application.get_dice_roll import get_dice_roll


def test_result_is_a_valid_dice_value() -> None:
    for _ in range(100):
        result = get_dice_roll()
        assert isinstance(result, int)
        assert result in {1 + 4, 2 + 4, 3 + 4, 4 + 4, 5 + 4, 6 + 4}
