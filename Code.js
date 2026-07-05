// Deploy Timestamp: 2026-07-05 13:50:00 (Force update layout)
function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('⚙️ 추가 기능')
    .addItem('HTML 화면 열기', 'showHtmlDialog')
    .addToUi();
}

function showHtmlDialog() {
  var html = HtmlService.createHtmlOutputFromFile('index')
      .setWidth(1000)
      .setHeight(750)
      .setTitle('AI 연구소 탈출: 좌표평면');
  SpreadsheetApp.getUi().showModalDialog(html, ' ');
}

// 웹 앱(Web App) URL로 직접 접속 시 HTML을 화면에 렌더링하는 함수입니다.
function doGet(e) {
  return HtmlService.createHtmlOutputFromFile('index')
      .setTitle('AI 연구소 탈출: 좌표평면')
      .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

