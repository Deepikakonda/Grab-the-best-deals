from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Deal, Product
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    return render(request, 'index.html')

def groceries(request):
    return render(request, 'groceries.html')

def stationeries(request):
    return render(request, 'stationeries.html')

def furnitures(request):
    return render(request, 'furnitures.html')

def gadgets(request):
    return render(request, 'clothing.html')

logger = logging.getLogger(__name__)


CATEGORIES = ['furnitures', 'stationeries', 'electronics', 'gadgets', 'vegetables']
CATEGORIES_GROCERIES = ["fruits", "vegetables"]
CATEGORIES_STATIONERIES = ['stationaries']
CATEGORIES_FURNITURES = ['furnitures']
CATEGORIES_CLOTHING = ['gadgets']

def scrape_deals_by_category(category, store_url_template):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = store_url_template.format(category.replace(' ', '+'))
    response = requests.get(url, headers=headers)
    deals = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Assuming item_containers and further selection based on specific site structure
        for item in soup.select('.item-container'):
            try:
                deal = parse_item(item)
                deals.append(deal)
            except Exception as e:
                logger.error(f"Failed to parse item in {category} due to {e}")
    else:
        logger.error(f"Failed to fetch category {category} from {url}")

    return deals

def parse_item(item):
    title_element = item.select_one('.item-title')
    price_element = item.select_one('.price-current')
    if not title_element or not price_element:
        raise ValueError("Required elements missing in the item")

    title = title_element.text
    price_text = price_element.text.strip('$,')
    price = float(price_text.split()[0])
    url = title_element['href']
    image_url = item.select_one('img')['src']

    product, _ = Product.objects.get_or_create(name=title)
    deal, _ = Deal.objects.get_or_create(
        product=product, store='Newegg', price=price, url=url, image_url=image_url
    )
    return deal

def home(request):
    # ebay_template = 'https://www.ebay.com/sch/i.html?_nkw={}'
    newegg_template = 'https://www.newegg.com/p/pl?d={}'

    combined_deals = {}
    for category in CATEGORIES:
        # ebay_deals = scrape_deals_by_category(category, ebay_template)
        newegg_deals = scrape_deals_by_category(category, newegg_template)
        all_deals = newegg_deals
        combined_deals[category] = all_deals[:6]  # Limit to only 5 deals per category

    return render(request, 'index.html', {'deals': combined_deals})

def groceries(request):
    # ebay_template = 'https://www.ebay.com/sch/i.html?_nkw={}'
    newegg_template = 'https://www.newegg.com/p/pl?d={}'

    combined_deals = {}
    for category in CATEGORIES_GROCERIES:
        # ebay_deals = scrape_deals_by_category(category, ebay_template)
        newegg_deals = scrape_deals_by_category(category, newegg_template)
        combined_deals[category] = newegg_deals

    return render(request, 'groceries.html', {'deals': combined_deals})

def stationeries(request):
    # ebay_template = 'https://www.ebay.com/sch/i.html?_nkw={}'
    newegg_template = 'https://www.newegg.com/p/pl?d={}'

    combined_deals = {}
    for category in CATEGORIES_STATIONERIES:
        # ebay_deals = scrape_deals_by_category(category, ebay_template)
        newegg_deals = scrape_deals_by_category(category, newegg_template)
        combined_deals[category] = newegg_deals

    return render(request, 'stationeries.html', {'deals': combined_deals})

def furnitures(request):
    # ebay_template = 'https://www.ebay.com/sch/i.html?_nkw={}'
    newegg_template = 'https://www.newegg.com/p/pl?d={}'

    combined_deals = {}
    for category in CATEGORIES_FURNITURES:
        # ebay_deals = scrape_deals_by_category(category, ebay_template)
        newegg_deals = scrape_deals_by_category(category, newegg_template)
        combined_deals[category] = newegg_deals

    return render(request, 'furnitures.html', {'deals': combined_deals})

def gadgets(request):
    # ebay_template = 'https://www.ebay.com/sch/i.html?_nkw={}'
    newegg_template = 'https://www.newegg.com/p/pl?d={}'

    combined_deals = {}
    for category in CATEGORIES_CLOTHING:
        # ebay_deals = scrape_deals_by_category(category, ebay_template)
        newegg_deals = scrape_deals_by_category(category, newegg_template)
        combined_deals[category] = newegg_deals

    return render(request, 'gadgets.html', {'deals': combined_deals})

# EBAY_TEMPLATE = 'https://www.ebay.com/sch/i.html?_nkw={}'
NEWEGG_TEMPLATE = 'https://www.newegg.com/p/pl?d={}'

