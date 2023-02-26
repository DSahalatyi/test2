import pytest


@pytest.mark.tcid96
@pytest.mark.usefixtures("create_test_food_section")
@pytest.mark.usefixtures("create_random_food_section")
def test_food_section_get_all_random_token(client_random_token, db_utility):
    response = client_random_token.get("api/food/section/get-all")
    db_food_sections = list(db_utility.foodsections.find({}))
    # Casting ObjectID to str for vaid comparison
    for food_section in db_food_sections:
        food_section["_id"] = str(food_section["_id"])
    assert response.json()["list"] == db_food_sections


@pytest.mark.tcid97
@pytest.mark.usefixtures("create_test_food_section")
@pytest.mark.usefixtures("create_random_food_section")
def test_food_section_get_all_is_staff_token(client_is_staff_token, db_utility):
    response = client_is_staff_token.get("api/food/section/get-all")
    db_food_sections = list(db_utility.foodsections.find({}))
    # Casting ObjectID to str for vaid comparison
    for food_section in db_food_sections:
        food_section["_id"] = str(food_section["_id"])
    assert response.json()["list"] == db_food_sections
