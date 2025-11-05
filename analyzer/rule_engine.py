from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_block_rules(suspicious_ips, output_file="text.pdf"):
    c = canvas.Canvas(output_file, pagesize=letter)
    text = c.beginText(40,750)
    text.setFont("Helvetica",12)

    text.textLine("Firewall Block Rules")
    text.textLine("---------------")

    for ip, count in suspicious_ips.items():
        text.textLine(f"set rulebase security rules Block-IP-{ip}")
        text.textLine(f"    source {ip} destination any application any service any")
        text.textLine("    action deny")
        text.textLine("")
        

    c.drawText(text)
    c.save()

    return output_file