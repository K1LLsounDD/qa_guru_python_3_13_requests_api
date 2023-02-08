import requests
import logging
from pytest_voluptuous.voluptuous import S
from schemas.user import create_user_schema, update_user_schema, login_successful_schema


def test_create_user_schema():
    new_user = {
        "name": "Sergey",
        "job": "Super QA"
    }

    result = requests.post('https://reqres.in/api/users', new_user)
    logging.info(result.json())

    assert result.status_code == 201
    assert S(create_user_schema) == result.json()


def test_update_user_schema():
    update_user = {
        "name": "morpheus",
        "job": "zion resident"
    }

    result = requests.put('https://reqres.in/api/users/2', update_user)
    logging.info(result.json())

    assert result.status_code == 200
    assert S(update_user_schema) == result.json()


def test_delete_user_schema():
    result = requests.delete('https://reqres.in/api/users/2')

    assert result.status_code == 204


def test_user_login_successful_schema():
    user_login = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    result = requests.post('https://reqres.in/api/login', user_login)
    logging.info(result.json())

    assert result.status_code == 200
    assert S(login_successful_schema) == result.json()
