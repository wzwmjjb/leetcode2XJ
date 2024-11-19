import json
import requests
import time

with open("assets/chosen_urls.txt", "r", encoding="utf-8") as file:
    problem_urls = file.read().splitlines()

problems_data = []

GRAPHQL_QUERY = """
query getQuestionDetail($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    translatedTitle
    translatedContent
    difficulty
  }
}
"""

HEADERS = {
    "Content-Type": "application/json",
    "Referer": "https://leetcode.cn/problems",
    "Origin": "https://leetcode.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
}

for url in problem_urls:
    title_slug = url.split("/")[-1]
    graphql_url = "https://leetcode.cn/graphql/"

    payload = {
        "operationName": "getQuestionDetail",
        "variables": {"titleSlug": title_slug},
        "query": GRAPHQL_QUERY,
    }

    try:
        response = requests.post(graphql_url, headers=HEADERS, json=payload)
        response_data = response.json()

        question = response_data["data"]["question"]
        problem_data = {
            "id": question["questionFrontendId"],
            "title": question["translatedTitle"],
            "slug": title_slug,
            "url": url,
            "difficulty": question["difficulty"],
            "description": question["translatedContent"],
        }

        problems_data.append(problem_data)
        print(f"Fetched: {problem_data['title']} - {url}")

        time.sleep(0.5)

    except Exception as e:
        print(f"Failed to fetch data for {url}: {e}")

with open("assets/chosen_problems_raw.json", "w", encoding="utf-8") as json_file:
    json.dump(problems_data, json_file, ensure_ascii=False, indent=4)

print("All problems have been saved to 'assets/chosen_problems_raw.json'")
