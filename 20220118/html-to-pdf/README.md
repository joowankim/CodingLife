# HTML 파일을 PDF 파일로 변환하기 with `Docker`

컨테이너 환경에서 실행할 수 있는 HTML to PDF 파일 변환 python 스크립트를 작성해보자.
이를 위해서는 다음과 같은 환경이 필요하다.

1. `python`, `wkhtmltopdf`가 설치되어있는 컨테이너 이미지
2. 변환을 실행할 `python` 스크립트
3. 한글도 입력할 수 있어야 하기에 한글 폰트또한 필요하다.

## 컨테이너 이미지

운 좋게도 다음과 같은 이미지가 이미 DockerHub에 있다.

[surnet/alpine-python-wkhtmltopdf](https://hub.docker.com/r/surnet/alpine-python-wkhtmltopdf)

## html to pdf 변환을 실행할 `python` 스크립트

`wkhtmltopdf` 프로그램을 랩핑한 파이썬 패키지 `pdfkit`를 이용해 한 줄의 코드로 구현할 수 있다.
따라서, `Dockerfile`로 `surnet/alpine-python-wkhtmltopdf` 이미지를 가져와서 `pdfkit`을 이용할 수 있는 개발환경만 설정해주면 된다.

## 컨테이너에 한글 폰트 설치하기

[검색으로 알게된 블로그](https://thekkom.tistory.com/m/15)에 따르면 두 가지 방법이 있다.

1. `apt-get`을 활용해 간편하게 폰트 설치하기
2. 직접 `.ttf` 파일을 다운받아 폰트 설치하기
