# Druckbare Karte (A5 quer) fuer Marina: "Silberabend".
from reportlab.lib.pagesizes import A5, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

W, H = landscape(A5)
c = canvas.Canvas("karte_marina.pdf", pagesize=(W, H))
gun, silver = HexColor("#4E535A"), HexColor("#A7ABB0")
c.setFillColor(HexColor("#F7F7F5")); c.rect(0, 0, W, H, fill=1, stroke=0)
c.setStrokeColor(silver); c.setLineWidth(1.2); c.rect(18, 18, W-36, H-36)
c.setLineWidth(0.4); c.rect(24, 24, W-48, H-48)
c.setFillColor(gun)
c.setFont("Helvetica-Bold", 26); c.drawCentredString(W/2, H-80, "Silberabend")
c.setFont("Helvetica", 11); c.drawCentredString(W/2, H-100, "15. November 2026")
y = H-150
for font, size, text in [
    ("Helvetica", 12, "Gut für jeden Sonntagabend, solange du willst:"),
    ("Helvetica-Bold", 14, "Beine hoch, Decke drüber, Handy in der Hand."),
    ("Helvetica-Bold", 14, "Ich massiere dir die Beine mit deinem Öl."),
    ("Helvetica", 12, "So sanft, wie du es magst. Du bestimmst."),
]:
    c.setFont(font, size); c.drawCentredString(W/2, y, text); y -= 26
c.setFont("Helvetica-Bold", 12); c.drawCentredString(W/2, 50, "Von Unur")
c.showPage(); c.save()
