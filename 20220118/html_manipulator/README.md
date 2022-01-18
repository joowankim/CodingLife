# BeautifulSoup4로 HTML 조작하기

![python](https://img.shields.io/badge/python-3.9-blue)

기존의 HTML 페이지를 python으로 조작하기 위한 방법 중 하나로 BeautifulSoup4 패키지를 이용해보았다.
해당 미니 프로젝트는 BeautifulSoup4 패키지의 `BeautifulSoup` 객체 사용법의 일부를 다룬다. 

### HTML의 DOM을 조작하기 위한 절차

1. HTML 파일을 BeautifulSoup4 패키지의 `BeautifulSoup` 객체로 만든다.
    - 별거 없다. 그냥 파일을 여는 것과 똑같다.
2. `BeautifulSoup` 객체의 여러 메소드를 이용해 조작할 수 있다.
   - 태그 찾기: `find_*()`
     - 클래스를 이용해서
     - 태그를 이용해서
     - 상대적 거리를 이용해서
   - 한 태그 아래에 새로운 태그 추가하기: `append()`
   - 새로운 태그 만들기: `new_tag()`

### 실행 방법

1. 프로젝트를 클론한다.
    
    ```bash
    $ git clone
    ```
   
2. 의존성 패키지를 설치한다.
   
    ```bash
    $ pip install -r requirements.txt
    ```