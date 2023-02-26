import pytest


@pytest.mark.tcid100
def test_food_item_get_list_by_section(client_random_token, db_utility, create_test_food_item):
    response = client_random_token.post("api/food/item/get-list-by-section")
    import pdb; pdb.set_trace()