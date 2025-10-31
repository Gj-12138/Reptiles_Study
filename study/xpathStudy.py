# lxml中的xpath
from lxml import etree

xml_doc = """
<bookstore xmlns:ns="http://test.ns" location="China">
  <book id="1" lang="zh">
    <title>Python编程入门</title>
    <author>张三</author>
    <price>50.00</price>
    <tag>hot</tag>
  </book>

  <book id="2" lang="zh">
    <title>深入理解Python</title>
    <author>李四</author>
    <price>80.00</price>
    <tag>new</tag>
  </book>

  <book id="3" lang="en">
    <title>Fluent Python</title>
    <author>Luciano Ramalho</author>
    <price>99.99</price>
    <tag>classic</tag>
  </book>

  <ns:book id="4">
    <ns:title>Namespace Book</ns:title>
  </ns:book>
</bookstore>
"""

root_doc = etree.XML(xml_doc)


# 路径

path_doc01 = root_doc.xpath("./book")
print(path_doc01)
path_doc02 = root_doc.xpath("//tag")
print(path_doc02)
path_doc03 = root_doc.xpath("../bookstore")
print(path_doc03)
path_doc04 = root_doc.xpath(".//title")
print(path_doc04)
path_doc05 = root_doc.xpath("/bookstore")
print(path_doc05)


# 属性
attrib_doc= root_doc.xpath("//*[@id]")
print(attrib_doc)
attrib_doc01= root_doc.xpath('//*[@id="4"]')
print(attrib_doc01)

attrib_doc02= root_doc.xpath('//book[3]')
print(attrib_doc02)

attrib_doc03= root_doc.xpath('//book[last()]')
print(attrib_doc03)
attrib_doc04= root_doc.xpath('//book[last()-1]')
print(attrib_doc04)

attrib_doc05= root_doc.xpath('//book[position()>1]')
print(attrib_doc05)
attrib_doc06= root_doc.xpath('//book[position()<2 or position()>3 ]')
print(attrib_doc06)
attrib_doc07= root_doc.xpath('//book[position()>=1 and position()<=3 ]')
print(attrib_doc07)

attrib_doc08= root_doc.xpath('//title[contains(text(),"Python")]')
print(attrib_doc08)
attrib_doc09= root_doc.xpath('//book[contains(@lang,"zh")]')
print(attrib_doc09)



# 取内容
attrib_doc10= root_doc.xpath('//title/text()')
print(attrib_doc10)

attrib_doc10= root_doc.xpath('//book/@id')
print(attrib_doc10)


