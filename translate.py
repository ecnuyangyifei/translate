import requests
import time


google_translate_api = 'http://translate.google.cn/translate_a/single?client=gtx&sl=en&tl=zh-CN&dt=t&q='


def translate(to_translate):
    # urllib3.re
    to_translate = to_translate.strip()
    url = google_translate_api + to_translate
    with requests.get(url, headers={'content-type': 'application/json'}) as r:
        response_json = r.json()
        length = len(response_json[0])
        result = ''
        for i in range(length):
            result = result + response_json[0][i][0]
        return result


def dummy(paragraph):
    return paragraph


def translate_file(filename, to_file_name):
    translate_result = ''
    with open(filename, encoding='utf-8') as fr:
        paragraph = ''
        lines = fr.readlines()
        length = len(lines)
        for line in lines:
            length = length - 1
            paragraph = paragraph + line.strip() + '\n'
            if not line.strip() or length == 0:
                if not paragraph.strip():
                    continue
                if length != 0 and len(paragraph) < 2000:
                    continue
                translate_result = translate_result + translate(paragraph) + '\n\n'
                # print(paragraph)
                paragraph = ''
                continue
    save_to_file(to_file_name, translate_result)


def save_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as fa:
        fa.write(content)


time_start = time.time()
# translate_file('test.txt', 'result.txt')
translate_file('to_translate.txt', 'result.txt')
time_end = time.time()
print(time_end - time_start, 's')

