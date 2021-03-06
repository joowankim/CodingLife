# HTML 파일을 PDF 파일로 변환하기 with `Docker`

![python](https://img.shields.io/badge/python-3.9-blue)
![docker](https://img.shields.io/badge/docker-20.10.12-blue)
![docker-compose](https://img.shields.io/badge/docker--compose-3-blue)
![wkhtmltopdf](https://img.shields.io/badge/wkhtmltopdf-0.12.6-blue)
![pdfkit](https://img.shields.io/badge/pdfkit-1.0.0-blue)

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
2. 직접 `.ttf` 파일을 다운받아 폰트 설치하기 (해당 프로젝트는 2번을 사용했다.)

## 실행하기

1. Docker와 docker-compose를 설치한다.
2. `docker-compose up`을 실행한다.
   ```bash
   $ docker-compose up
   ```
3. 실행하고 나면 프로젝트 내에 `output.pdf` 파일 생긴 것을 확인할 수 있다. 내용은 다음과 같다.
   ![image](https://user-images.githubusercontent.com/32446834/149945505-9c23b219-ad4a-4328-99ec-32054ac3e8e8.png)

