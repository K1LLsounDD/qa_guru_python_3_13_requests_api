import requests
import logging
from pytest_voluptuous.voluptuous import S
from schemas.user import create_user_schema


def test_create_user_schema():
    new_user = {
        "name": "Sergey",
        "job": "Super QA"
    }

    result = requests.post('https://reqres.in/api/users', new_user)
    logging.info(result.json())

    assert result.status_code == 201
    assert S(create_user_schema) == result.json()
