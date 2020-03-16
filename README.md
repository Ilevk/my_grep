## My_grep

과제) <br>
python으로 simple grep 기능 구현  (문자열검색)
   : corpus 가 담겨져있는 text 파일에서 문자열 검색 기능 (line 위치와 함께 출력)

### 1. 실행 방법
#### 1) Commend Line 사용 시

    python3 src/my_grep.py [-o=OPTION] -p=PATTERN -f=FILE

- 옵션에서 정규 표현식을 사용할 경우 Pattern은 따옴표로 묶어 'regex*' 등으로 입력
    
#### 2) Python 스크립트에서 import 시

    ...
    option = 'F'
    pattern = 'classical'
    file = '.../file.txt'
    mg = My_grep(option, pattern, file) # My_Grep 객체 생성
    mg.load_find()     # 파일 읽기 및 패턴 찾기 
    mg.found_pattern   # 매칭된 패턴 리스트 반환 [[# of Row, Start idx, End idx], String] 
    
### 2. 명령어 옵션
        -F        : PATTERN을 정규 표현식(RegEx)이 아닌 일반 문자열로 해석.
        -G        : PATTERN을 기본 정규 표현식(Basic RegEx)으로 해석.
        -i        : 대/소문자 무시.
- 입력하지 않은 경우 일반 문자열로 해석

### 3. grep 과의 비교 (한계 및 이점)

#### (1) 파이썬 정규식 문법의 문제점인 탈출 문자 적용이 되어있지 않음.<br>
#### (2) 이하 옵션이 구현되어 있지 않음.

        -E        : PATTERN을 확장 정규 표현식(Extended RegEx)으로 해석.
        -P        : PATTERN을 Perl 정규 표현식(Perl RegEx)으로 해석.
        -e        : 매칭을 위한 PATTERN 전달.
        -f        : 파일에 기록된 내용을 PATTERN으로 사용.
        -v        : 매칭되는 PATTERN이 존재하지 않는 라인 선택.
        -w        : 단어(word) 단위로 매칭.
        -x        : 라인(line) 단위로 매칭.
        -z        : 라인을 newline(\n)이 아닌 NULL(\0)로 구분.
        -m        : 최대 검색 결과 갯수 제한.
        -b        : 패턴이 매치된 각 라인(-o 사용 시 문자열)의 바이트 옵셋 출력.
        -n        : 검색 결과 출력 라인 앞에 라인 번호 출력.
        -H        : 검색 결과 출력 라인 앞에 파일 이름 표시.
        -h        : 검색 결과 출력 시, 파일 이름 무시.
        -o        : 매치되는 문자열만 표시.
        -q        : 검색 결과 출력하지 않음.
        -a        : 바이너리 파일을 텍스트 파일처럼 처리.
        -I        : 바이너리 파일은 검사하지 않음.
        -d        : 디렉토리 처리 방식 지정. (read, recurse, skip)
        -D        : 장치 파일 처리 방식 지정. (read, skip)
        -r        : 하위 디렉토리 탐색.
        -R        : 심볼릭 링크를 따라가며 모든 하위 디렉토리 탐색.
        -L        : PATTERN이 존재하지 않는 파일 이름만 표시.
        -l        : 패턴이 존재하는 파일 이름만 표시.
        -c        : 파일 당 패턴이 일치하는 라인의 갯수 출력.

#### (3) 다른 파이썬 스크립트에서 import를 통해 패턴에 맞는 문자열 탐색 기능을 사용할 수 있음.


### 4. Reference
1. grep의 구성: https://recipes4dev.tistory.com/157