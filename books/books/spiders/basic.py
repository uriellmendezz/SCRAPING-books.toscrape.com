import scrapy
from books.items import BooksItem

class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):

        books = response.css('article.product_pod')
        for book in books:
            book_url = 'https://books.toscrape.com/catalogue/' + str(book.css('a::attr(href)').get())
            yield response.follow(book_url, self.parse_book_page)

        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            if 'catalogue' in next_page:
                next = 'https://books.toscrape.com/' + str(next_page)
            else:
                next = 'https://books.toscrape.com/catalogue/' + str(next_page)

            yield response.follow(next,
                                  callback=self.parse)
            
    def parse_book_page(self, response):

        table_rows = response.css('table tr')

        item = BooksItem()

        item['url'] = response.url,
        item['gender'] = str(response.xpath('//*[@id="default"]/div[1]/div/ul/li[3]/a/text()').get()),
        item['title'] = str(response.css('div.col-sm-6.product_main h1::text').get()),
        item['rating'] = str(response.css('div.col-sm-6.product_main p.star-rating').attrib['class']),
        item['description'] = str(response.xpath('//div[@id="product_description"]/following-sibling::p/text()').get()),
        item['upc'] = str(table_rows[0].css('td::text').get()),
        item['product_type'] = str(table_rows[1].css('td::text').get()),
        item['price_original'] = str(table_rows[2].css('td::text').get()),
        item['price_taxes'] = str(table_rows[3].css('td::text').get()),
        item['taxes'] = str(table_rows[4].css('td::text').get()),
        item['stock'] = str(table_rows[5].css('td::text').get()),
        item['reviews'] = str(table_rows[6].css('td::text').get())

        yield item
        
