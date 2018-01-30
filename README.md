# translate using python3

## 调用谷歌翻译完成英文到中文的翻译

## 执行方式
 
python translate.py 

将会翻译当前目录下to_translate.txt（必须为utf-8格式保存）文件，翻译结果存到当前目录下result.txt文件中

## 若要打包成.exe文件可执行如下步骤
- pip install pyinstaller
- pyinstaller -F translate.py
