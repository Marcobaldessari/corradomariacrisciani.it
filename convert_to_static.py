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
    
    # First, generate the HTML for the slides
    slides_html = '<div class="gallery-container">\n'
    
    # Main Swiper
    slides_html += '        <div class="swiper main-swiper">\n            <div class="swiper-wrapper">\n'
    for img in images:
        relative_img = img.lstrip('/')
        slides_html += f'                <div class="swiper-slide">\n                    <img src="{relative_img}"/>\n                </div>\n'
    slides_html += '            </div>\n'
    # Custom Navigation
    slides_html += '            <div class="swiper-button-next custom-nav"><i class="fa fa-chevron-right"></i></div>\n'
    slides_html += '            <div class="swiper-button-prev custom-nav"><i class="fa fa-chevron-left"></i></div>\n'
    slides_html += '        </div>\n'
    
    # Thumb Swiper
    slides_html += '        <div class="swiper thumb-swiper">\n            <div class="swiper-wrapper">\n'
    for img in images:
        relative_img = img.lstrip('/')
        slides_html += f'                <div class="swiper-slide">\n                    <img src="{relative_img}"/>\n                </div>\n'
    slides_html += '            </div>\n        </div>\n'
    slides_html += '    </div>\n'

    # Update CSS/JS for Swiper
    # Check if they are already there to avoid duplicates
    if 'swiper-bundle.min.css' not in content:
        # Match <link ... href="css/style.css" ...> regardless of attribute order
        content = re.sub(r'(<link[^>]+href=["\']css/style\.css["\'][^>]*>)', r'\1\n    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />', content)
    if 'swiper-bundle.min.js' not in content:
        # Match <script ... src="js/scripts.js" ...> regardless of attribute order
        content = re.sub(r'(<script[^>]+src=["\']js/scripts\.js["\'][^>]*>)', r'<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>\n    \1', content)

    # First, try to replace the entire section content if it exists
    if '<section class="slider">' in content:
        content = re.sub(r'<section class="slider">.*?</section>', f'<section class="slider">\n{slides_html}\n                    </section>', content, flags=re.DOTALL)
    else:
        # Fallback for older formats if section is missing or differently named
        # We target the old structure OR the previously generated swarm structure
        # Old flexslider
        content = re.sub(r'<div id="slider" class="flexslider">.*?<ul class="slides">.*?</ul>.*?</div>', slides_html, content, flags=re.DOTALL)
        # Our previous swiper attempts
        content = re.sub(r'<div id="slider" class="swiper gallery-swiper">.*?</div>', slides_html, content, flags=re.DOTALL)
        content = re.sub(r'<div class="gallery-container">.*?</div>', slides_html, content, flags=re.DOTALL)
    
    # Remove the old carousel if present
    content = re.sub(r'<div id="carousel" class="flexslider">.*?<ul class="slides">.*?</ul>.*?</div>', '', content, flags=re.DOTALL)
    
    # Remove the pseudo-scroll if present
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
