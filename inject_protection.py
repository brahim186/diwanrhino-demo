import os

html_protection_code = """<script>
document.addEventListener('contextmenu', e => e.preventDefault());
document.addEventListener('keydown', e => {
  if (e.key === 'F12' || (e.ctrlKey && (e.shiftKey && (e.key === 'I' || e.key === 'J' || e.key === 'U')))) {
    e.preventDefault();
  }
});
</script>
"""

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root:
        continue
        
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if "contextmenu" not in content:
                if '</body>' in content:
updated_content = content.replace('</body>', html_protection_code + '</body>')                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    print(f"DR: {file_path}")
