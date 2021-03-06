# -*- coding: utf-8 -*-
"""
    sphinxcontrib-reviewbuilder
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2013 by the WAKAYAMA Shirou
    :license: LGPLv2, see LICENSE for details.
"""

from __future__ import absolute_import

from docutils.nodes import Text, paragraph

from sphinxcontrib.reviewbuilder.reviewbuilder import ReVIEWBuilder


# from japanesesupport.py
def trunc_whitespace(app, doctree, docname):
    for node in doctree.traverse(Text):
        if isinstance(node.parent, paragraph):
            newtext = node.astext()
            for c in "\n\r\t":
                newtext = newtext.replace(c, "")
            newtext = newtext.strip()
            node.parent.replace(node, Text(newtext))


def setup(app):
    app.add_builder(ReVIEWBuilder)
    app.connect("doctree-resolved", trunc_whitespace)
