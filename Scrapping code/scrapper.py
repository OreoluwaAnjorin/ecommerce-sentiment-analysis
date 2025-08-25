import requests
from bs4 import BeautifulSoup
import time
import re

def get_jumia_reviews(product_urls, total_reviews=1100):
    """Scrape reviews from multiple Jumia product pages"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5"
    }
    
    reviews = set()  # Use set to automatically handle duplicates
    page = 1
    
    print(f"Scraping Jumia reviews from {len(product_urls)} product pages...")
    
    for product_url in product_urls:
        print(f"\nScraping from: {product_url}")
        page = 1
        consecutive_no_new_reviews = 0 
        
        while len(reviews) < total_reviews:
            if "productratingsreviews" in product_url:
                page_url = f"{product_url}?page={page}"
            else:
                page_url = f"{product_url}?page={page}"
            
            print(f"Scraping page {page}...")
            
            try:
                response = requests.get(page_url, headers=headers, timeout=10)
                
                if response.status_code != 200:
                    print(f"Failed to get page {page}. Status: {response.status_code}")
                    break
                
                soup = BeautifulSoup(response.text, 'html.parser')
                
                review_elements = []
                review_elements = soup.find_all('div', class_=re.compile(r'review|comment|feedback|rating', re.IGNORECASE))
                
                if not review_elements:
                    review_elements = soup.find_all(['p', 'div', 'span'], string=re.compile(r'good|great|nice|love|like|quality|comfortable|fit|style|excellent|amazing|perfect|recommend', re.IGNORECASE))

                if not review_elements:
                    all_text_elements = soup.find_all(['p', 'div', 'span'])
                    for element in all_text_elements:
                        text = element.get_text(strip=True)
                        if text and len(text) > 30 and len(text) < 500:
                            # Check if text looks like a review
                            review_keywords = ['good', 'great', 'nice', 'love', 'like', 'quality', 'comfortable', 'fit', 'style', 'excellent', 'amazing', 'perfect', 'recommend', 'product', 'use', 'buy', 'purchase']
                            if any(keyword in text.lower() for keyword in review_keywords):
                                review_elements.append(element)
                
                if not review_elements:
                    print(f"No reviews found on page {page}. Moving to next product.")
                    break
                
                reviews_before = len(reviews)
                page_reviews = 0
                
                for element in review_elements:
                    text = element.get_text(strip=True)
                    if text and len(text) > 20 and len(text) < 1000:
                        exclude_keywords = ['$', 'price', 'add to cart', 'buy now', 'shipping', 'delivery', 'stock', 'availability', 'specification', 'description']
                        if not any(keyword in text.lower() for keyword in exclude_keywords):
                            reviews.add(text)
                            page_reviews += 1
                            if len(reviews) >= total_reviews:
                                break

                new_unique_reviews = len(reviews) - reviews_before
                print(f"Found {page_reviews} reviews on page {page}, {new_unique_reviews} new unique (Total unique: {len(reviews)})")
                
                if new_unique_reviews == 0:
                    consecutive_no_new_reviews += 1
                    print(f"No new unique reviews found. Consecutive count: {consecutive_no_new_reviews}/3")
                    
                    if consecutive_no_new_reviews >= 3:
                        print(f"3 consecutive pages with no new reviews. Moving to next product.")
                        break
                else:
                    consecutive_no_new_reviews = 0  
                
                page += 1
                time.sleep(2)  # Increased delay to be more respectful
                
            except Exception as e:
                print(f"Error scraping page {page}: {e}")
                break
    
    return list(reviews)

product_urls = [
    "https://www.jumia.com.ng/catalog/productratingsreviews/sku/NI930ST2G34R8NAFAMZ/",
    "https://www.jumia.com.ng/catalog/productratingsreviews/sku/FA203MW4MZSOQNAFAMZ/",
    "https://www.jumia.com.ng/catalog/productratingsreviews/sku/FL585EA3CG6JHNAFAMZ/",
    "https://www.jumia.com.ng/catalog/productratingsreviews/sku/NI930ST23IVW4NAFAMZ/",
    "https://www.jumia.com.ng/catalog/productratingsreviews/sku/AI075HB19HEEMNAFAMZ/"
]

all_reviews = get_jumia_reviews(product_urls, total_reviews=1100)

print(f"\nTotal unique reviews collected: {len(all_reviews)}")

if all_reviews:
    training_reviews = all_reviews[:1000]
    test_reviews = all_reviews[1000:1100]
    
    with open("Nivea_men_reviews.txt", "w", encoding="utf-8") as f:
        for review in training_reviews:
            f.write(review + "\n")
    
    print(f"Saved {len(training_reviews)} reviews to Nivea_men_reviews.txt")
    
    with open("nivea_test.txt", "w", encoding="utf-8") as f:
        for review in test_reviews:
            f.write(review + "\n")
    
    print(f"Saved {len(test_reviews)} reviews to nivea_test.txt")
    
    if training_reviews:
        print(f"\nSample from training set (first 3):")
        for i, review in enumerate(training_reviews[:3]):
            print(f"Review {i+1}: {review[:100]}...")
    
    if test_reviews:
        print(f"\nSample from test set (first 3):")
        for i, review in enumerate(test_reviews[:3]):
            print(f"Review {i+1}: {review[:100]}...")
        
else:
    print("No reviews found. The products might not have reviews or the page structure is different.")
