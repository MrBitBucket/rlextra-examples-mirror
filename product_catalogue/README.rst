Product Catalogue Example
--------------------------

XML product listing converted to a fully customisable PDF in seconds.
---------------------------------------------------------------------


This example is aimed at showing the use of Report Markup Language (RML), which is a component of our commercial tool-kit. All you need to do to download a full evaluation copy is `sign in`_ or `register on our site`_; then, follow the installation instructions to get yourself set up. Once these are completed, you're ready to go.

.. _sign in: https://www.reportlab.com/accounts/login/
.. _register on our site: http://www.reportlab.com/accounts/register/


Run the exampe
--------------

To see the output, run product_catalog.py and look at the generated file under /output.


How is the PDF generated?
-------------------------

The main script lives in prodcut_catalog.py, this is just a Python module which starts by pulling in data from an XML file, then uses a Rlextra utility function to first render a RML file from template filled in by the data, then use the rendered RML to produce a PDF. RML is the markup language use to describe the desired PDF document. The template itself uses Preppy, a Python pre-processor used to output valid RML. Preppy is just Python and therefore quite powerful. 

.. code:: python
    #generate the RML file from the preppy template
    rml = template.getOutput(dict(products=some_data))
    open(os.path.join(DATA_DIR,'latest.rml'), 'w').write(rml)
    buf = StringIO.StringIO()
	#write the rml into a pdf file
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

Report Markup LanguageTM (RML) is ReportLab's direct-to-PDF document formatting solution. It addresses key shortcomings in the marketplace for reporting and document generating tools, and has proven itself in demanding mission-critical solutions with some of the world's largest financial houses. And it's the natural reporting tool for XML workflows!

The idea is extremely simple. Developers everywhere have plenty of tools for generating data-driven HTML. We defined a Markup Language which describes the exact appearance of a printed document; and a software component, RML2PDF, which converts RML into PDF files. (We also have some very powerful and simple tools to help generate the RML, in case you don't). 

In the process, we have made it as easy to generate PDF as it is to generate HTML. This is not only the most flexible solution possible; it's also easy to deploy, and completely natural and straightforward for developers.
