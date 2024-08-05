from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]

styles = getSampleStyleSheet()

Title = "Hello world Heading"
pageinfo = "platypus example"
def myFirstPage(canvas, doc):
	canvas.saveState()
	canvas.setFont('Times-Bold',16)
	canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
	canvas.setFont('Times-Roman',9)
	canvas.drawString(inch, 0.75 * inch, "First Page / %s" % pageinfo)
	canvas.restoreState()
	
def go():
	doc = SimpleDocTemplate("hello-world.pdf")
	Story = [Spacer(1,1*inch)]
	style = styles["Normal"]
	text = "Hello World Text"
	p = Paragraph(text, style)
	Story.append(p)
	doc.build(Story, onFirstPage=myFirstPage)

go()
