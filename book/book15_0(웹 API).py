"""
JSON 형식의 데이터 처리

python 데이터 ----> JSON 데이터로 형변환
    json.dumps(python_data [, indent=n, sort_key = True or False, ensure_ascii = True or False])
        indent = n >> : n칸만큼 들여쓰기를 한다.
        sort_key >> : 파이썬 데이터가 딕셔너리 타입인 경우 key를 기준으로 정렬할지를 설정
        ensure_ascii >> : ASCII코드로 구성된 문자열인지 설정,
                     >> : 파이썬데이터에 한글이 있는 경우 False로 한다.

JSON 데이터 ----> pyhton 에서 사용할 수 있는 데이터 타입으로 변환
    json.loads(json_data)

XML 형식의 데이터 처리
xml 데이터 ----> 딕셔너리 타입으로 변환
    xmltodict.parse(xml_input [, xml_attribs = True or False])
        xml_input >> : xml 데이터
        xml_attribs = True >> : 흠.. xml에서 태그에 지정한 속성을 처리한다.
        xml_attribs = False >> : xml에서 지정했던 속성이 모두 무시되고 딕셔너리 형식으로 변환





"""