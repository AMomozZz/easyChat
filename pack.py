import os
import subprocess
import shutil


# 用来自动打包成exe程序
def main():
    # 执行命令并打印输出
    os.system("python -m venv venv")
    subprocess.run(r"venv\Scripts\activate && pip install -r requirements.txt", shell=True, check=True)
    subprocess.run(r"venv\Scripts\activate && pyinstaller -Fw wechat_gui.py", shell=True, check=True)

    exe_path = os.path.join("dist", "wechat_gui.exe")
    if os.path.exists(exe_path):
        shutil.copy(exe_path, "wechat_gui.exe")
    else:
        print("未找到生成的 exe 文件！")

if __name__ == '__main__':
    main()
