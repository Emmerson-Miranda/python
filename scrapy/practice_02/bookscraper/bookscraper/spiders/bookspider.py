import scrapy

# scrapy crawl bookspider
# scrapy crawl bookspider -o bookdata.csv
# scrapy crawl bookspider -o bookdata.json
class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com"]

    def parse(self, response):
        books = response.css('article.product_pod')
        for book in books:
            next_page = book.css('h3 a').attrib['href']
            yield response.follow(next_page, callback=self.parse_book)
            #yield {
            #    'name' : book.css('h3 a::text').get(),
            #    'price' : book.css('.product_price .price_color a::text').get(),
            #    'url' : book.css('h3 a').attrib['href']
            #}
        
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_book(self, response):
        table_rows = response.css('table.table-striped tr')
        yield {
            'url': response.url,
            'title': response.css('.product_main h1::text').get(),
            'product_type': table_rows[1].css('td ::text').get(),
            'price_exc_tax': table_rows[2].css('td ::text').get(),
            'price_incl_tax': table_rows[3].css('td ::text').get(),
            'tax': table_rows[4].css('td ::text').get(),
            'availability': table_rows[5].css('td ::text').get(),
            'num_reviews': table_rows[6].css('td ::text').get(),
            'stars': response.css('p.star-rating').attrib['class'],
            'category': response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get(),
            'description': response.xpath("//div[@id='product_description']/following-sibling::p/text()").get(),
            'price': response.css('p.price_color ::text').get()
        }