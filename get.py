import requests
import bs4 as bs
import re
import os

def main(url):
    r = requests.get(url=url)

    soup = bs.BeautifulSoup(r.text, 'html.parser')

    title = soup.select_one("div.question-title h3").text
    filename = "{}-{}.py".format(title.split(".")[0], title.split(".")[1].replace(" ", ""))

    rawCode = soup.find("div", attrs={"ng-controller": "AceCtrl as aceCtrl"}).attrs["ng-init"]
    pattern = "\\'text\\':\s\\'Python\\',\s\\'defaultCode\\':\s\\'(.*?)\\'"

    content = re.search(pattern, rawCode).group(1).\
              encode("utf-8").decode("unicode-escape").\
              replace("\r\n", "\n")

    filepath = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "code", filename)

    with open(filepath, "w") as f:
        f.write("# Link: {}\n".format(url))
        f.write(content)

    print("Wrote to {}!".format(filepath))


if __name__ == '__main__':
    import clime.now
