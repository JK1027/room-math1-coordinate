import base64
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 메인 스크립트를 분리하기 위한 정규식
match = re.search(r'(<!-- MAIN GAME SCRIPT -->\s*<script>)(.*?)(</script>\s*</body>\s*</html>)', html, re.DOTALL | re.IGNORECASE)

if match:
    prefix = match.group(1)
    script_content = match.group(2)
    suffix = match.group(3)
    
    # UTF-8 문자열을 Base64로 인코딩
    encoded_bytes = base64.b64encode(script_content.encode('utf-8'))
    encoded_str = encoded_bytes.decode('ascii')
    
    # 새로운 스크립트 로더 생성
    loader_script = f"""
        const encodedCode = "{encoded_str}";
        // utf-8 안전한 base64 디코딩
        const decodedCode = decodeURIComponent(escape(atob(encodedCode)));
        const scriptElement = document.createElement('script');
        scriptElement.textContent = decodedCode;
        document.body.appendChild(scriptElement);
    """
    
    # 새로운 HTML 조립
    new_html = html[:match.start()] + prefix + loader_script + suffix
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Success: Script is now Base64 encoded and wrapped.")
else:
    print("Error: Could not find main script block.")
