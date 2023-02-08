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


