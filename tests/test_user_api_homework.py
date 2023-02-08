import requests
import logging
from pytest_voluptuous.voluptuous import S
from schemas.user import create_user_schema, update_user_schema, login_successful_schema, register_user_schema


def test_create_user_schema():
    new_user = {
        "name": "Sergey",
        "job": "Super QA"
    }

    result = requests.post(f'{base_url}/api/users', new_user)
    logging.info(result.json())

    assert result.status_code == 201
    assert len(result.json()) == 4
    assert result.json()["name"] == "Sergey"
    assert S(create_user_schema) == result.json()


def test_update_user_schema():
    update_user = {
        "name": "morpheus",
        "job": "zion resident"
    }

    result = requests.put(f'{base_url}/api/users/2', update_user)
    logging.info(result.json())

    assert result.status_code == 200
    assert len(result.json()) == 3
    assert result.json()["job"] == "zion resident"
    assert S(update_user_schema) == result.json()


def test_register_user_schema():
    user_date = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    result = requests.post(f'{base_url}/api/register', user_date)
    logging.info(result.json())

    assert result.status_code == 200
    assert result.json()["token"] is not None
    assert S(register_user_schema) == result.json()


def test_user_login_successful_schema():
    user_login = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    result = requests.post(f'{base_url}/api/login', user_login)
    logging.info(result.json())

    assert result.status_code == 200
    assert result.json()["token"] is not None
    assert S(login_successful_schema) == result.json()


base_url = 'https://reqres.in'
