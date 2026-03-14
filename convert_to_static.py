import os
import re

def get_images(path):
    full_path = os.path.join(os.getcwd(), path.lstrip('/'))
    if not os.path.exists(full_path):
        return []
    files = [f for f in os.listdir(full_path) if os.path.isfile(os.path.join(full_path, f)) and not f.startswith('.')]
    files.sort()
    return [os.path.join(path, f) for f in files]

def convert_php_to_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the path in the PHP script
    path_match = re.search(r"\$path = '([^']+)';", content)
    if not path_match:
        # Some files might not have a path or have a different format
        # For now, let's just replace simple PHP echo/server variables
        content = re.sub(r'<\?php echo \$_SERVER\["HTTP_HOST"\]; \?>', 'localhost', content)
        content = re.sub(r'<\?php echo \$_SERVER\["SERVER_SOFTWARE"\]; \?>', 'Python/3.x', content)
        return content

    image_path = path_match.group(1)
    images = get_images(image_path)

    # Replace the multi-line PHP blocks
    # We look for the patterns starting with <?php and ending with ?>
    
    # First, let's just generate the HTML for the slides
    slides_html = ""
    for img in images:
        # Make paths relative for GitHub Pages compatibility
        relative_img = img.lstrip('/')
        slides_html += f'                                    <li>\n                                        <img src="{relative_img}"/>\n                                    </li>\n'

    carousel_html = ""
    for img in images:
        # Make paths relative for GitHub Pages compatibility
        relative_img = img.lstrip('/')
        carousel_html += f'                                    <li>\n                                        <div class="hover"></div>\n                                        <img src="{relative_img}"/>\n                                    </li>\n'

    # This is a bit hacky but should work for this specific codebase
    # Replace the slider block
    content = re.sub(r'<\?php.*?// Inizio script per il caricamento di file da ftp.*?// Fine script per il caricamento di file da ftp.*?\?>', slides_html, content, flags=re.DOTALL)
    
    # Replace the carousel block (if present)
    content = re.sub(r'<\?php.*?// Inizio script per il caricamento di file da ftp.*?// Fine script per il caricamento di file da ftp.*?\?>', carousel_html, content, flags=re.DOTALL)

    # Some files use shorthand <?= $img ?>
    content = re.sub(r'<\?=\$img \?>', '', content)
    
    # Handle other PHP blocks
    content = re.sub(r'<\?php.*?\?>', '', content, flags=re.DOTALL)

    return content

def main():
    files = [f for f in os.listdir('.') if f.endswith('.php')]
    for f in files:
        # Check if index.php is a placeholder to avoid overwriting a good index.html
        if f == 'index.php':
            with open(f, 'r', encoding='utf-8') as check_file:
                if 'sito in costruzione' in check_file.read():
                    print(f"Skipping {f} as it is a placeholder.")
                    continue

        html_content = convert_php_to_html(f)
        output_name = f.replace('.php', '.html')
        with open(output_name, 'w', encoding='utf-8') as out:
            out.write(html_content)
        print(f"Converted {f} to {output_name}")

    # Update links in all .html files
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    for f in html_files:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace .php with .html in links
        new_content = re.sub(r'href="([^"]+)\.php"', r'href="\1.html"', content)
        
        if new_content != content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated links in {f}")

if __name__ == "__main__":
    main()
