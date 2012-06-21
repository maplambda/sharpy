sharpy
======

html elements represented as functions

Sharpy is an experimental dsl for writing html/xml in Python. Sharpy uses function closures and lists to build html documents.

See tests for examples.

Quickstart:

```python
h = html()
page = h.html()([
    h.head()([h.title()('Title')]),
    h.body()([
        h.h1()('htmlgen')]),
        h.p(id='intro')('a paragraph generated by the htmlgen dsl')
    ])
```

print h.dumps(page)

Todo:
* html escaping
* pretty/ minify output options
* tidy the parser
* benchmarking

Pull requests welcome.