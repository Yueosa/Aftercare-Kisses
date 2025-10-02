import random as rd
from typing import Literal
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, ".."))
from Pkg import Printer


class NumberGuess:
    def __init__(self) -> None:
        """
        NumberGuess类的指责是实现游戏的主逻辑
        """
        self._flag: int = 0
        self.left: int = 0
        self.right: int = 100
        self.user_input: int = 0

        self.cp: Printer = Printer()

    def _number_guess(self) -> bool:
        """判断用户输入是否等于正确数"""
        return self._flag == self.user_input

    def _get_user_input(
            self,
            message: str,
            ) -> int:
        """从用户处获取输入(整数类型)"""
        while True:
            user_input = input(message)
            try:
                guess = int(user_input)
                return guess
            except ValueError:
                self.cp.cprint("red", "宝宝输的不是数字呢~ 请再试一次~")

    def _set_flag(
            self,
            mode: Literal["auto", "user"] = "auto"
            ) -> None:
        """设置正确数, 有自动和用户输入两种模式, 默认为自动"""
        if mode == "user":
            self.left = self._get_user_input("请输入最小数~ : ")
            self.right = self._get_user_input("请输入最大数~ : ")
            if self.left > self.right:
                self.cp.cprint("red", "范围不对哦，帮你调换一下~")
                self.left, self.right = self.right, self.left
        self._flag = rd.randint(self.left, self.right)

    def _print_left_right(self) -> None:
        """输出当前left和right的情况"""
        self.cp.cprint("cyan", f"\n在这个范围里试一试哦 ! {self.left} - {self.right}")

    def menu(self) -> bool:
        """游戏主菜单"""
        while True:
            self.cp.cprint("yellow", "\n== 猜数字小游戏 ==")
            self.cp.cprint("cyan", "1. 开始游戏")
            self.cp.cprint("cyan", "2. 自己划定范围")
            self.cp.cprint("cyan", "3. 退出游戏")

            choice = input("请选择操作：")

            if choice == "1":
                self._set_flag()
                self._print_left_right()
                return True
            elif choice == "2":
                self._set_flag("user")
                self._print_left_right()
                return True
            elif choice == "3":
                self.cp.cprint("green", "\n游戏退出啦, 下次再来玩哦~ 👋")
                return False
            else:
                self.cp.cprint("red", "无效选择，请重新输入~")

    def play(self) -> None:
        """游戏主逻辑"""
        while True:
            self.user_input = self._get_user_input("宝宝请输入要猜测的数字哦~ : ")
            if self._number_guess():
                self.cp.cprint("green", "\n恭喜宝宝, 猜对啦 !🎉")
                break
            elif self.user_input < self._flag:
                self.cp.cprint("blue", "太小啦，再试一次~")
                self.left = self.user_input + 1
            else:
                self.cp.cprint("magenta", "太大啦，再试一次~")
                self.right = self.user_input - 1

            self._print_left_right()

    def main(self) -> None:
        """程序入口"""
        while True:
            if self.menu():
                self.play()
            else:
                break


if __name__ == "__main__":
    ng = NumberGuess()
    ng.main()
