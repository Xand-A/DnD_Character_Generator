import pdfkit
import base64


def generate_pdf():
    wkhtmltopdf_path = "C:\Program Files\wkhtmltopdf"
    pdfkit_options = {
        "page-size": "A4",
        "orientation": "Portrait",
        "dpi": 300,
    }

    # Convert the Streamlit page to PDF
    pdfkit.from_file("app.py", "streamlit_page.pdf", options=pdfkit_options)


def get_downloader_link(file_path, file_label):
    with open(file_path, "rb") as file:
        data = file.read()
    b64 = base64.b64encode(data).decode("utf-8")
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_label}">Click here to download: {file_label}</a>'
    return href
