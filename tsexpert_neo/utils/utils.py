from lxml import etree

def has_background_color(cell):
    """
    주어진 셀이 백그라운드 색을 가지고 있는지 확인합니다.
    
    :param cell: DOCX 테이블의 셀
    :return: 백그라운드 색이 있으면 True, 없으면 False
    """
    cell_xml = cell._element  # 셀의 XML 요소에 접근
    shd = cell_xml.find('.//w:shd', namespaces={'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'})  # 네임스페이스를 포함하여 'w:shd' 태그 찾기
    
    if shd is not None:
        fill = shd.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}fill')  # 'fill' 속성 확인
        if fill and fill != "auto":  # 'auto'가 아닌 값이 있으면 배경색이 설정된 것
            print(f"Background color detected: {fill}")  # 배경색 출력 (디버깅용)
            return fill
    return False