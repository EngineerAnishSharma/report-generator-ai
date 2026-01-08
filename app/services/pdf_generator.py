# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet

# def generate_pdf(report_text: str, output_path: str):
#     styles = getSampleStyleSheet()
#     doc = SimpleDocTemplate(output_path)

#     paragraphs = []
#     for line in report_text.split("\n"):
#         paragraphs.append(Paragraph(line, styles["Normal"]))

#     doc.build(paragraphs)
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def generate_report_pdf(report: dict, output_path: str):
    """
    Generates a PDF report from a structured report dictionary.

    Args:
        report (dict): The cleaned report dictionary from LLM.
        output_path (str): Path where the PDF will be saved.
    """
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    # ----- Title -----
    elements.append(Paragraph("Analytical Report", styles["Title"]))
    elements.append(Spacer(1, 0.3 * inch))

    # ----- Summary -----
    elements.append(Paragraph("Summary", styles["Heading2"]))
    summary = report.get("summary", "")

    if isinstance(summary, dict):
        summary_text = (
            summary.get("overview")
            or summary.get("overall_insight")
            or "Summary not available"
        )
    else:
        summary_text = summary or "Summary not available"

    elements.append(Paragraph(summary_text, styles["Normal"]))
    elements.append(Spacer(1, 0.3 * inch))

    # ----- Key Metrics -----
    elements.append(Paragraph("Key Metrics", styles["Heading2"]))
    table_data = [["Metric", "Value"]]
    key_metrics = report.get("key_metrics", {})
    for key, value in key_metrics.items():
        table_data.append([key.replace("_", " ").title(), str(value)])

    if len(table_data) > 1:
        table = Table(table_data, hAlign="LEFT")
        elements.append(table)
        elements.append(Spacer(1, 0.3 * inch))
    else:
        elements.append(Paragraph("No key metrics available.", styles["Normal"]))
        elements.append(Spacer(1, 0.3 * inch))

    # ----- Recommendations -----
    elements.append(Paragraph("Recommendations", styles["Heading2"]))
    recommendations = report.get("recommendations", {})
    items = recommendations.get("action_items", [])

    if isinstance(items, str):
        elements.append(Paragraph(items, styles["Normal"]))
    elif isinstance(items, list) and items:
        for item in items:
            elements.append(Paragraph(f"- {item}", styles["Normal"]))
    else:
        elements.append(Paragraph("No recommendations provided.", styles["Normal"]))

    # ----- Build PDF -----
    doc.build(elements)

