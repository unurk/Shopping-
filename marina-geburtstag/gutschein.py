# Erzeugt den druckbaren Gutschein (A5 quer) für Marina.
from reportlab.lib.pagesizes import A5, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

W, H = landscape(A5)
c = canvas.Canvas("gutschein_marina.pdf", pagesize=(W, H))
gun = HexColor("#5A5F66")   # Gunmetal
silver = HexColor("#A7ABB0")
c.setFillColor(HexColor("#FAFAF8")); c.rect(0, 0, W, H, fill=1, stroke=0)
c.setStrokeColor(silver); c.setLineWidth(1.2); c.rect(18, 18, W-36, H-36)
c.setLineWidth(0.4); c.rect(24, 24, W-48, H-48)

c.setFillColor(gun)
c.setFont("Helvetica-Bold", 24); c.drawCentredString(W/2, H-75, "Deine Abende. Deine Beine.")
c.setFont("Helvetica", 11); c.drawCentredString(W/2, H-95, "Gutschein zum 15. November 2026")

lines = [
    ("Helvetica-Bold", 12, "3 x Manuelle Lymphdrainage & Bewegung (je 60 min)"),
    ("Helvetica", 10, "inkl. Anleitung, wie du dein Abend-Ritual (Bürste, Hochlagern) selbst wirksamer machst"),
    ("Helvetica-Bold", 12, "1 x Test der maschinellen Lymphdrainage (40 min)"),
    ("Helvetica", 10, "damit du selbst spürst, ob so ein Gerät für zu Hause etwas für dich ist"),
    ("Helvetica-Bold", 12, "+ ich begleite dich zur ärztlichen Abklärung, wenn du magst"),
]
y = H-135
for font, size, text in lines:
    c.setFont(font, size); c.drawCentredString(W/2, y, text); y -= 20 if size == 12 else 26

c.setFont("Helvetica-Oblique", 10)
c.drawCentredString(W/2, 70, "Du suchst Termin und Therapeutin aus, ich zahle. Kein Ablaufdatum.")
c.setFont("Helvetica-Bold", 12); c.drawCentredString(W/2, 48, "Von Unur")
c.showPage(); c.save()
