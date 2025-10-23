from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics

# Register font for Unicode compatibility
pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))

# File path
pdf_path = "C:/Anshu/Automation"

# Document setup
doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                        rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Header', fontName='HeiseiMin-W3', fontSize=14, leading=18, spaceAfter=6, alignment=1, textColor=colors.HexColor('#1a1a1a')))
styles.add(ParagraphStyle(name='SubHeader', fontName='HeiseiMin-W3', fontSize=11, leading=16, spaceAfter=4, textColor=colors.HexColor('#2b2b2b')))
styles.add(ParagraphStyle(name='Body', fontName='HeiseiMin-W3', fontSize=10, leading=14, spaceAfter=6))
styles.add(ParagraphStyle(name='SectionHeader', fontName='HeiseiMin-W3', fontSize=11, leading=14, spaceAfter=4, textColor=colors.HexColor('#004080'), underlineWidth=0.5))

content = []

# Header
header = Paragraph("<b>Anshu Sharma</b>", styles['Header'])
contact_info = Paragraph("📧 anshusharma5.as@gmail.com | 🌐 <u>https://sharmanshu5.github.io/Portfolio/</u><br/>"
                         "💼 <u>linkedin.com/in/anshu-sharma-b74a07221</u> | 💻 <u>github.com/SharmAnshu5</u><br/>"
                         "📍 Ghaziabad, Uttar Pradesh", styles['SubHeader'])
content += [header, contact_info, Spacer(1, 8), HRFlowable(width="100%", color=colors.HexColor('#004080')), Spacer(1, 12)]

# Professional Summary
content += [Paragraph("<b>Professional Summary</b>", styles['SectionHeader']),
            Paragraph("Dedicated Software Developer & AI Automation Engineer with hands-on experience in Artificial Intelligence, Machine Learning, and Robotic Process Automation (RPA). Currently part of Amar Ujala’s Technical Team, contributing to intelligent automation projects that streamline workflows and enhance efficiency. Experienced in developing full-stack AI applications with Python, FastAPI, Streamlit, React, and modern ML frameworks.", styles['Body'])]

# Experience Section
content += [Paragraph("<b>Professional Experience</b>", styles['SectionHeader'])]

experience_data = [
    ["<b>Software Developer & AI Automation Engineer — Amar Ujala</b><br/><i>Aug 2025 – Present | Full-Time | Technical Team</i><br/>"
     "- Building and deploying RPA systems to optimize workflows.<br/>- Developing AI-driven automation pipelines using Python, Selenium, and FastAPI.<br/>- Collaborating with cross-functional teams for scalable solutions."],
    ["<b>AI, ML & Data Science Intern — Inventia</b><br/><i>Jan 2025 – Apr 2025 | Internship</i><br/>"
     "- Developed ML models for predictive analytics and data insights.<br/>- Implemented supervised and unsupervised learning algorithms.<br/>- Worked on end-to-end data pipelines and deployment."]
]
for exp in experience_data:
    content.append(Paragraph(exp[0], styles['Body']))

# Projects Section
content += [Paragraph("<b>Key Projects</b>", styles['SectionHeader'])]

projects = [
    ["<b>Insu Scan Pro (Deployed)</b><br/><i>Python, FastAPI, Streamlit, XGBoost</i><br/>AI-powered diagnostic system predicting diabetes with 98% accuracy.<br/>[Live App: insuscanpro.streamlit.app]"],
    ["<b>See Beneath – Underwater Object Detection</b><br/><i>Python, YOLOv4, OpenCV</i><br/>Deep learning-based detection of underwater objects in real-time."],
    ["<b>AI-Powered Medical Chatbot</b><br/><i>Python, TensorFlow, NLTK, React</i><br/>Conversational chatbot with contextual understanding using AI."],
    ["<b>Portfolio Website (Deployed)</b><br/><i>React, Tailwind CSS, Three.js</i><br/>Personal 3D portfolio showcasing projects and achievements."],
    ["<b>Online Voting System</b><br/><i>React, JavaScript</i><br/>Simple and secure voting interface built as a learning project."]
]
for proj in projects:
    content.append(Paragraph(proj[0], styles['Body']))

# Education
content += [Paragraph("<b>Education</b>", styles['SectionHeader']),
            Paragraph("<b>B.Tech (Computer Science with Artificial Intelligence)</b><br/>ABES Institute of Technology, AKTU — Pursuing | CGPA: 7.33", styles['Body']),
            Paragraph("Class XII — Arpan Public School (CBSE) | 2021 | 83.33%", styles['Body']),
            Paragraph("Class X — Arpan Public School (CBSE) | 2019 | 84.44%", styles['Body'])]

# Skills
skills = [
    "<b>Programming:</b> Python, C++, JavaScript",
    "<b>AI & ML:</b> Machine Learning, Deep Learning, Generative AI, Prompt Engineering",
    "<b>Frameworks & Tools:</b> FastAPI, Streamlit, TensorFlow, scikit-learn, Selenium, PyMuPDF, OpenAI API",
    "<b>Web Development:</b> React, HTML, CSS, Tailwind CSS, Three.js",
    "<b>Database:</b> MySQL",
    "<b>Other Skills:</b> OOPs, Git, RPA Tools, Data Visualization, API Integration"
]

content += [Paragraph("<b>Technical Skills</b>", styles['SectionHeader'])]
for skill in skills:
    content.append(Paragraph(skill, styles['Body']))

# Achievements
content += [Paragraph("<b>Achievements & Interests</b>", styles['SectionHeader']),
            Paragraph("• Developed multiple AI and automation projects (deployed and local).<br/>• Specialized in healthcare-focused ML applications.<br/>• Passionate about AI + RPA integration for real-world automation.", styles['Body'])]

# Personal tagline
content += [Spacer(1, 12), HRFlowable(width="100%", color=colors.HexColor('#004080')),
            Paragraph("<i>“Blending AI and automation to design intelligent systems that simplify and accelerate the future of work.”</i>", styles['SubHeader'])]

# Build PDF
doc.build(content)

pdf_path
