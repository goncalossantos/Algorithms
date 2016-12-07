from geopy.distance import great_circle
from itertools import islice


class SearchQuery(object):

    def __init__(self, static_data, input_form):

        self.static_data = static_data
        self.radius_km = input_form.radius.data / 1000.
        self.center = (input_form.lat.data, input_form.lng.data)
        self.tags = input_form.tags.data
        self.total_products_to_return = input_form.total_products.data

    def apply(self):
        # Get all the shops inside the radius
        shops_inside_circle = set()
        for shop in self.static_data.shops.values():
            if great_circle((shop.lat, shop.lng), (self.center[0], self.center[1])) < self.radius_km and not (
                self.tags and self.tags.isdisjoint(shop.tags)
            ):
                shops_inside_circle.add(shop)
        # Return most popular products that are sold on those shops up to total_products to return
        return islice(
            [product.toDic() for product in self.static_data.products if product.shop in shops_inside_circle],
            self.total_products_to_return,
        )
