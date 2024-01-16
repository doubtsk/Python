import requests


def getHtml(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
    except requests.exceptions.Timeout:
        print("请求超时")
    except requests.exceptions.HTTPError as e:
        print(f"请求失败: {e}")
    except Exception as e:
        print(f"发生异常: {e}")


def main():
    getHtml("https://www.github.com")

main()
