import peewee_filters as filters

from api.constructions.models import Construction


class ConstructionFilter(filters.FilterSet):
    name = filters.Filter(operator="contains")

    def filter_description(self, query, value: bool, **kwargs):
        return query.where(
            Construction.description.is_null(not value) | (
                (Construction.description != "") if value else (Construction.description == "")
            )
        )

    class Meta:
        model = Construction
