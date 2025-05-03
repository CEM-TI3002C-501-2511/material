from html_to_dash import parse_html
from bs4 import BeautifulSoup
import os
html_file_directory = "html"
python_file_directory = "pages"

os.makedirs(python_file_directory, exist_ok=True)

files = [file for file in os.listdir(html_file_directory) if file.endswith('.html')]

for file in files:
    with open(f"{html_file_directory}/{file}", "r", encoding="utf8") as f:
        html = f.read()
        soup = BeautifulSoup(html, "html.parser")
        body = soup.find('body')
        
        header = body.find('header')
        header_html_path = os.path.join(html_file_directory, 'header.html')
        if header and not os.path.exists(header_html_path):
            new_soup = BeautifulSoup('<html><head></head><body></body></html>', 'html.parser')
            new_soup.body.append(header.extract())
            with open(header_html_path, 'w', encoding='utf8') as f:
                f.write(str(new_soup))
            files.append("header.html")
            
        footer = body.find('footer')
        footer_html_path = os.path.join(html_file_directory, 'footer.html')
        if footer and not os.path.exists(footer_html_path):
            new_soup = BeautifulSoup('<html><head></head><body></body></html>', 'html.parser')
            new_soup.body.append(footer.extract())
            with open(footer_html_path, 'w', encoding='utf8') as f:
                f.write(str(new_soup))
            files.append("footer.html")
        
        if file != "header.html" and file != "footer.html":
            for tag in body.find_all(['header', 'footer']):
                tag.decompose()
            
        parsed = parse_html(str(body), if_return=True, enable_dash_svg=True)
        with open(f"{python_file_directory}/{file.replace('.html', '.py')}", "w", encoding="utf8") as f:
            f.write(parsed)
print("Done...")