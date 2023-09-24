## CNN Web Scraping Spider

This Python code defines a web scraping spider using Scrapy to extract information from the CNN website and save it in a CSV file.  
Below, is the key components and functionalities of the code:

#Demo Video: https://youtu.be/fOO04dZ9-2A

### Dependencies:

scrapy: Scrapy is a Python web scraping framework.

urljoin: Used to join relative and absolute URLs.

datetime and date: Used for working with dates.

requests: Used to make HTTP requests to download images.

os: Provides functions for working with the operating system.

csv: Allows reading and writing CSV files.

Define a class named CnnspideySpider that inherits from Scrapy's Spider class.

### Define class attributes:

name: Specifies the spider's name as "cnnspidey."

allowed_domains: Lists the allowed domain(s) for scraping (in this case, "edition.cnn.com").

base_url: Specifies the base URL for the CNN website.

sections: Lists various sections of the website to scrape.

start_urls: Generates a list of starting URLs by joining the base URL with each section.

csv_file: Defines the name of the CSV file where data will be stored.


### Functions

Implement the __init__ method:

Initializes the spider with optional parameters date and depth.
Sets attributes such as date_to_compare, date_string, visited_urls, max_depth, depth, and initializes the CSV file if it doesn't exist.
Define a format_date method:

Converts a date string to a specific format ("dd mm yyyy" to "yyyy/mm/dd").
Define a handle_error method:

Handles errors when making HTTP requests.
Implement the parse method:

Parses web pages to extract links.

Iterates through links on the page, checks if they contain the specified date string, and follows them for further parsing.
Increments the depth to limit the number of pages to scrape.

Logs when the maximum depth is reached.

Define a save_image method:

Downloads images from URLs and saves them to a local directory.
Handles exceptions and logs errors.

Implement the parse_link method:

Parses individual article pages to extract title and image information.
Extracts the article's title and the URL of the main image.
Calls the save_image method to download and save the image locally.
Appends the title and local image path to the CSV file.

In summary, this code defines a Scrapy spider named "cnnspidey" that crawls CNN's website, extracts article titles and images, and saves them to a CSV file. The spider can be configured with a specific date and depth, and it limits its scraping based on these parameters. Images are downloaded and saved locally for each article.


## Replication

Python: Ensure that you have Python installed on your system. You can download and install Python from the official website: Python Downloads.

Scrapy: Install the Scrapy framework using pip, which is the package manager for Python:

pip install scrapy

Clone the Repository: Clone it to your local machine using Git:

git clone <repository_url>
Navigate to the Project Directory: Change your current directory to the project directory:

cd <project_directory>
Create a Virtual Environment (Optional): It's a good practice to work within a virtual environment to manage dependencies. Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate
Install Dependencies: Install the required Python libraries specified in the code (Scrapy, urllib, datetime, requests, os, csv):

pip install urllib3 requests
Run the Spider: Execute the Scrapy spider by running the following command:

scrapy crawl cnnspidey -o cnn_data.json
This command will start the web scraping process using the "cnnspidey" spider and save the extracted data to a JSON file named "cnn_data.json." You can change the output format and filename as needed (e.g., CSV, XML).


### Limitations

The code may not work if the structure of the CNN website changes.

It assumes a specific format for dates in URLs.

Error handling for network issues or website changes is limited.

Large-scale scraping may be subject to rate limiting and legal considerations.


### Future Scope
Potential improvements and extensions for this code include:

Enhanced error handling and recovery mechanisms.

Incorporating user-agent rotation to avoid IP blocking.

Handling dynamic websites that load content via JavaScript.

Adding support for more news websites.

Implementing multi-threading or distributed scraping for performance.
