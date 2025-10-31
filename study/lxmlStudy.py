"""

    xml

"""
from lxml import etree

xml_content = """
<library>
  <book id="1">
    <title>Python编程入门</title>
    <author>张三</author>
    <price>50.00</price>
  </book>
  <book id="2">
    <title>深入理解Python</title>
    <author>李四</author>
    <price>80.00</price>
  </book>
</library>
"""

tree = etree.XML(xml_content)
# print(type(tree))
print(dir(tree))

doc  = tree.find('book')
print(doc.attrib,"find")

docs = tree.findall('book')
for doc in docs:
    print(doc.attrib,"findall")

childrens_doc = tree.getchildren()
for child in childrens_doc:
    print(child.attrib,"getchildren")
    print(child.tag,"getchildren")

# cssselect
cssselect_doc = tree.cssselect('book')
for books in cssselect_doc:
    print(books.attrib,"cssselect")
    print(books.tag,"cssselect")
    book= books.cssselect('title')
    print(book[0].text,"cssselect02")




"""

    html

"""
html_content = """
<html>
  <body>
    <h1>欢迎来到我的网站</h1>
    <ul>
      <li><a href="https://example.com/page1">页面一</a></li>
      <li><a href="https://example.com/page2">页面二</a></li>
    </ul>
  </body>
</html>
"""





