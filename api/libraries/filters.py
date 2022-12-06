import peewee_filters as filters

from api.libraries.models import Library


class LibraryFilter(filters.FilterSet):
    name = filters.Filter(operator="contains")
    type = filters.Filter(operator="contains")

    def filter_description(self, query, value: bool, **kwargs):
        return query.where(
            Library.description.is_null(not value) | (
                (Library.description != "") if value else (Library.description == "")
            )
        )

    class Meta:
        model = Library
