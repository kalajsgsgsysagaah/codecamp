import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

def analyze_data(file_path):
    df = pd.read_csv(file_path)
    summary = df.describe()
    return summary, df

def generate_plot(df, column, output_image):
    plt.figure(figsize=(6, 4))
    df[column].hist(bins=20, color='blue', edgecolor='black')
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.savefig(output_image)
    plt.close()

def generate_pdf_report(summary, image_path, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica-Bold", 14)
    c.drawString(200, height - 50, "Automated Data Analysis Report")
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 80, "Summary Statistics:")
    
    y_position = height - 100
    for row in summary.to_string().split('\n'):
        c.drawString(50, y_position, row)
        y_position -= 15
    
    c.drawImage(ImageReader(image_path), 150, y_position - 200, width=300, height=200)
    c.save()

def main():
    file_path = "data.csv"  # Replace with your file
    output_image = "histogram.png"
    output_pdf = "report.pdf"
    column_to_analyze = "column_name"  # Replace with your column
    
    summary, df = analyze_data(file_path)
    generate_plot(df, column_to_analyze, output_image)
    generate_pdf_report(summary, output_image, output_pdf)
    print(f"Report generated: {output_pdf}")

if __name__ == "__main__":
    main()
