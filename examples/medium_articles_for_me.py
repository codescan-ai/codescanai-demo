import requests
from bs4 import BeautifulSoup
import urllib.parse

def search_medium_articles(query):
    search_query = urllib.parse.quote(query + " site:medium.com")
    search_url = f"https://www.google.com/search?q={search_query}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    
    response = requests.get(search_url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to retrieve search results.")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = []

    for h3_tag in soup.find_all('h3'):
            title = h3_tag.text
            results.append(title)
    
    return results

def main():
    interest = input("Enter your interest: ")
    print(f"Searching for Medium articles related to '{interest}'...")
    
    articles = search_medium_articles(interest)
    
    if articles:
        print("\nFound articles:")
        for idx, article in enumerate(articles, start=1):
            print(f"{idx}. {article}")
    else:
        print("No articles found.")

if __name__ == "__main__":
    main()
