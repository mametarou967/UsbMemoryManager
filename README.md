# UsbMemoryManager
Usbメモリ管理機

# clone後の作業

1. venv環境の作成（必要に応じて)

```
python3 -m venv venv
source venv/bin/activate
```

2. 必要なパッケージのインストール

```
pip install flask
pip install python-dotenv
pip install flask-wtf
pip install flask-sqlalchemy
pip install flask-migrate
pip install flask-login
```

3. db作成

```
flask db init
flask db migrate -m "hogehoge"
flask db upgrade
```

4. usbMemoryデータの作成

usb_numberソケット分だけ以下を実行します
- flask shell
- usbMemory = UsbMemory(usb_number=1)
- db.session.add(usbMemory)
- usbMemory = UsbMemory(usb_number=2)
- db.session.add(usbMemory)
- ...
- db.session.commit()

# 実行方法

1.raspberry piでvenv環境下で動作するためコンソールで以下のように入力して実行します(venv環境作成時に実行している場合は不要)

 source venv/bin/activate

2.最後に以下のコマンドを実行してserverを立ち上げます
ポート0.0.0.0を指定することにより外部公開することになります（参考：https://flask.palletsprojects.com/en/1.1.x/quickstart/)

 flask run --host=0.0.0.0

3.shell modeで立ち上げる場合は以下のようにします

 flask shell

# debug機能の有効化

以下のコマンドで有効化されます

 export FLASK_ENV=development
