import scrapy
from urllib.parse import urljoin
from datetime import datetime, date as dt_date
import requests
import os
import csv

class CnnspideySpider(scrapy.Spider):
    name = "cnnspidey"
    allowed_domains = ["edition.cnn.com"]
    base_url = "https://edition.cnn.com/"
    sections = [
        "world/india",
        "weather",
        "us/energy-and-environment",
        "us/space-science",
        "world",
        "world/europe",
        "politics",
        "business",
        "entertainment",
        "travel"
    ]
    start_urls = [urljoin("https://edition.cnn.com/", section) for section in sections]
    csv_file = "cnn_ksh.csv"  

    def __init__(self, date=None, depth=1000, *args, **kwargs):
        super(CnnspideySpider, self).__init__(*args, **kwargs)  
        self.date_to_compare = date if date else dt_date.today().strftime("%d %m %Y")
        self.date_string = self.format_date(self.date_to_compare)
        self.visited_urls = set()
        self.max_depth = int(depth)
        self.depth = 0
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["Title", "Local Image Path"])
    
    def format_date(self, date):
        date_obj = datetime.strptime(date, "%d %m %Y")
        formatted_date = date_obj.strftime("%Y/%m/%d")
        return formatted_date
    
    def handle_error(self, failure):
        self.log(f"Failed to fetch URL: {failure.request.url} - {failure.value}")

    def parse(self, response):
        if self.depth < self.max_depth:
            link_elements = response.css('a.container__link')  
            for link_element in link_elements:
                relative_link = link_element.attrib['href']
                absolute_link = urljoin(response.url, relative_link)
                if self.date_string in absolute_link:
                    self.visited_urls.add(absolute_link)
                    yield response.follow(absolute_link, callback=self.parse_link, errback=self.handle_error)
            self.depth += 1
        else:
            self.log(f"Reached maximum depth of {self.max_depth}")
    
    def save_image(self, img_url):
        try:
            image_data = requests.get(img_url).content
            image_name = os.path.basename(img_url.split('?')[0])
            image_path = os.path.join('downloaded_images', image_name)
            if not os.path.exists('downloaded_images'):
                os.makedirs('downloaded_images')
            with open(image_path, 'wb') as handler:
                handler.write(image_data)
            return image_path
        except Exception as e:
            self.log(f"Error downloading image: {e}")
            return None

    def parse_link(self, response):
        title = response.xpath('//h1[@data-editable="headlineText"]/text()').get().strip()
        img = response.css("meta[property='og:image']::attr(content)").get()
        if img:
            local_img_path = self.save_image(img)
            with open(self.csv_file, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([title, local_img_path])
# run : scrapy crawl cnnspidey -a date="23 09 2023" -a depth=1000 -o cnnspidey.json