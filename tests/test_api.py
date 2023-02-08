import logging

import requests
from pytest_voluptuous import S
from requests import Response

from schemas.user import single_user_schema, users_list_schema


def test_get_single_user():
    response: Response = requests.get(url='https://reqres.in/api/users/2')
    logging.info(response.status_code)

    assert response.status_code == 200
    assert response.json()["data"]["email"] == "janet.weaver@reqres.in"
    assert response.json()["data"]["first_name"] == "Janet"


def test_get_single_user_has_avatar_field():
    response: Response = requests.get('https://reqres.in/api/users/2')
    logging.info(response.status_code)

    assert response.status_code == 200
    assert response.json().get("data").get("avatar", None)


def test_get_single_user_has_avatar_exists():
    response: Response = requests.get('https://reqres.in/api/users/2')
    logging.info(response.status_code)
    avatar = response.json().get("data").get("avatar")
    result = requests.get(avatar)

    assert result.status_code == 200
    assert len(response.content) == 280


def test_get_single_user_schema():
    response: Response = requests.get('https://reqres.in/api/users/2')

    assert S(single_user_schema) == response.json()


def test_get_users_list_shema():
    result = requests.get('https://reqres.in/api/users?page=2')
    logging.info(result.json())

    assert S(users_list_schema) == result.json()


def test_users_default_count_on_page():
    response = requests.get('https://reqres.in/api/users?page=2')
    per_page = response.json()["per_page"]
    data = response.json()["data"]

    assert per_page == 6
    assert len(data) == 6
