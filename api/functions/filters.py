import peewee_filters as filters

from api.functions.models import DataType, Function


class DataTypeFilter(filters.FilterSet):
    name = filters.Filter(operator="startswith")

    def filter_description(self, query, value: bool, **kwargs):
        return query.where(
            DataType.description.is_null(not value) | (
                (DataType.description != "") if value else (DataType.description == "")
            )
        )

    class Meta:
        model = DataType


class FunctionFilter(filters.FilterSet):
    name = filters.Filter(operator="contains")

    def filter_description(self, query, value: bool, **kwargs):
        return query.where(
            Function.description.is_null(not value) | (
                (Function.description != "") if value else (Function.description == "")
            )
        )

    class Meta:
        model = Function
