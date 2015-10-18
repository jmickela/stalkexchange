from haystack import indexes

from .models import GardenItem

class GardenItemIndex (indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    #produce = indexes.CharField(document=True, use_template=False)

    def get_model(self):
        return GardenItem