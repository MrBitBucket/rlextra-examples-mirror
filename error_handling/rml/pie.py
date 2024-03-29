#Autogenerated by ReportLab guiedit do not edit
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin
from reportlab.graphics.charts.piecharts import Pie

class PieChart(_DrawingEditorMixin,Drawing):
	def __init__(self,width=400,height=200,*args,**kw):
		Drawing.__init__(self,width,height,*args,**kw)
		self.width       = 60
		self.height      = 60
		self._add(self,Pie(),name='Pie',validate=None,desc=None)
		self.Pie.height              = 60
		self.Pie.width               = 60

if __name__=="__main__": #NORUNTESTS
	PieChart().save(formats=['pdf'],outDir='.',fnRoot=None)