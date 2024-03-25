import argparse
import urllib.robotparser
from urllib.parse import urlparse

def can_fetch(url, user_agent='*'):
    parsed_url = urlparse(url)
    robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
    
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robots_url)
    rp.read()

    return rp.can_fetch(user_agent, url)

def main(urls_file):
    with open(urls_file, "r") as file:
        for url in file:
            url = url.strip()  # 余分な空白や改行を削除
            if url:  # URLが空でない場合
                if can_fetch(url):
                    print(f"Fetching is allowed for URL: {url}")
                else:
                    print(f"Fetching is disallowed for URL: {url}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check if URLs can be fetched according to their robots.txt.')
    parser.add_argument('urls_file', type=str, help='A file containing URLs to check.')
    
    args = parser.parse_args()

    main(args.urls_file)

