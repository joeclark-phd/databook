# Plumbing the Big Data Pipeline
(c) 2015 by Joseph Clark

These are my course notes (under development) for CIS 355, "Business Data Warehouses and Dimensional Modeling", which I have conceived -- more broadly than the name implies -- as a data engineering class that looks at the whole pipeline from data ingest to transformation, loading into databases, and serving to the world via applications and services.

Feel free to use this for education and training purposes, as long as you give me credit.

[![Stories in Ready](https://badge.waffle.io/joeclark-phd/databook.svg?label=ready&title=Ready)](http://waffle.io/joeclark-phd/databook)

## Compiling

The book is prepared using LaTeX markup. Because I'm using the `minted` package, which executes syntax highlighting on code blocks, I need to compile the code with the following command on Windows:

    pdflatex -shell-escape databook.tex

You may need to compile the code two or three times for the references and table of contents to be correctly rendered in the PDF.