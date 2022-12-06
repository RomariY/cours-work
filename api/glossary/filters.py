import peewee_filters as filters

from api.glossary.models import Glossary


class GlossaryFilter(filters.FilterSet):
    name = filters.Filter(operator="contains")

    def filter_description(self, query, value: bool, **kwargs):
        return query.where(
            Glossary.description.is_null(not value) | (
                (Glossary.description != "") if value else (Glossary.description == "")
            )
        )

    class Meta:
        model = Glossary
