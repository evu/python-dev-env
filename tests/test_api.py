import hug

from falcon import HTTP_200

import api

# A fixture example (https://docs.pytest.org/en/latest/fixture.html#fixture)
# @pytest.fixture
# def db_conn():
#     import db_connection as db
#     return db.open_connection("mydb")


class TestEncodeEndpoint:

    # def test_example_using_fixture(self, db_conn):
    #     sql_results = db_conn.execute("SELECT * FROM USERS;")
    #     assert "admin" in sql_results

    def test_encode_v1_should_return_rotated_chars(self):
        response = hug.test.get(api, "v1/encode", {"text": "evu"})
        assert response.status == HTTP_200
        assert response.data["data"] == "rih"

    def test_encode_v2_should_return_rotated_chars(self):
        response = hug.test.get(api, "v2/encode", {"text": "evu"})
        assert response.status == HTTP_200
        assert response.data["result"] == "rih"

    def test_rot13_should_rotate_chars(self):
        result = api.rot13("evu")
        assert result == "rih"
