import csv
from operator import attrgetter


class CSVStaticData:
    def __init__(self, file_path):

        # Load the CSV files into memory. Sort the products by popularity
        self.shops = self._read_shops(file_path('shops.csv'))
        self.products = sorted(self._read_products(file_path('products.csv')),
                               key=attrgetter('popularity'), reverse=True)
        self.tags = self._read_tags(file_path('tags.csv'))
        # Assign tags to the correspoding shops
        self._add_tags_to_shops(file_path('taggings.csv'))

    def _read_shops(self, filename):

        column_names = ['id', 'name', 'lat', 'lng']

        with open(filename, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            assert next(reader) == column_names
            return {_id: shop for _id, shop in self._generate_shops(reader)}

    def _read_products(self, filename):

        column_names = ['id', 'shop_id', 'title', 'popularity', 'quantity']

        with open(filename, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            assert next(reader) == column_names
            return [p for p in self._generate_products(reader, self.shops)]

    def _read_tags(self, tags_file):
        tags_dict = None
        column_names = ['id', 'tag']
        with open(tags_file, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            assert next(reader) == column_names
            tags_dict = {_id: tag for _id, tag in reader}
        return tags_dict

    def _add_tags_to_shops(self, taggings_file):

        column_names = ['id', 'shop_id', 'tag_id']

        with open(taggings_file, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            assert next(reader) == column_names
            for _, shop_id, tag_id in reader:
                self.shops[shop_id].add_tag_to_set(self.tags[tag_id])

    @staticmethod
    def _generate_shops(csv_reader):
        for line in csv_reader:
            yield line[0], Shop(*line[1:])

    @staticmethod
    def _generate_products(csv_reader, shops):
        for line in csv_reader:
            yield Product(shops, *line)

    @property
    def tags(self):
        return self.tags.values()


class Shop(object):

    def __init__(self, name, lat, lng):
        self.name, self.lat, self.lng = name, float(lat), float(lng)
        self._tags = set()

    @property
    def tags(self):
        return self._tags

    def add_tag_to_set(self, t):
        self._tags.add(t)

    def toDic(self):
        return {
            'name': self.name,
            'lat': self.lat,
            'lng': self.lng,
        }       


class Product(object):

    def __init__(self, shop_lookup, _id, shop_id, title, popularity, quantity):
        self.id, self.title, self.popularity, self.quantity = _id, title, float(popularity), int(quantity)
        self.shop = shop_lookup[shop_id]

    def toDic(self):
        return {
            'id': self.id,
            'popularity': self.popularity,
            'title': self.title,
            'quantity': self.quantity,
            'shop': self.shop.toDic(),
        }
