flask intro

- 파이썬 환경 설정

- 플라스크

  ```python
  pip install flask
  ```

- app.py 파일 만들고 나서 다음과 같이 입력하기

  ```py
  from flask import Flask
  app = Flask(__name__)
  
  @app.route("/")
  def hello():
      return "Hello World!"
      
  ```
