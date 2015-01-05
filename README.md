# Hundo Wiki: a wiki in less than a hundred lines of code

The goal here was to make a really, really simple wiki in less than a hundred lines of Python code. The goal was achieved; depending on how you count, this uses either 54 lines (including blank lines, comments, etc.) or significantly less if you only count lines of actual code. It wasn't meant to be especially clear, but neither was it meant to be confusing. It stores wiki pages in text files in the `pages/` directory, shows them by URL, and auto-links anything that looks like a WikiWord in that nice CamelCase style. It uses Flask, but aside from that, has no other dependencies.

    $ pip install flask
    $ python wiki.py
     * Running on http://127.0.0.1:5000/

If there's a moral to this story, it is that wiki software is kind of ridiculously easy to make if you're not overly worried about its quality or usability.
