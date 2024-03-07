Product Catalogue Example
--------------------------

XML product listing converted to a fully customisable PDF in seconds.
---------------------------------------------------------------------


This example is aimed at showing the use of Report Markup Language (RML), which is a component of our commercial tool-kit. All you need to do to download a full evaluation copy is `sign in`_ or `register on our site`_; then, follow the installation instructions to get yourself set up. Once these are completed, you're ready to go.

.. _sign in: https://www.reportlab.com/accounts/login/
.. _register on our site: http://www.reportlab.com/accounts/register/


Run the example
--------------

To see the output, run product_catalog.py and look at the generated file under /output.


How is the PDF generated?
-------------------------

The main script lives in prodcut_catalog.py, this is just a Python module which starts by pulling in data from an XML file, then uses a Rlextra utility function to first render a RML file from template filled in by the data, then use the rendered RML to produce a PDF. RML is the markup language use to describe the desired PDF document. The template itself uses Preppy, a Python pre-processor used to output valid RML. Preppy is just Python and therefore quite powerful. 

.. code:: python
from rlextra.rml2pdf import rml2pdf

    #generate the RML file from the preppy template
    rml = template.getOutput(dict(products=some_data))
    open(os.path.join(DATA_DIR,'latest.rml'), 'w').write(rml)
    buf = StringIO.StringIO()
	#write the rml into a pdf file using rml2pdf
    rml2pdf.go(rml, outputFileName=buf)
    return buf.getvalue()


Preppy - a PreProcessor for Python
----------------------------------

Preppy is ReportLab's templating system. It has been in continuous production use since 2000.

It was released as open source code but never evangelized. We are putting it out on PyPI now because many of our solutions depend on it, and this makes it a lot easier to install (e.g. with a pip requirements file).

Preppy is a single Python module which should be placed directly on the path (i.e. you access it with 'import preppy'). The setup script does this, but it's just as effective to grab it from the repo and drop it into your project.

Preppy aims to be absolutely minimal. You embed Python expressions and control structures in your template. It compiles the template into a .pyc file. A preppy template is exactly equivalent to a Python function which accepts parameters and returns text output. We don't both with include functions, block nesting, filters or any other fancy stuff, because we already have a perfectly good language to do that in.

Preppy is just Python, so you get proper Python tracebacks, with the original line number in the .prep file; you can happily debug through calls to python, preppy, python and more preppy.


.. code:: python
<story>  
  
    <para style="h1"> Product Availability </para>  
    <para style="h2">{{today.strftime('%d %B %Y')}}</para>  
  
    {{for prod in products}}  
        <para style="prod_name">{{i(prod.name)}}</para>  
    {{endfor}}  
  
</story> 


What is Report Markup Language?
-------------------------------

Report Markup LanguageTM (RML) is ReportLab's direct-to-PDF document formatting solution. We defined a Markup Language which describes the exact appearance of a printed document; and a software component, RML2PDF, which converts RML into PDF files. Report Markup Language describes the precise layout of a printed document, and RML2PDF converts this to a finished document in one step.


What does a RML file look like?
-------------------------------

A RML file will in most cases contain the following three sections: a template, a stylesheet and a story. 

The template tells rml2pdf what should be on the page: headers, footers, any graphic elements you use as a background. It is the section where the layout of a document is set out - both for the whole document and for individual pages within it.

The stylesheet is where the styles for a document are set. This tells the parser what fonts to use for paragraphs and paragraph headers, how to format tables and other things of that nature.

The story is where the "meat" of the document is. Just like in a newspaper, the story is the bit you want people to read, as opposed to design elements or page markup. As such, this is where headers, paragraphs and the actual text is contained.

.. code:: xml

<!DOCTYPE document SYSTEM "rml.dtd">
<document filename="example_2.pdf">
    <template>
        <pageTemplate id="main">
            <frame id="first" x1="72" y1="72" width="451" height="698"/>
        </pageTemplate>
</template>
    <stylesheet>

    <paraStyle name="h1"
               fontName="Courier-Bold"
               fontSize="12"
               spaceBefore="0.5 cm"
               />
    </stylesheet>
    <!-- The story starts below this comment -->
    <story>
        <para style="h1">
            This is the "story". This is the part of the RML document where
            your text is placed.
        </para>
        <para>
            It should be enclosed in "para" and "/para" tags to turn it into
paragraphs.
        </para>
    </story>
</document>


RML basics
----------

RML allows you to use comments in the RML code. These are not displayed in the output PDF file. Just like in HTML, they start with a "<!--" and are terminated with a "-->". Unlike other tags, comments cannot be nested. In fact, you can't even have the characters "--" inside the <!-- --> section.

<template> allows you to set options for the whole document. The <pageTemplate> tag allows you to set options for individual pages. You can have more than one<pageTemplate> inside the template section. This allows you to have different pageTemplates for each page that requires a different structure. For example, the title page of a report could have a number of graphics on it while the rest of the pages are more text-orientated.

Just like in a word processor, RML allows you to define a stylesheet at the start of your document, and then apply it to paragraphs later on. This means that you can define a complicated mixture of settings that you want to apply to paragraphs, only define it in one place, and refer to it with a simple name at the start of each paragraph rather than having to type or cut-and-paste large blocks of text over and over for each paragraph.

For more info, please take a look at the `official documentation`_

.. _official documentation: https://www.reportlab.com/docs/rml2pdf-userguide.pdf
