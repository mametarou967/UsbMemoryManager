# UsbMemoryManager
Usbメモリ管理機

# clone後の準備



# 実行方法

1.raspberry piでvenv環境下で動作するためコンソールで以下のように入力して実行します

 source venv/bin/activate
 
続いてflaskAppを有効にします(.flaskenvに宣言しているので、読み込みは不要（かもしれません))

　export FLASK_APP=UsbMemoryManager.py

2.最後に以下のコマンドを実行してserverを立ち上げます
ポート0.0.0.0を指定することにより外部公開することになります（参考：https://flask.palletsprojects.com/en/1.1.x/quickstart/)

 flask run --host=0.0.0.0

3.shell modeで立ち上げる場合は以下のようにします

 flask shell

# debug機能の有効化

以下のコマンドで有効化されます

 export FLASK_ENV=development
