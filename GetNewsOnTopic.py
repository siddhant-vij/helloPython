# Here are the user stories implemented:

# Topic-Based News Search:
# 1. As a user, I want to enter a specific topic so that I can view the top 10 news articles related to that topic, irrespective of their publication date.
# 2. As a user, I want to see news articles that are relevant to my search query so that I can get the most pertinent information.

# Source Selection:
# 1. As a user, I want the option to specify a particular news source so that I can get articles from my preferred media outlet.
# 2. As a user, I want to see a list of available news sources so that I can choose a valid source for my news articles.
# 3. As a user, I want to be informed if I enter an invalid source so that I can choose a valid one or proceed without specifying a source.

# Top Headlines:
# 1. As a user, I want the option to view the top news headlines in my country for the current day so that I can stay updated with the most recent and important news events locally.
# 2. As a user, I want to specify my country using a country code so that I can get the top headlines tailored to my region.

# Error Handling and Feedback:
# 1. As a user, I want to be informed if there's an error fetching news so that I know if there's an issue with the system or the API.
# 2. As a user, I want to be informed if no articles are found for my topic or country so that I can try a different search or check back later.

# User-Friendly Interface:
# 1. As a user, I want clear prompts and instructions in the command-line interface so that I can easily navigate and use the program.
# 2. As a user, I want to see a concise description and a link to the full article for each news item so that I can get a quick overview and decide if I want to read more.

import requests
from datetime import datetime

API_ENDPOINT = "https://newsapi.org/v2/everything"
TOP_HEADLINES_ENDPOINT = "https://newsapi.org/v2/top-headlines"
SOURCES_ENDPOINT = "https://newsapi.org/v2/top-headlines/sources"
API_KEY = "YOUR_API_KEY"  # Replace with your API key


def get_sources():
    params = {
        "apiKey": API_KEY
    }
    response = requests.get(SOURCES_ENDPOINT, params=params)
    if response.status_code != 200:
        return []
    sources_data = response.json()
    return [source["id"] for source in sources_data.get("sources", [])]


def fetch_top_headlines(country):
    current_date = datetime.now().strftime('%Y-%m-%d')

    params = {
        "country": country,
        "apiKey": API_KEY,
        "pageSize": 10,
        "from": current_date,
        "to": current_date
    }

    response = requests.get(TOP_HEADLINES_ENDPOINT, params=params)

    if response.status_code != 200:
        print("Error fetching top headlines. Please try again later.")
        return

    news_data = response.json()
    articles = news_data.get("articles", [])

    if not articles:
        print("No top headlines found for the given country.")
        return

    for idx, article in enumerate(articles, 1):
        title = article["title"]
        description = article["description"]
        url = article["url"]
        print(f"{idx}. {title}\n   {description}\n   Read more: {url}\n")


def fetch_news(topic, source=None):
    params = {
        "q": topic,
        "apiKey": API_KEY,
        "pageSize": 10,
        "page": 1
    }

    if source:
        params["sources"] = source

    response = requests.get(API_ENDPOINT, params=params)
    if response.status_code != 200:
        print("Error fetching news. Please try again later.")
        return

    news_data = response.json()
    articles = news_data.get("articles", [])

    if not articles:
        print("No articles found for the given topic.")
        return

    for idx, article in enumerate(articles, 1):
        title = article["title"]
        description = article["description"]
        url = article["url"]
        print(f"{idx}. {title}\n   {description}\n   Read more: {url}\n")


def main():
    top_headlines_choice = input(
        "Do you want the top news in your country? (yes/no): ").lower()
    if top_headlines_choice == 'yes':
        country = input(
            "Enter your country code (e.g., 'us' for the United States, 'in' for India): ")
        fetch_top_headlines(country)
    else:
        topic = input("Enter a topic to fetch news: ")
        source_choice = input(
            "Do you want to specify a news source? (yes/no): ").lower()
        source = None
        if source_choice == 'yes':
            available_sources = get_sources()
            print("Available sources are:", ", ".join(available_sources))
            source = input("Enter your preferred source from the list above: ")
            if source not in available_sources:
                print("Invalid source. Fetching from all sources.")
                source = None
        fetch_news(topic, source)


if __name__ == "__main__":
    main()
