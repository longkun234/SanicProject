# coding:utf8
import cv2
from sanic import Sanic
from sanic.response import text
from sanic.response import json
import face as face
import json as jsons

app = Sanic("SanicApp")


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。、


@app.route("/")
async def hello_world(request):
    return json({"hello": "world"})


@app.post("/Dector")
async def Get_Dector(request):
    json_str = jsons.dumps(request.json)
    data2 = jsons.loads(json_str)
    jxzp_str = face.tranposeDector(str(data2["img"]).replace('data:image/jpg;base64,', '').replace('data:image/png;base64,', ''), 0)
    return json({"face": str('data:image/jpg;base64,' + str(jxzp_str).replace("b'", '').replace("'", ''))})


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1234, debug=True)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
