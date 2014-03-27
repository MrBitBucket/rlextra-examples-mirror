==================
ReportLab PLUS Examples
==================

This contains runnable examples for our commercial PDF library, ReportLab PLUS.
It should help you get up and running and creating your own PDF document layouts
quickly.   

We strongly suggest you start by skimming through the RML User Guide:
    
    https://www.reportlab.com/software/documentation/


Current contents:

- Product Catalogue Tutorial
- RML test suite


Product Catalogue Tutorial
==========================

This is an example taken from a real world solution to create a catalogue for a business delivering seasonal wild meats.  It demonstrates how to create attractive
listings using our preppy templating system and Report Markup Language.  Most people will be using this kind of workflow, with a templating system to handle
loops/conditionals/variables, embedded in an RML document to control the formatting.

To try it::
 	cd product_catalogue
 	python product_catalog.py

Look at the output files in output/, then the main script, then the .prep file which controls the layout.  Feel free to make some edits


RML samples
===========
We include a full copy of our own internal RML test suite.  These files can also be seen, with their output, on our own web site:

   https://www.reportlab.com/software/documentation/rml-samples/

You should be able to convert any of them with the installed 'rml2pdf' command.
For example::

   $ rml2pdf test_001_hello.rml
   test_001_hello.pdf

    
