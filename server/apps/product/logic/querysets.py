from django.db.models import QuerySet


class ProductQuerySet(QuerySet):
    def filter_by_category(self, categories):
        return self.filter(categories__in=categories)
