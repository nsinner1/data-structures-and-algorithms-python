from left_join import left_join
import pytest

@pytest.fixture
def my_dict():
    dict1 = {
        'fond':'enamored',
        'wrath':'anger',
        'diligent':'employed',
        'outfit':'garb',
        'guide':'usher'
        }

    return dict1


def test_given_example(my_dict):

    dict1 = my_dict
    dict2 = {
        'fond':'averse',
        'wrath':'delight',
        'diligent':'idle',
        'guide':'follow',
        'flow':'jam'
        }

    assert left_join(dict1,dict2) == {
                                "fond": ["enamored","averse"],
                                "wrath": ["anger","delight"],
                                "diligent": ["employed","idle"],
                                "outfit": ["garb",None],
                                "guide": ["usher","follow"]
                                }