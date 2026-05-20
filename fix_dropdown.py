import re

html_to_inject = """  <div class="news-dropdown-container" id="roadmap-dropdown-container" style="max-width: 100%; margin-bottom: 20px;">
    <div class="news-dropdown-trigger" onclick="toggleRoadmapDropdown()" style="padding: 14px 18px; font-size: 15px;">
      <span id="roadmap-dropdown-selected"><span style="font-weight:600;color:#2563EB;margin-right:8px;display:inline-block;width:55px">Stage 1</span> 소형 전문직 사무소</span>
      <span class="dropdown-chevron">▼</span>
    </div>
    <div class="news-dropdown-menu" id="roadmap-dropdown-menu">
      <div class="news-dropdown-item active" onclick="selectRoadmapStage(0, '<span style=\\'font-weight:600;color:#2563EB;margin-right:8px;display:inline-block;width:55px\\'>Stage 1</span> 소형 전문직 사무소')">
        <span style="font-weight:600;color:#2563EB;margin-right:8px;display:inline-block;width:55px">Stage 1</span> 소형 전문직 사무소
      </div>
      <div class="news-dropdown-item" onclick="selectRoadmapStage(1, '<span style=\\'font-weight:600;color:#7C3AED;margin-right:8px;display:inline-block;width:55px\\'>Stage 2</span> 미디어·콘텐츠 제작사')">
        <span style="font-weight:600;color:#7C3AED;margin-right:8px;display:inline-block;width:55px">Stage 2</span> 미디어·콘텐츠 제작사
      </div>
      <div class="news-dropdown-item" onclick="selectRoadmapStage(2, '<span style=\\'font-weight:600;color:#DC2626;margin-right:8px;display:inline-block;width:55px\\'>Stage 3</span> 중견 제조·건설')">
        <span style="font-weight:600;color:#DC2626;margin-right:8px;display:inline-block;width:55px">Stage 3</span> 중견 제조·건설
      </div>
      <div class="news-dropdown-item" onclick="selectRoadmapStage(3, '<span style=\\'font-weight:600;color:#D97706;margin-right:8px;display:inline-block;width:55px\\'>Stage 4</span> ISMS 의무 대상 기업')">
        <span style="font-weight:600;color:#D97706;margin-right:8px;display:inline-block;width:55px">Stage 4</span> ISMS 의무 대상 기업
      </div>
      <div class="news-dropdown-item" onclick="selectRoadmapStage(4, '<span style=\\'font-weight:600;color:#059669;margin-right:8px;display:inline-block;width:55px\\'>Stage 5</span> 공공·금융·대형 병원')">
        <span style="font-weight:600;color:#059669;margin-right:8px;display:inline-block;width:55px">Stage 5</span> 공공·금융·대형 병원
      </div>
    </div>
  </div>"""

js_to_inject = """function toggleRoadmapDropdown() {
  const container = document.getElementById('roadmap-dropdown-container');
  if (container) container.classList.toggle('open');
}

function selectRoadmapStage(idx, titleHtml) {
  const container = document.getElementById('roadmap-dropdown-container');
  if (container) container.classList.remove('open');
  
  const selectedSpan = document.getElementById('roadmap-dropdown-selected');
  if (selectedSpan) selectedSpan.innerHTML = titleHtml;
  
  const items = document.querySelectorAll('#roadmap-dropdown-menu .news-dropdown-item');
  items.forEach((item, i) => {
    if (i === idx) item.classList.add('active');
    else item.classList.remove('active');
  });
  
  showRoadmapStage(idx);
}

function showRoadmapStage(idx){"""

def replace_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the HTML grid
    pattern = re.compile(r'<div style="display:grid;grid-template-columns:repeat\(5,1fr\);gap:8px;margin-bottom:20px">.*?</div>\s*</div>', re.DOTALL)
    content = pattern.sub(html_to_inject, content, count=1)
    
    if filepath == 'index.html':
        # Replace JS
        content = content.replace('function showRoadmapStage(idx){', js_to_inject, 1)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

replace_html('index.html')
replace_html('datark_sales_kit2.html')
