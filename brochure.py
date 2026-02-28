from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

c = canvas.Canvas("brochure.pdf", pagesize=A4)
c.setFont("Helvetica-Bold", 20)
c.drawString(50, 800, "My Brochure Title")
# … more content/graphics …
c.save()
