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
        # Global URL cleanup
        content = content.replace('http://fonts.googleapis.com', 'https://fonts.googleapis.com')
        content = content.replace('http://ajax.googleapis.com', 'https://ajax.googleapis.com')
        return content

    image_path = path_match.group(1)
    images = get_images(image_path)

    # Replace the multi-line PHP blocks
    # We look for the patterns starting with <?php and ending with ?>
    
    # First, let's just generate the HTML for the slides
    slides_html = '<div class="swiper-wrapper">\n'
    for img in images:
        # Make paths relative for GitHub Pages compatibility
        relative_img = img.lstrip('/')
        slides_html += f'        <div class="swiper-slide">\n            <img src="{relative_img}"/>\n        </div>\n'
    slides_html += '    </div>\n    <div class="swiper-button-next"></div>\n    <div class="swiper-button-prev"></div>\n'

    # Update CSS/JS for Swiper
    content = content.replace('css/style.css">', 'css/style.css">\n    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />')
    content = content.replace('<script src="js/scripts.js"></script>', '<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>\n    <script src="js/scripts.js"></script>')

    # Replace the slider block
    # We target the <div id="slider" class="flexslider">...</div> structure
    content = re.sub(r'<div id="slider" class="flexslider">.*?<ul class="slides">.*?</ul>.*?</div>', f'<div id="slider" class="swiper gallery-swiper">{slides_html}</div>', content, flags=re.DOTALL)
    
    # Remove the old carousel if present
    content = re.sub(r'<div id="carousel" class="flexslider">.*?<ul class="slides">.*?</ul>.*?</div>', '', content, flags=re.DOTALL)
    
    # Remove the pseudo-scroll if present (we'll use Swiper's native scrollbar if needed)
    content = re.sub(r'<div class="pseudo-scroll">.*?</div>', '', content, flags=re.DOTALL)

    # Some files use shorthand <?= $img ?>
    content = re.sub(r'<\?=\$img \?>', '', content)
    
    # Global URL cleanup
    content = content.replace('http://fonts.googleapis.com', 'https://fonts.googleapis.com')
    content = content.replace('http://ajax.googleapis.com', 'https://ajax.googleapis.com')

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
        
        # Replace insecure URLs and links
        new_content = content.replace('http://fonts.googleapis.com', 'https://fonts.googleapis.com')
        new_content = new_content.replace('http://ajax.googleapis.com', 'https://ajax.googleapis.com')
        new_content = re.sub(r'href="([^"]+)\.php"', r'href="\1.html"', new_content)
        
        # Replace initialization calls
        new_content = new_content.replace('InitPortfolioFlexSlider();', 'InitPortfolioSwiper();')
        
        if new_content != content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated links/URLs in {f}")

if __name__ == "__main__":
    main()
