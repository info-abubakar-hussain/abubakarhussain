#!/usr/bin/env python3
"""
Convert resume.html to PDF using weasyprint
Install weasyprint first: pip3 install weasyprint
"""

try:
    from weasyprint import HTML
    import os
    
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(script_dir, 'resume.html')
    pdf_file = os.path.join(script_dir, 'AbuBakar_Hussain_Resume.pdf')
    
    print(f"Converting {html_file} to PDF...")
    HTML(html_file).write_pdf(pdf_file)
    print(f"✅ Success! PDF created: {pdf_file}")
    
except ImportError:
    print("❌ weasyprint not installed.")
    print("\nTo install weasyprint, run:")
    print("  pip3 install weasyprint")
    print("\nOr use your browser:")
    print("  1. Open resume.html in Chrome/Safari")
    print("  2. Press Cmd+P (Print)")
    print("  3. Select 'Save as PDF'")
    print("  4. Save as 'AbuBakar_Hussain_Resume.pdf'")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nAlternative: Use browser print-to-PDF:")
    print("  1. Open resume.html in Chrome/Safari")
    print("  2. Press Cmd+P (Print)")
    print("  3. Select 'Save as PDF'")
    print("  4. Save as 'AbuBakar_Hussain_Resume.pdf'")

