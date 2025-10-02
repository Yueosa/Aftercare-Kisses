from typing import Tuple
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, ".."))

from Pkg import Printer


class IntCalculate:
    """整数计算器实现"""
    def _add(self, a: int, b: int) -> int:
        return a + b
    
    def add(self, a: int, b: int) -> int:
        return self._add(a, b)
    
    def sub(self, a: int, b: int) -> int:
        return self._add(a, -b)
    
    def mul(self, a: int, b: int) -> int:
        sign = 1
        if a < 0:
            a = -a
            sign = -sign
        if b < 0:
            b = -b
            sign = -sign
        
        result = 0
        for _ in range(b):
            result = self._add(result, a)
        
        return result if sign > 0 else -result
    
    def div(self, a: int, b: int) -> Tuple[int, int]:
        if b == 0:
            raise ZeroDivisionError("The divisor cannot be zero")
        
        sign = 1
        if a < 0:
            a = -a
            sign = -sign
        if b < 0:
            b = -b
            sign = -sign
        
        count = 0
        while a >= b:
            a = self._add(a, -b)
            count = self._add(count, 1)
        
        quotient = count if sign > 0 else -count
        remainder = a if sign > 0 else -a
        
        return quotient, remainder


def menu(calu: IntCalculate, pr: Printer):
    """菜单"""
    while True:
        pr.cprint("cyan", "\n===== 简易计算器 =====")
        pr.cprint("yellow", "1. 加法 (a + b)")
        pr.cprint("yellow", "2. 减法 (a - b)")
        pr.cprint("yellow", "3. 乘法 (a * b)")
        pr.cprint("yellow", "4. 除法 (a ÷  b)")
        pr.cprint("yellow", "5. 退出")
        
        choice = input("请输入选项 (1-5): ").strip()
        
        if choice == "5":
            pr.cprint("green", "感谢使用，再见！")
            break
        
        if choice not in {"1", "2", "3", "4"}:
            pr.cprint("red", "无效的选项，请重新输入。")
            continue
        
        try:
            a = int(input("请输入第一个整数 a: "))
            b = int(input("请输入第二个整数 b: "))
        except ValueError:
            pr.cprint("red", "输入无效，请输入整数！")
            continue
        
        try:
            if choice == "1":
                result = calu.add(a, b)
                pr.cprint("green", f"结果: {a} + {b} = {result}")
            elif choice == "2":
                result = calu.sub(a, b)
                pr.cprint("green", f"结果: {a} - {b} = {result}")
            elif choice == "3":
                result = calu.mul(a, b)
                pr.cprint("green", f"结果: {a} * {b} = {result}")
            elif choice == "4":
                q, r = calu.div(a, b)
                pr.cprint("green", f"结果: {a} ÷  {b} = {q} (余数 {r})")
        except ZeroDivisionError as e:
            pr.cprint("red", f"错误: {e}")


def main():
    """程序入口"""
    calu: IntCalculate = IntCalculate()
    pr: Printer = Printer()
    menu(calu, pr)


if __name__ == "__main__":
    main()
