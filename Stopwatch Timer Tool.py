import time

def stopwatch():
    print("按下回车键开始计时，随时按下回车键停止计时。")
    input("准备好后按下回车键开始...")
    print("开始计时！")
    start_time = time.time()

    input("再次按下回车键停止...")
    end_time = time.time()
    elapsed_time = end_time - start_time

    minutes, seconds = divmod(elapsed_time, 60)
    print(f"计时时间为：{int(minutes)} 分钟 {seconds:.2f} 秒")

if __name__ == "__main__":
    stopwatch()
