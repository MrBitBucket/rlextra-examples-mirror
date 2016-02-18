#Autogenerated by ReportLab guiedit do not edit
from rlextra.graphics.guiedit.datacharts import CSVDataSource, ODBCDataSource, DataAssociation, DataAwareDrawing, Array
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.graphics.shapes import _DrawingEditorMixin
from reportlab.graphics.charts.lineplots import ScatterPlot
from reportlab.lib.colors import green

class ScatterPlotDrawing(_DrawingEditorMixin,DataAwareDrawing):
	def __init__(self,width=400,height=200,*args,**kw):
		DataAwareDrawing.__init__(*(self,width,height)+args, **kw)
		self.add(ScatterPlot(),'ScatterPlot')
		self.ScatterPlot.xValueAxis.labelTextFormat = '%.2f%%'
		self.ScatterPlot.xLabel="Volatility"
		self.ScatterPlot.yLabel="% Return"
		self.ScatterPlot.xValueAxis.labels.fontName = "Helvetica-Oblique"
		self.ScatterPlot.yValueAxis.labels.fontName = "Helvetica-Oblique"
		self.width = 175
		self.height = 105
		self.dataSource = CSVDataSource()
		self.dataSource.filename = 'scatterplot.csv'
		self.dataSource.sep = '\t'
		self.dataSource.integerColumns = ['chartId']
		self.dataSource.floatColumns=['Return','Volatility']
		self.dataSource.sql = 'SELECT chartId, 100*Return, 100*Volatility FROM scatterplot_data'
		self.fileNamePattern = 'scatterplot%03d'
		self.outDir = './output'
		self.formats = ['eps', 'pdf']
		self.ScatterPlot.joinedLines = 0
		self.dataSource.associations = Array(2, DataAssociation)
		self.dataSource.associations.element00 = DataAssociation(column=0, target='chartId', assocType='scalar')
		self.dataSource.associations.element01 = DataAssociation(column=[[2,1]], target='ScatterPlot.data', assocType='matrix')
		self.ScatterPlot.lineLabels[(2, 2)].dy = 3

if __name__=="__main__": #NORUNTESTS
	ScatterPlotDrawing().go()