def search_deals(request):
    search_term = request.GET.get('q', '').strip()

    # Only perform the search if there is a search term
    if search_term:
        # The URL templates are placeholders. Replace them with the actual URLs of the websites you want to scrape.
        # ebay_template = 'https://www.ebay.com/sch/i.html?_nkw={}'
        newegg_template = 'https://www.newegg.com/p/pl?d={}'

        # Scrape deals from multiple sources
        # deals = scrape_deals_by_category(search_term, ebay_template)
        deals = scrape_deals_by_category(search_term, newegg_template)
        
        context = {'deals': deals, 'query': search_term}
    else:
        # If there's no search term, don't send any deals
        context = {'deals': [], 'query': ''}

    # Render the page with the deals
    return render(request, 'groceries.html', context)

def groceries_search(request):
    search_term = request.GET.get('q', '').strip()
    deals = {'Search Results': []}  # Default to an empty list in case no deals are found
    
    # Only perform the search if there is a search term
    if search_term:
        # Assume `scrape_newegg_deals` is your function that returns a list of deals
        search_results_newegg = scrape_newegg_deals(search_term)
        # search_results_ebay = scrape_ebay_deals(search_term)
        
        # Add the search results to the dictionary under a 'Search Results' key
        deals['Search Results'] = search_results_newegg
    
    # Pass the dictionary to the context
    context = {
        'deals': deals,
        'query': search_term
    }
    
    return render(request, 'deals_all.html', context)

def scrape_newegg_deals(search_term):
    search_url = f"https://www.newegg.com/p/pl?d={search_term}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(search_url, headers=headers)
    deals = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        product_listings = soup.find_all('div', class_='item-container')
        
        for item in product_listings:
            try:
                title_element = item.select_one('.item-title')
                price_element = item.select_one('.price-current')
                original_price_element = item.select_one('.price-was-data')
                image_element = item.select_one('img')

                if not title_element or not price_element or not image_element:
                    continue  # Skip this item if it doesn't have all required elements

                title = title_element.text
                price_text = price_element.text.strip('$,').replace(" ", "").replace("\r", "").replace("\n", "")
                original_price_text = original_price_element.text.strip('$,').replace(" ", "").replace("\r", "").replace("\n", "")
                # Assuming the price is the first number before the first space
                price = float(price_text.split()[0])
                original_price = float(original_price_text.split()[0])
                image_url = image_element['src']
                product_url = title_element['href']

                # This part is similar to parse_item
                product, _ = Product.objects.get_or_create(name=title)
                deal, _ = Deal.objects.get_or_create(
                    product=product,
                    store='Newegg',
                    price=price,
                    original_price=original_price,
                    url=product_url,
                    image_url=image_url
                )

                # Append the deal object instead of dictionary
                deals.append(deal)
            except Exception as e:
                print(f"Error parsing item: {e}")
    
    return deals

# def scrape_ebay_deals(search_term):
#     ebay_url = f'https://www.ebay.com/sch/i.html?_nkw={search_term}'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     }
    
#     response = requests.get(ebay_url, headers=headers)
#     deals = []

#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         item_containers = soup.find_all('div', class_='s-item__info')  # Update the selector as needed

#         for item_container in item_containers:
#             try:
#                 title_element = item_container.find('h3', class_='s-item__title')  # Update the selector as needed
#                 if not title_element:
#                     continue  # Skip this item if title is not found

#                 title = title_element.text.strip()

#                 price_element = item_container.find('span', class_='s-item__price')  # Update the selector as needed
#                 if not price_element:
#                     continue  # Skip if price is not found

#                 price_text = price_element.get_text(strip=True).replace(',', '').replace('$', '')
#                 price = float(price_text.split(' to ')[0].split()[0])  # Take the first price if there's a range

#                 url_element = item_container.find('a', class_='s-item__link')  # Update the selector as needed
#                 if not url_element:
#                     continue  # Skip if URL is not found

#                 product_url = url_element['href']

#                 image_element = item_container.find('img', class_='s-item__image-img')  # Update the selector as needed
#                 if not image_element:
#                     continue  # Skip if image is not found

#                 image_url = image_element['src']

#                 # Create or get the product and deal instances
#                 product, _ = Product.objects.get_or_create(name=title)
#                 deal, _ = Deal.objects.get_or_create(
#                     product=product,
#                     store='eBay',
#                     price=price,
#                     url=product_url,
#                     image_url=image_url
#                 )

#                 deals.append(deal)
#             except Exception as e:
#                 logger.error(f"Error parsing eBay item: {e}")
#     else:
#         logger.error(f"Failed to connect to eBay with status code {response.status_code}")

#     return deals

