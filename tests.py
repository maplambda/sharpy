import unittest
import sharpy

class TestHtml(unittest.TestCase):

    def test_element(self):
        h = sharpy.html()
        page = h.html()('An empty page')

        html = '''<html>
An empty page
</html>'''
        self.assertEqual(html, h.dumps(page))

    def test_nested_element(self):
        h = sharpy.html()
        page = h.html()([
            h.body()("Body text")])

        html = '''<html>
<body>
Body text
</body>
</html>'''
        self.assertEqual(html, h.dumps(page))    

    def test_element_attributes(self):
        h = sharpy.html()
        page = h.p(id='intro', _class="intro")('Intro paragraph')

        html = '''<p class="intro" id="intro">
Intro paragraph
</p>'''
        self.assertEqual(html, h.dumps(page))    


    def test_href(self):
        h = sharpy.html()
        page = h.a(href='https://github.com/maplambda/sharpy')('sharpy')

        html = '''<a href="https://github.com/maplambda/sharpy">
sharpy
</a>'''
        self.assertEqual(html, h.dumps(page))

    def test_multiple_nested_elements(self):
        h = sharpy.html()
        page = h.html()([
            h.body()([
                h.h1()('sharpy'),
                h.p(id='intro')('Intro paragraph')])
            ])

        html = '''<html>
<body>
<h1>
sharpy
</h1>
<p id="intro">
Intro paragraph
</p>
</body>
</html>'''
        self.assertEqual(html, h.dumps(page))    

if __name__ == '__main__':
    unittest.main()
