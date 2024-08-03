# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re


class BooksPipeline:

    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        # Gender and Product_type
        columns = ['gender', 'product_type']
        for c in columns:
            value = adapter.get(c)[0]
            adapter[c] = value.lower()

        # Prices
        cols = ['price_original', 'price_taxes', 'taxes']
        for column in cols:
            value = adapter.get(column)[0]
            adapter[column] = float(value[1:])

        # Stock
        value = adapter.get('stock')[0]
        number_value = re.sub(r'\D', '', value)
        adapter['stock'] = int(number_value)

        # Rating
        col = adapter.get('rating')[0]
        value = col.strip('star-rating ').lower().strip()
        value = str(value)

        values_dict = {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5
        }

        number_value = values_dict[value]
        adapter['rating'] = number_value

        return item
