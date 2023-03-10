from voluptuous import Schema, PREVENT_EXTRA

user = Schema(
    {

        "id": int,
        "email": str,
        "first_name": str,
        "last_name": str,
        "avatar": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

support = Schema(
    {
        "url": str,
        "text": str,
        # Optional("new"): int - указывает, что поле либо вернется либо нет
    },
    required=True,
    extra=PREVENT_EXTRA
)

single_user_schema = Schema(
    {
        "data": user,
        "support": support
    },
    required=True,
    extra=PREVENT_EXTRA

)

users_list_schema = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": [user],
        "support": support
    }
)

create_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str
    },
    required=True,
    extra=PREVENT_EXTRA

)

update_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "updatedAt": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

login_successful_schema = Schema(
    {
        "token": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

register_user_schema = Schema(
    {
        "id": int,
        "token": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

login_unsuccessful_schema = Schema(
{
    "error": str
}
)