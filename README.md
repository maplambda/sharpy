sharpy
======

html elements represented as functions

Sharpy is an experimental dsl for writing html/xml in Python. Sharpy uses function closures and lists to build html documents.

See tests for examples.

Quickstart:

h = html()
page = h.html()([
    h.head()([h.title()('Title')]),
    h.body()([
        h.h1()('htmlgen')]),
        h.p(id='intro')('a paragraph generated by the htmlgen dsl')
    ])

print h.dumps(page)

Todo:
* html escaping 
* tidy the parser
* pluggable parsers
* benchmarking

Pull requests welcome.