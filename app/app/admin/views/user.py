from .base import CustomModelView


class UserView(CustomModelView):
    column_list = [
        "id",
        "login",
        "status",
        "email",
        "balance",
        "raiting",
        "review_amount",
    ]
