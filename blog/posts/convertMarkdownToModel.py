import markdown as md
import codecs
input = codecs.open("testing_post.md", mode="r")
text = input.read()
html = md.markdown(text)
from bs4 import BeautifulSoup as bs
html = bs(html)
print(html.find("h1").get_text())
