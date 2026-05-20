import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Delete the leftover horizontal grid items (rs1 to rs4)
    # The leftover starts with: <div onclick="showRoadmapStage(1)" id="rs1"
    # and ends with the </div> right before <div id="roadmap-detail"></div>
    pattern = re.compile(r'    <div onclick="showRoadmapStage\(1\)" id="rs1".*?  </div>\n\n  <div id="roadmap-detail"></div>', re.DOTALL)
    
    # We replace it with just: \n  <div id="roadmap-detail"></div>
    content = pattern.sub('  <div id="roadmap-detail"></div>', content)

    # 2. Fix the width wrapping issue for "Stage X" inside the dropdown menu
    # Replace "width:55px" with "min-width:60px; white-space:nowrap;"
    content = content.replace('width:55px', 'min-width:60px; white-space:nowrap;')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_file('index.html')
fix_file('datark_sales_kit2.html')
print("Issues fixed.")
