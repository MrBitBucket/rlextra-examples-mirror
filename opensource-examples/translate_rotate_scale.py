import os

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


MEDIA_DIR = "media"


def transformations(canvas):
    """Setting transformations apply to all the images that come after, so you must invert them to add normally again"""
    logo = os.path.join(MEDIA_DIR, 'reportlab.png')
    canvas.setFont("Helvetica", 20, leading = None)
    # Translate
    canvas.drawString(x=30, y=780, text="Translate")
    canvas.drawInlineImage(image=logo, x=100, y=700, width=50, height=50)
    canvas.translate(dx=55, dy=0) #Adding transformation so you can see the underlying image
    canvas.drawInlineImage(image=logo, x=100, y=700, width=50, height=50)
    canvas.translate(dx=-55, dy=0) #Adding transformation so you can see the underlying image

    # Rotate
    # It's rotating around the page origin 0, 0. So we must translate to the image location first so we rotate around it
    canvas.drawString(x=30, y=580, text="Rotate")
    canvas.drawInlineImage(image=logo, x=100, y=500, width=50, height=50)
    # Rotate clockwise 90
    canvas.translate(dx=100, dy=500)
    canvas.rotate(-90)
    canvas.translate(dx=-100, dy=-500)
    canvas.drawInlineImage(image=logo, x=100, y=500, width=50, height=50)
    # Rotate anticlockwise 90
    canvas.translate(dx=100, dy=500)
    canvas.rotate(90)
    canvas.translate(dx=-100, dy=-500)

    # Scale
    # Also applies to x and y value, so this should be combined with translate. The image has same parameters each time.
    canvas.drawString(x=30, y=380, text="Scale")
    canvas.drawInlineImage(image=logo, x=100, y=180, width=50, height=50)
    canvas.scale(1.5, 1.5)
    canvas.drawInlineImage(image=logo, x=100, y=180, width=50, height=50)
    canvas.scale(1/1.5, 1/1.5)


def go():
    c = canvas.Canvas("translate_rotate_scale.pdf", pagesize=A4) # 595 x 842 is the page dimensions for A4 at 72DPI
    transformations(canvas=c)
    c.showPage()
    c.save()


go()