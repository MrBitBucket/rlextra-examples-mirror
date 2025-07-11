"""
create one page performance report
"""
import sys, os, datetime, preppy
from rlextra.rml2pdf import rml2pdf
from utils import OurBook
from utils import getHere, registerFonts

def generate_pdf(workbook_file_name, options):
    here = getHere()
    output = os.path.abspath(options.output)
    if not os.path.isdir(output):
        os.makedirs(output,0o755)

    #wrap it up in something friendlier
    data = None

    #make a dictionary to pass into preppy as its namespace.
    #you could pass in any Python objects or variables,
    #as long as the template expressions evaluate
    ns = dict(data=data, format="long" if options.longformat else "short")

    #we usually put some standard things in the preppy namespace
    ns['DATE_GENERATED'] = datetime.date.today()
    ns['showBoundary'] = "1" if options.showBoundary else "0"
    ns['here'] = here

    #let it know where it is running; trivial in a script, confusing inside
    #a big web framework, may be used to compute other paths.  In Django
    #this might be relative to your project path,
    ns['RML_DIR'] = os.path.join(here, 'rml')

    #we tend to keep fonts in a subdirectory.  If there won't be too many,
    #you could skip this and put them alongside the RML
    FONT_DIR = ns['FONT_DIR'] = os.path.join(ns['RML_DIR'], 'fonts')
    registerFonts()
    IMAGES_DIR = ns['IMAGES_DIR'] = os.path.join(ns['RML_DIR'], 'images')
    b = ns['ourbook'] = OurBook(workbook_file_name)
    SN = [n for n in b.workbook.sheet_names() if n != 'Data for each Product Graph']

    #We tell our template to use Preppy's standard quoting mechanism.
    #This means any XML characters (&, <, >) will be automatically
    #escaped within the prep file.
    template = preppy.getModule('template.prep',ns['RML_DIR'],savePyc=False)
    #this hack will allow rmltuils functions to 'know' the default quoting mechanism
    #try:
    #   import builtins as __builtin__
    #except:
    #   import __builtin__
    #__builtin__._preppy_stdQuote = preppy.stdQuote
    for n in SN:
        file_name_root =  os.path.join(output,'-'.join(filter(None,n.split())))
        ns['prname'] = n

        rmlText = template.getOutput(ns, quoteFunc=preppy.stdQuote)

        if options.saverml:
            #It's useful in development to save the generated RML.
            #If you generate some illegal RML, pyRXP will complain
            #with the exact line number and you can look to see what
            #went wrong.  Once running, no need to save.  Within Django
            #projects we usually have a settings variable to toggle this
            #on and off.
            rml_file_name = file_name_root + '.rml'
            open(rml_file_name, 'w').write(rmlText)
        pdf_file_name = file_name_root + '.pdf'

        #convert to PDF on disk.  If you wanted a PDF in memory,
        #you could pass a StringIO to 'outputFileName' and
        #retrieve the PDF data from it afterwards.
        rml2pdf.go(rmlText, outputFileName=pdf_file_name)
        print('saved %s' % pdf_file_name)

if __name__=='__main__':
    from optparse import OptionParser
    usage = "usage: runme.py [--long] myfile.xlsx"
    parser = OptionParser(usage=usage)
    parser.add_option("-l", "--long",
                      action="store_true", dest="longformat", default=False,
                      help="Do long profile (rather than short)")
    parser.add_option("-r","--rml",
                      action="store_true", dest="saverml", default=False,
                      help="save a copy of the generated rml")
    parser.add_option("-s","--showb",
                      action="store_true", dest="showBoundary", default=False,
                      help="turn on global showBoundary flag")
    parser.add_option("-o", "--output",
                      action="store", dest="output", default='output',
                      help="where to store result")

    options, args = parser.parse_args()

    if len(args) != 1:
        print(parser.usage)
    else:
        filename = args[0]
        generate_pdf(filename, options)

    #generate_pdf('cv_data.json')
