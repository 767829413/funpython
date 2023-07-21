from PyQt5 import QtWidgets


class CalState:
    READY = 0
    INPUT = 1


class CalLogic:
    def __init__(self, lcd_widget: QtWidgets.QLCDNumber):
        self.lcd_widget = lcd_widget

        self.state = None
        self.stack = None  # list

        self.last_operation = None
        self.current_operator = None

        self.memory = None

    def init_cal(self):
        """
        初始化计算器状态
        :return:
        """
        self.state = CalState.READY
        self.stack = [0]
        self.last_operation = None
        self.current_operator = None

        self._dispaly()

    def _dispaly(self):
        """
        计算器数字显示在屏上
        :return:
        """
        self.lcd_widget.display(self.stack[-1])

    def number_slot(self, num_val):
        """
        数字0~9的槽函数
        :param num_val:
        :return:
        """
        if self.state == CalState.READY:
            self.stack[-1] = num_val
            self.state = CalState.INPUT
        else:
            self.stack[-1] = self.stack[-1] * 10 + num_val

        self._dispaly()

    def operation_slot(self, op):
        print(self.stack,self.current_operator)
        """
        + - * / 按键操作槽函数
        :param op:
        :return:
        """
        self.current_operator = op
        self.state = CalState.INPUT
        self.stack.append(0)

    def perc_slot(self):
        """
        实现百分之一按键的槽函数
        :return:
        """
        self.stack[-1] *= 0.01
        self._dispaly()
        self.state = CalState.INPUT

    def eq_slot(self):
        print(self.stack,self.current_operator)
        if self.current_operator:
            try:
                result = self._do_operator(self.stack[0], self.stack[1])
            except Exception:
                self.lcd_widget.display("ERROR")
                self.stack = [0]
                return
            self.stack = [result]
            self.current_operator = None
            self.state = CalState.READY
            self._dispaly()

    def _do_operator(self, operand1, operand2):
        """
        执行+-*/操作逻辑
        :param operand1:
        :param operand2:
        :return:
        """
        reslut = 0
        if self.current_operator == "+":
            reslut = operand1 + operand2
        elif self.current_operator == "-":
            reslut = operand1 - operand2
        elif self.current_operator == "/":
            reslut = operand1 / operand2
        elif self.current_operator == "*":
            reslut = operand1 * operand2

        return reslut

    def re_slot(self):
        self.init_cal()

    def m_slot(self):
        self.memory = self.lcd_widget.value()

    def mr_slot(self):
        self.stack[-1] = self.memory
        self.state = CalState.INPUT
        self._dispaly()
