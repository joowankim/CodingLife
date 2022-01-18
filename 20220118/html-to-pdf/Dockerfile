FROM surnet/alpine-python-wkhtmltopdf:3.9.9-0.12.6-small

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN wget https://github.com/naver/D2Codingfont/releases/download/VER1.3.2/D2Coding-Ver1.3.2-20180524.zip && \
    unzip D2Coding-Ver1.3.2-20180524.zip && \
    mkdir /usr/share/fonts/truetype/D2Coding && \
    cp ./D2Coding/*.ttf /usr/share/fonts/truetype/D2Coding/ && \
    fc-cache -fv

CMD ["python", "main.py"]