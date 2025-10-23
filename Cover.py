from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER

# Output PDF file
pdf_path = "Anshu_Sharma_Cover_Letter.pdf"

# Create the document
doc = SimpleDocTemplate(pdf_path, pagesize=LETTER,
                        rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name='Left', alignment=TA_LEFT))
styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))

Story = []

header = """
<b>Anshu Sharma</b><br/>
Ghaziabad, Uttar Pradesh<br/>
📧 anshusharma5.as@gmail.com<br/>
🔗 linkedin.com/in/anshu-sharma-b74a07221<br/>
💻 github.com/SharmAnshu5<br/>
<br/>
Date: October 11, 2025<br/><br/>
"""

body = """
<b>To,</b><br/>
The Hiring Manager<br/>
<b>Amar Ujala / (or Company Name)</b><br/>
Subject: Application for Software Developer / AI & Automation Engineer<br/><br/>

Dear Hiring Manager,<br/><br/>

I am writing to express my keen interest in the <b>Software Developer and AI & Automation Engineer</b> role at <b>Amar Ujala</b>. 
As a B.Tech student in <b>Computer Science with specialization in Artificial Intelligence</b>, 
I bring hands-on experience in <b>AI model development, RPA automation, and full-stack implementation</b> that aligns with your organization’s vision of technological excellence.<br/><br/>

During my full-time role in the <b>Technical Team at Amar Ujala</b>, I worked on an <b>RPA automation project</b> designed to streamline manual workflows and enhance operational efficiency. 
My experience also includes developing <b>AI-driven diagnostic systems</b> such as <i>Insu Scan Pro</i> (a diabetes prediction and medical report summarization tool) 
and <i>See Beneath</i> (an underwater object detection model). 
These projects demonstrate my ability to design scalable, production-grade solutions using <b>Python, FastAPI, Streamlit, React, and deep learning frameworks</b>.<br/><br/>

Previously, as an <b>AI/ML & Data Science Intern at Inventia</b>, I gained strong experience in data preprocessing, model optimization, and deployment—helping bridge the gap between raw data and actionable intelligence.<br/><br/>

I am confident that my blend of <b>AI expertise, software development skills, and automation focus</b> would make me a strong addition to your team. 
I am deeply motivated to contribute to innovative, impactful solutions at scale.<br/><br/>

Thank you for considering my application. 
I look forward to the opportunity to discuss how my technical background can contribute to your team’s success.<br/><br/>

Warm regards,<br/>
<b>Anshu Sharma</b><br/>
📧 anshusharma5.as@gmail.com<br/>
🔗 linkedin.com/in/anshu-sharma-b74a07221<br/>
💻 github.com/SharmAnshu5
"""

Story.append(Paragraph(header, styles["Left"]))
Story.append(Paragraph(body, styles["Justify"]))

doc.build(Story)

print(f"✅ Cover Letter generated successfully: {pdf_path}")
