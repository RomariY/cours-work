import peewee_filters as filters

from api.operators.models import Operator


class OperatorFilter(filters.FilterSet):
    name = filters.Filter(operator="startswith")

    def filter_description(self, query, value: bool, **kwargs):
        return query.where(
            Operator.description.is_null(not value) | (
                (Operator.description != "") if value else (Operator.description == "")
            )
        )

    class Meta:
        model = Operator
