# 리스트 메소드
# .append() : 리스트에서 항목 하나를 맨 마지막에 추가
# .insert() : 리스트에서 특정 위치에 항목을 삽입
#   ex) lang.insert(1, "javascript")
# extends() : 리스트에서 항목 여러개를 맨 마지막에 추가
#   ex) lang.extend(['Mybatis','Spring'])
# remove() : 입력값과 첫 번째로 일치하는 항목을 리스트에서 제거
#   ex) lang.remove('Spring')
# pop() : 리스트의 마지막 항목을 제거한 후에 반환
#   ex) poplang = lang.pop()
# index() : 리스트에서 인자와 일치하는 첫 번째 항목의 위치를 반환
#   ex) indexlang = lang.index('C언어')
# count() : 리스트에서 인자와 일치하는 항목의 개수를 반환
#   ex) countlang = lang.count('javascript')
# sort() : 숫자나 문자열로 구성된 리스트 항목을 순방향으로 정렬
#   ex) lang.sort()
# reverse() : 리스트 항목을 끝에서부터 역순으로 정렬
#   ex) lang.reverse()
# len(lang) : lang 배열의 길이를 출력



# 리스트와 튜플의 차이
# 리스트는 값을 추가하거나 빼거나 할 수 있다.
# 튜플은 한번 생성하면 그 이후에는 항목을 변경할 수 없다.
# list = []
# tuple = () >> 괄호의 차이 , tuple1 = (1,) : 한개만 튜플에 넣으려면 tuple1[1] = 1

# 세트(Set) : 수학에서의 집합개념 : 자동으로 중복 제거
# set = {1,2,3,3} : >> print(set) : {1,2,3}
# 교집합 : .intersection() >> A.intersection(B)
# 합칩합 : .union() >> A.union(B)
# 차집합 : .differenct() >> A.difference(B)

# 리스트, 튜플, 세트 간 타입변환 가능
# a = [1,2,3,4,5] >> type(a) >> 리스트
# b = tuple(a) >> type(b) >> 튜플로 형변환
# c = set(a) >> type(c) >> 세트로 형변환

# 딕셔너리( 자바에서의 해쉬맵 )
# key:value 로 이루어짐
# country_capital = {"한국":"서울","일본":"도쿄","중국":"베이징","북한":"평양"}
# country_capital["미국"] = "워싱턴" >> 딕셔너리에 항목 추가
# del country_capital["미국"] >> key가 미국인 value 삭제(del)
# 딕셔너리 메소드
# .keys() : 딕셔너리에서 키 전체를 리스트 형태로 반환
# .values() : 딕셔너리에서 값 전체를 리스트 형태로 반환
# .items() : 딕셔너리에서 키와 값의 쌍을(키, 값)처럼 튜플 형태로 반환
#   country_capital.items()
# .update('dict_data_2') : 딕셔너리에 딕셔너리(dict_data_2) 데이터 추가
# .clear() : 딕셔너리의 모든 항목 삭제

country_capital = {"한국":"서울","일본":"도쿄","중국":"베이징","북한":"평양"}
print(country_capital.items())

lang = []
lang.append("파이썬")
lang.append("C언어")
lang.append("자바")
print(lang)
print(lang[0])
print(len(lang))