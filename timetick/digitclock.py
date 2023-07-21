import time


class DigitClock:
    def __init__(self):
        """
        初始化方法
        """
        local_time = time.localtime()
        self._hour = local_time.tm_hour
        self._minute = local_time.tm_min
        self._second = local_time.tm_sec

    def run(self):
        self._second += 1
        if self._second == 60:
            self._minute += 1
            self._second = 0
        if self._minute == 60:
            self._hour += 1
            self._minute = 0
        if self._hour == 24:
            self._hour = 0

    def show(self):
        return f"{self._hour}:{ self._minute}:{self._second} \n"


def main():
    myclock = DigitClock()
    step = 10
    for _ in range(step):
        print(myclock.show())
        time.sleep(1)
        myclock.run()

main()