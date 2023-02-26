# import pytest
#
# pytestmark = pytest.mark.admin_models
#
#
# @pytest.mark.tcid96
# def test_models(client_is_staff_token, db_utility):
#     db_utility.database.create_collection("test")
#     response = client_is_staff_token.get("api/admin/models")
#     import pdb; pdb.set_trace()