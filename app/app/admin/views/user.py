from .base import CustomModelView


class UserView(CustomModelView):
    column_list = [
        "id",
        "login",
        "password",
        "salt",
        "status",
        "email",
        "balance",
        "raiting",
        "review_amount",
    ]
