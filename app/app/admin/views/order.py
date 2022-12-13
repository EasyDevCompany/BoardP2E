from .base import CustomModelView


class OrderView(CustomModelView):
    column_list = [
        "id",
        "amount_of_selling_item",
        "price_for_one_currency",
        "view_amount",
        "server_eng",
        "side_eng",
        "description_eng",
        "name_of_currency_ru",
        "server_ru",
        "side_ru",
        "description_ru",
        "author_of_deal",
        "category",
        "status",
        "created_at",
        "subfields",
    ]
