from tkinter import *
from tkinter import messagebox
import tkinter as tk
import time

# 声明 result 为全局变量
result = 0
key = 0
# 输入的明文
resultminwen = ""

# 输入的密文
resultjiamwen = ""

# 输入的密钥
resultkey = ""

# 输出的明文
putminwen = ""

# 输出的密文
putjiamwen = ""

ciphertext = ""  # 最终的密文
plaintext = ""  # 最终的明文


class Appbidget(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("S-DES算法加密与解密工具")  # 设置窗口标题
        self.master.geometry("500x400")  # 设置窗口大小
        self.pack()

        self.widget()

    def widget(self):
        # 设置按钮的行和列间隔
        padding = 10

        # 标签说明
        self.label = tk.Label(self, text="请选择操作:", font=("Arial", 12))
        self.label.grid(row=0, column=0, columnspan=2, padx=padding, pady=(padding, 10))

        # 加密按钮
        self.testbtn01 = Button(self, text="01bit进行加密", command=self.changejiami, width=20)
        self.testbtn01.grid(row=1, column=0, padx=padding, pady=padding)

        # 解密按钮
        self.testbtn02 = Button(self, text="01bit进行解密", command=self.changejiemi, width=20)
        self.testbtn02.grid(row=1, column=1, padx=padding, pady=padding)

        # ASCII加密按钮
        self.testbtn03 = Button(self, text="ASCII进行加密", command=self.ascchangejiami, width=20)
        self.testbtn03.grid(row=2, column=0, padx=padding, pady=padding)

        # ASCII解密按钮
        self.testbtn04 = Button(self, text="ASCII进行解密", command=self.ascchangejiemi, width=20)
        self.testbtn04.grid(row=2, column=1, padx=padding, pady=padding)

        # 求解密钥按钮
        self.testbtn05 = Button(self, text="求解密钥", command=self.qiujiemiyao, width=20)
        self.testbtn05.grid(row=4, column=0, columnspan=2, padx=padding, pady=padding)

        # 封装测试按钮
        self.testbtn06 = Button(self, text="封装测试", command=self.qiujiemiyao2, width=20)
        self.testbtn06.grid(row=5, column=0, columnspan=2, padx=padding, pady=padding)
        # Unicode加密按钮
        self.testbtn07 = Button(self, text="UNICODE进行加密", command=self.unicode_jiami, width=20)
        self.testbtn07.grid(row=3, column=0, padx=padding, pady=padding)
        # Unicode解密按钮
        self.testbtn08 = Button(self, text="UNICODE进行解密", command=self.unicode_jiemi, width=20)
        self.testbtn08.grid(row=3, column=1, padx=padding, pady=padding)
        # 退出按钮
        self.exit_button = Button(self, text="退出", command=self.master.destroy, width=20)
        self.exit_button.grid(row=6, column=0, columnspan=2, padx=padding, pady=padding)

    def qiujiemiyao2(self):
        self.master.destroy()
        root1 = Tk()
        root1.geometry("500x400+200+300")
        root1.title("封装测试页面")

        Application6(master=root1)
        root1.mainloop()

    def qiujiemiyao(self):
        self.master.destroy()
        root1 = Tk()
        root1.geometry("500x400+200+300")
        root1.title("封装测试页面")

        Application5(master=root1)
        root1.mainloop()

    def changejiami(self):
        self.master.destroy()
        root1 = Tk()
        root1.geometry("500x400+200+300")
        root1.title("01bitS-DES算法加密页面")

        Application1(master=root1)
        root1.mainloop()

    def changejiemi(self):
        self.master.destroy()
        root2 = Tk()
        root2.geometry("500x400+200+300")
        root2.title("01bitS-DES算法解密页面")

        Application2(master=root2)
        root2.mainloop()

    def ascchangejiami(self):
        self.master.destroy()
        root1 = Tk()
        root1.geometry("500x400+200+300")
        root1.title("ascii码S-DES算法加密页面")

        Application3(master=root1)
        root1.mainloop()

    def ascchangejiemi(self):
        self.master.destroy()
        root2 = Tk()
        root2.geometry("500x400+200+300")
        root2.title("ascii码S-DES算法解密页面")

        Application4(master=root2)
        root2.mainloop()

    def unicode_jiami(self):
        self.master.destroy()
        root1 = Tk()
        root1.geometry("500x400+200+300")
        root1.title("unicode码S-DES算法加密页面")

        Application7(master=root1)
        root1.mainloop()

    def unicode_jiemi(self):
        self.master.destroy()
        root2 = Tk()
        root2.geometry("500x400+200+300")
        root2.title("unicode码S-DES算法解密页面")

        Application8(master=root2)
        root2.mainloop()


# 封装测试
class Application6(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.qiujiemiyao()

    def qiujiemiyao(self):
        padding = 8  # 设置按钮和输入框之间的间距

        # 输入明文内容
        self.entry1 = tk.Entry(self)
        self.entry1.grid(row=0, column=1, padx=padding, pady=padding)
        self.button2 = tk.Button(self, text="键入明文内容(8 bits)", command=self.getitem1)
        self.button2.grid(row=0, column=0, padx=padding, pady=padding)

        # 求解已知明文的不同密钥所得的相同密文
        self.button111 = tk.Button(self, text="求解明文是否有不同的密钥加密成相同的密文", command=self.qiumiyao1)
        self.button111.grid(row=2, column=0, columnspan=2, padx=padding, pady=padding)

        # 返回按钮
        self.btnQuit = tk.Button(self, text="返回", command=self.fanhui)
        self.btnQuit.grid(row=3, column=0, columnspan=2, padx=padding, pady=padding)

        # 密文结果文本框
        self.result_text = tk.Text(self, wrap=tk.WORD, height=5, width=40)
        self.result_text.grid(row=4, column=0, columnspan=2, padx=padding, pady=padding)

        # 添加一个说明标签
        self.info_label = tk.Label(self, text="求解结果结果将显示在上面:", font=("Arial", 10, "italic"))
        self.info_label.grid(row=5, column=0, columnspan=2, padx=padding, pady=(5, 0))

    def qiumiyao1(self):
        keys_found = []  # 用于存储所有找到的密钥
        miwen_found = {}  # 用于存储密文与其对应的密钥

        if resultminwen:  # 检测明文不为空
            for i in range(1024):  # 生成0到1024范围的密钥
                key2 = format(i, '010b')  # 转换为10位二进制密钥
                temp = encrypt(resultminwen, key2)  # 使用当前密钥加密明文

                # 检查密文是否已存在
                if temp in miwen_found:
                    miwen_found[temp].append(key2)  # 添加当前密钥到已有密文的密钥列表
                else:
                    miwen_found[temp] = [key2]  # 新密文，初始化密钥列表

            # 处理结果
            matching_keys_info = []
            for c, keys in miwen_found.items():
                if len(keys) > 1:  # 只关心那些有多个密钥的密文
                    matching_keys_info.append(f"密文: {c} | 密钥: {', '.join(keys)}")

            if matching_keys_info:
                keys_output = "满足条件的密文及其密钥:\n" + "\n".join(matching_keys_info)
                self.result_text.delete(1.0, tk.END)  # 清空文本框
                self.result_text.insert(tk.END, keys_output)  # 显示加密结果
            else:
                messagebox.showwarning("ERROR", "不存在不同密钥产生相同密文的情况")

    def fanhui(self):
        self.master.destroy()
        windows4 = tk.Tk()
        windows4.geometry("500x400+200+300")
        windows4.title("选择页面")
        Appbidget(master=windows4)
        windows4.mainloop()

    def getitem1(self):
        global resultminwen
        resultminwen = self.entry1.get()

        if len(resultminwen) > 0 and len(resultminwen) % 8 == 0 and all(bit in '01' for bit in resultminwen):
            messagebox.showinfo("输入的明文为", resultminwen)
        else:
            messagebox.showwarning("ERROR!", "输入错误，请输入8位的01字符串！")
            resultminwen = ""


# 求解密钥
class Application5(Frame):
    def __init__(self, master=None):
        super().__init__(master)  # super()代表父类的定义
        self.master = master
        self.pack()
        self.qiujiemiyao()

    def qiujiemiyao(self):
        padding = 8  # 设置按钮和输入框之间的间距

        # 输入明文内容
        self.entry1 = tk.Entry(self)
        self.entry1.grid(row=0, column=1, padx=padding, pady=padding)
        self.button2 = tk.Button(self, text="键入明文内容(8 bits)", command=self.getitem1)
        self.button2.grid(row=0, column=0, padx=padding, pady=padding)

        # 输入密文内容
        self.entry2 = tk.Entry(self)
        self.entry2.grid(row=1, column=1, padx=padding, pady=padding)
        self.button3 = tk.Button(self, text="键入密文内容(8 bits)", command=self.getitem3)
        self.button3.grid(row=1, column=0, padx=padding, pady=padding)

        # 求解密钥
        self.button111 = tk.Button(self, text="求解密钥", command=self.qiumiyao)
        self.button111.grid(row=2, column=0, columnspan=2, padx=padding, pady=padding)

        # 返回按钮
        self.btnQuit = tk.Button(self, text="返回", command=self.fanhui)
        self.btnQuit.grid(row=3, column=0, columnspan=2, padx=padding, pady=padding)

        # 密文结果文本框
        self.result_text = tk.Text(self, wrap=tk.WORD, height=5, width=40)
        self.result_text.grid(row=4, column=0, columnspan=2, padx=padding, pady=padding)

        # 添加一个说明标签
        self.info_label = tk.Label(self, text="密钥结果将显示在上面:", font=("Arial", 10, "italic"))
        self.info_label.grid(row=5, column=0, columnspan=2, padx=padding, pady=(5, 0))

    def qiumiyao(self):
        keys_found = []  # 用于存储所有找到的密钥
        time_found = []  # 用于储存所有的时间搓

        if resultminwen and resultjiamwen:
            start_time = time.time()  # 记录开始时间
            count = 1
            for i in range(1024):  # 0到1024的范围
                print("第", count, "次暴力破解")
                key2 = format(i, '010b')  # 转换为10位二进制密钥
                temp = encrypt(resultminwen, key2)  # 使用当前密钥加密明文

                if temp == resultjiamwen:  # 检查加密结果是否匹配
                    print("第", count, "次破解成功")
                    time2 = time.time()  # 记录成功破解的时间
                    print(f"时间为 {1000 * (time2 - start_time):.3f} 毫秒")  # 输出耗时（毫秒）
                    keys_found.append(key2)  # 如果匹配，将密钥添加到列表中
                    timex = time2 - start_time
                    time_found.append(timex)  # 如果匹配，将时间添加到列表中
                count += 1

            end_time = time.time()  # 记录结束时间
            elapsed_time = 1000 * (end_time - start_time)  # 将耗时转换为毫秒

            # 将所有找到的密钥输出到一个页面
            if keys_found:
                keys_output = "找到的密钥及耗时:\n"
                for key, time2 in zip(keys_found, time_found):
                    time222 = time2 * 1000
                    keys_output += f"密钥: {key}，破解时间: {time222:.3f} 毫秒\n"

            else:
                keys_output = "没有找到匹配的密钥。"

            keys_output += f"\n\n暴力破解总耗时: {elapsed_time:.3f} 毫秒"  # 保留3位小数并输出毫秒

            # 使用 messagebox 显示结果
            self.result_text.delete(1.0, tk.END)  # 清空文本框
            self.result_text.insert(tk.END, keys_output)  # 显示加密结果
        else:
            messagebox.showwarning("error", "密文或者明文不能为空")

    def fanhui(self):
        self.master.destroy()
        windows4 = Tk()
        windows4.geometry("500x400+200+300")
        windows4.title("选择页面")

        Appbidget(master=windows4)
        windows4.mainloop()

    def getitem1(self):
        global resultminwen
        resultminwen = self.entry1.get()

        if len(resultminwen) > 0 and len(resultminwen) % 8 == 0 and all(bit in '01' for bit in resultminwen):
            messagebox.showinfo("输入的明文为", resultminwen)
        else:
            messagebox.showwarning("ERROR!", "输入错误，请输入8位的01字符串！")
            resultminwen = ""

    def getitem3(self):
        global resultjiamwen
        resultjiamwen = self.entry2.get()

        if len(resultjiamwen) > 0 and len(resultjiamwen) % 8 == 0 and all(bit in '01' for bit in resultjiamwen):
            messagebox.showinfo("输入的密文为", resultjiamwen)
        else:
            messagebox.showwarning("ERROR!", "输入错误，请输入8位的01字符串！")
            resultjiamwen = ""


# 01bit加密页面
class Application1(Frame):
    """一个经典的gui"""

    def __init__(self, master=None):
        super().__init__(master)  # super()代表父类的定义
        self.master = master
        self.pack()
        self.createWidget1()

    def createWidget1(self):
        padding = 8  # 设置按钮和输入框之间的间距

        # 输入明文内容
        self.entry1 = tk.Entry(self)
        self.entry1.grid(row=0, column=1, padx=padding, pady=padding)
        self.button2 = tk.Button(self, text="键入明文内容(8 bits)", command=self.getitem1)
        self.button2.grid(row=0, column=0, padx=padding, pady=padding)

        # 输入密钥内容
        self.entry2 = tk.Entry(self)
        self.entry2.grid(row=1, column=1, padx=padding, pady=padding)
        self.button3 = tk.Button(self, text="键入密钥内容(10 bits)", command=self.getitem2)
        self.button3.grid(row=1, column=0, padx=padding, pady=padding)

        # 加密按钮
        self.button111 = tk.Button(self, text="加密", command=self.jiami)
        self.button111.grid(row=2, column=0, columnspan=2, padx=padding, pady=padding)

        # 返回按钮
        self.btnQuit = tk.Button(self, text="返回", command=self.fanhui)
        self.btnQuit.grid(row=3, column=0, columnspan=2, padx=padding, pady=padding)

        # 密文结果文本框
        self.result_text = tk.Text(self, wrap=tk.WORD, height=3, width=20)
        self.result_text.grid(row=4, column=0, columnspan=2, padx=padding, pady=padding)

        # 密文结果文本框
        self.result_text = tk.Text(self, wrap=tk.WORD, height=5, width=40)
        self.result_text.grid(row=4, column=0, columnspan=2, padx=padding, pady=padding)

        # 添加一个说明标签
        self.info_label = tk.Label(self, text="加密结果将显示在上面:", font=("Arial", 10, "italic"))
        self.info_label.grid(row=5, column=0, columnspan=2, padx=padding, pady=(5, 0))

    def fanhui(self):
        self.master.destroy()
        windows4 = Tk()
        windows4.geometry("500x400+200+300")
        windows4.title("选择页面")

        Appbidget(master=windows4)
        windows4.mainloop()

    def jiami(self):
        global putminwen, resultminwen, resultkey

        if not resultminwen or not resultkey:
            messagebox.showwarning("警告", "明文或密钥不能为空！")
            return

            # 确保输入是有效的8位二进制字符串
        if len(resultminwen) % 8 != 0 or not all(bit in '01' for bit in resultminwen):
            messagebox.showwarning("ERROR!", "输入错误，请输入多个8位的01字符串！")
            return

        # 拆分输入为多个8位二进制字符串
        groups = [resultminwen[i:i + 8] for i in range(0, len(resultminwen), 8)]

        # 加密每组数据
        ciphertext_parts = []
        for group in groups:
            ciphertext = encrypt(group, resultkey)
            ciphertext_parts.append(ciphertext)

            # 拼接最终密文
        final_ciphertext = ''.join(ciphertext_parts)

        self.result_text.delete(1.0, tk.END)  # 清空之前的内容
        self.result_text.insert(tk.END, final_ciphertext)  # 插入新的结果

    def getitem1(self):
        global resultminwen
        resultminwen = self.entry1.get()

        if len(resultminwen) > 0 and len(resultminwen) % 8 == 0 and all(bit in '01' for bit in resultminwen):
            messagebox.showinfo("输入的明文为", resultminwen)
        else:
            messagebox.showwarning("ERROR!", "输入错误，请输入多个8位的01字符串！")
            resultminwen = ""

    def getitem2(self):
        global resultkey
        resultkey = self.entry2.get()
        if (len(resultkey) != 10):
            messagebox.showwarning("ERROR!", "输入错误请重新输入！")
            resultkey = ""
        else:
            messagebox.showinfo("输入的密钥为", resultkey)


# 01bit解密页面
class Application2(Frame):
    """一个经典的gui"""

    def __init__(self, master=None):
        super().__init__(master)  # super()代表父类的定义
        self.master = master
        self.pack()
        self.createWidget2()

    def createWidget2(self):
        padding = 8  # 设置按钮和输入框之间的间隙

        # 输入密文内容
        self.entry3 = tk.Entry(self)
        self.entry3.grid(row=0, column=1, padx=padding, pady=padding)
        self.button4 = tk.Button(self, text="键入密文内容(8 bits)", command=self.getitem3)
        self.button4.grid(row=0, column=0, padx=padding, pady=padding)

        # 输入密钥内容
        self.entry2 = tk.Entry(self)
        self.entry2.grid(row=1, column=1, padx=padding, pady=padding)
        self.button3 = tk.Button(self, text="键入密钥内容(10 bits)", command=self.getitem2)
        self.button3.grid(row=1, column=0, padx=padding, pady=padding)

        # 解密按钮
        self.button222 = tk.Button(self, text="解密", command=self.jiemi)
        self.button222.grid(row=2, column=0, columnspan=2, padx=padding, pady=padding)

        # 返回按钮
        self.btnQuit = Button(self, text="返回", command=self.fanhui)
        self.btnQuit.grid(row=3, column=0, columnspan=2, padx=padding, pady=padding)

        # 明文文结果文本框
        self.result_text = tk.Text(self, wrap=tk.WORD, height=5, width=40)
        self.result_text.grid(row=4, column=0, columnspan=2, padx=padding, pady=padding)

        # 添加一个说明标签
        self.info_label = tk.Label(self, text="解密结果将显示在上面:", font=("Arial", 10, "italic"))
        self.info_label.grid(row=5, column=0, columnspan=2, padx=padding, pady=(5, 0))

    def fanhui(self):
        self.master.destroy()
        windows4 = Tk()
        windows4.geometry("500x400+200+300")
        windows4.title("选择页面")

        Appbidget(master=windows4)
        windows4.mainloop()

    def jiemi(self):
        global resultjiamwen, resultkey

        if not resultjiamwen or not resultkey:
            messagebox.showwarning("警告", "密文或密钥不能为空！")
            return

            # 确保密文是有效的8位二进制字符串
        if len(resultjiamwen) % 8 != 0 or not all(bit in '01' for bit in resultjiamwen):
            messagebox.showwarning("ERROR!", "输入错误，请输入有效的密文！")
            return

            # 拆分密文为多个8位二进制字符串
        groups = [resultjiamwen[i:i + 8] for i in range(0, len(resultjiamwen), 8)]

        # 解密每组数据
        plaintext_parts = []
        for group in groups:
            plaintext_binary = decrypt(group, resultkey)
            plaintext_parts.append(plaintext_binary)

            # 拼接最终明文
        final_plaintext = ''.join(plaintext_parts)

        self.result_text.delete(1.0, tk.END)  # 清空之前的内容
        self.result_text.insert(tk.END, final_plaintext)  # 插入新的结果

    def getitem3(self):
        global resultjiamwen
        resultjiamwen = self.entry3.get()

        if len(resultjiamwen) > 0 and len(resultjiamwen) % 8 == 0 and all(bit in '01' for bit in resultjiamwen):
            messagebox.showinfo("输入的密文为", resultjiamwen)
        else:
            messagebox.showwarning("ERROR!", "输入错误，请输入多个8位的01字符串！")
            resultjiamwen = ""

    def getitem2(self):
        global resultkey
        resultkey = self.entry2.get()
        if (len(resultkey) != 10):
            messagebox.showwarning("ERROR!", "输入错误请重新输入！")
            resultkey = ""
        else:
            messagebox.showinfo("输入的密钥为", resultkey)


# ascill码的加密页面
class Application3(Frame):
    """一个经典的gui"""

    def __init__(self, master=None):
        super().__init__(master)  # super()代表父类的定义
        self.master = master
        self.pack()
        self.createWidget1()

    def createWidget1(self):
        padding = 8  # 设置按钮和输入框之间的间距

        # 输入明文内容
        self.entry1 = tk.Entry(self)
        self.entry1.grid(row=0, column=1, padx=padding, pady=padding)
        self.button2 = tk.Button(self, text="键入明文内容(字符)", command=self.getitem1)
        self.button2.grid(row=0, column=0, padx=padding, pady=padding)

        # 输入密钥内容
        self.entry2 = tk.Entry(self)
        self.entry2.grid(row=1, column=1, padx=padding, pady=padding)
        self.button3 = tk.Button(self, text="键入密钥内容(10 bit)", command=self.getitem2)
        self.button3.grid(row=1, column=0, padx=padding, pady=padding)

        # 加密按钮
        self.button111 = tk.Button(self, text="加密", command=self.jiami)
        self.button111.grid(row=2, column=0, columnspan=2, padx=padding, pady=padding)

        # 返回按钮
        self.btnQuit = tk.Button(self, text="返回", command=self.fanhui)
        self.btnQuit.grid(row=3, column=0, columnspan=2, padx=padding, pady=padding)

        # 密文结果文本框
        self.result_text = tk.Text(self, wrap=tk.WORD, height=5, width=40)
        self.result_text.grid(row=4, column=0, columnspan=2, padx=padding, pady=padding)

        # 添加一个说明标签
        self.info_label = tk.Label(self, text="加密结果将显示在上面:", font=("Arial", 10, "italic"))
        self.info_label.grid(row=5, column=0, columnspan=2, padx=padding, pady=(5, 0))

    def fanhui(self):
        self.master.destroy()
        windows4 = Tk()
        windows4.geometry("500x400+200+300")
        windows4.title("选择页面")

        Appbidget(master=windows4)
        windows4.mainloop()

    def jiami(self):
        global resultminwen, resultkey

        if not resultminwen or not resultkey:
            messagebox.showwarning("警告", "明文或密钥不能为空！")
            return

            # 将输入的明文转换为二进制格式
        binary_input = ascii_to_bin(resultminwen)

        # 拆分输入为多个8位二进制字符串
        groups = [binary_input[i:i + 8] for i in range(0, len(binary_input), 8)]

        # 加密每组数据
        ciphertext_parts = []
        for group in groups:
            ciphertext = encrypt(group, resultkey)
            ciphertext_parts.append(ciphertext)

            # 将密文拼接为ASCII形式
        final_ciphertext = bin_to_ascii(''.join(ciphertext_parts))
        self.result_text.delete(1.0, tk.END)  # 清空之前的内容
        self.result_text.insert(tk.END, final_ciphertext)  # 插入新的结果

    def getitem1(self):
        global resultminwen
        resultminwen = self.entry1.get()

        if len(resultminwen) > 0:
            messagebox.showinfo("输入的明文为", resultminwen)
        else:
            messagebox.showwarning("ERROR!", "输入错误，请输入有效的文本！")
            resultminwen = ""

    def getitem2(self):
        global resultkey
        resultkey = self.entry2.get()
        if (len(resultkey) != 10):
            messagebox.showwarning("ERROR!", "输入错误请重新输入！")
            resultkey = ""
        else:
            messagebox.showinfo("输入的密钥为", resultkey)


# ascill码的解密页面
class Application4(Frame):
    """一个经典的gui"""

    def __init__(self, master=None):
        super().__init__(master)  # super()代表父类的定义
        self.master = master
        self.pack()
        self.createWidget2()

    def createWidget2(self):
        padding = 8  # 设置按钮和输入框之间的间隙

        # 输入密文内容
        self.entry3 = tk.Entry(self)
        self.entry3.grid(row=0, column=1, padx=padding, pady=padding)
        self.button4 = tk.Button(self, text="键入密文内容(字符)", command=self.getitem3)
        self.button4.grid(row=0, column=0, padx=padding, pady=padding)

        # 输入密钥内容
        self.entry2 = tk.Entry(self)
        self.entry2.grid(row=1, column=1, padx=padding, pady=padding)
        self.button3 = tk.Button(self, text="键入密钥内容(10 bits)", command=self.getitem2)
        self.button3.grid(row=1, column=0, padx=padding, pady=padding)

        # 解密按钮
        self.button222 = tk.Button(self, text="解密", command=self.jiemi)
        self.button222.grid(row=2, column=0, columnspan=2, padx=padding, pady=padding)

        # 返回按钮
        self.btnQuit = Button(self, text="返回", command=self.fanhui)
        self.btnQuit.grid(row=3, column=0, columnspan=2, padx=padding, pady=padding)

        # 明文结果文本框
        self.result_text = tk.Text(self, wrap=tk.WORD, height=5, width=40)
        self.result_text.grid(row=4, column=0, columnspan=2, padx=padding, pady=padding)

        # 添加一个说明标签
        self.info_label = tk.Label(self, text="解密结果将显示在上面:", font=("Arial", 10, "italic"))
        self.info_label.grid(row=5, column=0, columnspan=2, padx=padding, pady=(5, 0))

    def fanhui(self):
        self.master.destroy()
        windows4 = Tk()
        windows4.geometry("500x400+200+300")
        windows4.title("选择页面")

        Appbidget(master=windows4)
        windows4.mainloop()

    def jiemi(self):
        global resultjiamwen, resultkey

        if not resultjiamwen or not resultkey:
            messagebox.showwarning("警告", "密文或密钥不能为空！")
            return

            # 确保密文是有效的输入
        try:
            # 将密文进行分组和解密
            binary_input = ascii_to_bin(resultjiamwen)
            if len(binary_input) % 8 != 0:
                raise ValueError("输入错误，请用有效的ASCII字符串！")

            groups = [binary_input[i:i + 8] for i in range(0, len(binary_input), 8)]

            # 解密每组数据
            plaintext_parts = []
            for group in groups:
                plaintext_binary = decrypt(group, resultkey)
                plaintext_parts.append(plaintext_binary)

                # 拼接最终明文，并将其转换为 ASCII 格式
            final_plaintext = bin_to_ascii(''.join(plaintext_parts))
            self.result_text.delete(1.0, tk.END)  # 清空之前的内容
            self.result_text.insert(tk.END, final_plaintext)  # 插入新的结果

        except Exception as e:
            messagebox.showwarning("ERROR!", str(e))

    def getitem3(self):
        global resultjiamwen
        resultjiamwen = self.entry3.get()

        if len(resultjiamwen) > 0:
            messagebox.showinfo("输入的密文为", resultjiamwen)
        else:
            messagebox.showwarning("ERROR!", "输入错误，请输入有效的文本！")
            resultjiamwen = ""

    def getitem2(self):
        global resultkey
        resultkey = self.entry2.get()
        if (len(resultkey) != 10):
            messagebox.showwarning("ERROR!", "输入错误请重新输入！")
            resultkey = ""
        else:
            messagebox.showinfo("输入的密钥为", resultkey)


# unicode码的加密页面
class Application7(Frame):
    """一个经典的gui"""

    def __init__(self, master=None):
        super().__init__(master)  # super()代表父类的定义
        self.master = master
        self.pack()
        self.createWidget1()

    def createWidget1(self):
        padding = 8  # 设置按钮和输入框之间的间距

        # 输入明文内容
        self.entry1 = tk.Entry(self)
        self.entry1.grid(row=0, column=1, padx=padding, pady=padding)
        self.button2 = tk.Button(self, text="键入明文内容(字符)", command=self.getitem1)
        self.button2.grid(row=0, column=0, padx=padding, pady=padding)

        # 输入密钥内容
        self.entry2 = tk.Entry(self)
        self.entry2.grid(row=1, column=1, padx=padding, pady=padding)
        self.button3 = tk.Button(self, text="键入密钥内容(10 bit)", command=self.getitem2)
        self.button3.grid(row=1, column=0, padx=padding, pady=padding)

        # 加密按钮
        self.button111 = tk.Button(self, text="加密", command=self.encryptUnicode)
        self.button111.grid(row=2, column=0, columnspan=2, padx=padding, pady=padding)

        # 返回按钮
        self.btnQuit = tk.Button(self, text="返回", command=self.fanhui)
        self.btnQuit.grid(row=3, column=0, columnspan=2, padx=padding, pady=padding)

        # 密文结果文本框
        self.result_text = tk.Text(self, wrap=tk.WORD, height=5, width=40)
        self.result_text.grid(row=4, column=0, columnspan=2, padx=padding, pady=padding)

        # 添加一个说明标签
        self.info_label = tk.Label(self, text="加密结果将显示在上面:", font=("Noto Sans", 10, "italic"))
        self.info_label.grid(row=5, column=0, columnspan=2, padx=padding, pady=(5, 0))

    def fanhui(self):
        self.master.destroy()
        windows4 = Tk()
        windows4.geometry("500x400+200+300")
        windows4.title("选择页面")

        Appbidget(master=windows4)
        windows4.mainloop()

    # 加密unicode函数
    def encryptUnicode(self):
        global resultminwen, resultkey

        if not resultminwen or not resultkey:
            messagebox.showwarning("警告", "明文或密钥不能为空！")
            return
        binary_list = unicode2binary(resultminwen)
        final_ciphertext = ''

        for binary in binary_list:
            left = binary[:8]  # 高8位
            right = binary[8:]  # 低8位

            # 加密高8位和低8位
            encrypted_left = encrypt(left, resultkey)
            encrypted_right = encrypt(right, resultkey)

            # 合并加密后的结果
            combined_binary = encrypted_left + encrypted_right

            # 转换为Unicode字符并追加到结果
            unicode_char = chr(int(combined_binary, 2))  # 将二进制转换为整数，再转换为字符
            final_ciphertext += unicode_char
        self.result_text.delete(1.0, tk.END)  # 清空之前的内容
        self.result_text.insert(tk.END, final_ciphertext)  # 插入新的结果

    def getitem1(self):
        global resultminwen
        resultminwen = self.entry1.get()

        if len(resultminwen) > 0:
            messagebox.showinfo("输入的明文为", resultminwen)
        else:
            messagebox.showwarning("ERROR!", "输入错误，请输入有效的文本！")
            resultminwen = ""

    def getitem2(self):
        global resultkey
        resultkey = self.entry2.get()
        if (len(resultkey) != 10):
            messagebox.showwarning("ERROR!", "输入错误请重新输入！")
            resultkey = ""
        else:
            messagebox.showinfo("输入的密钥为", resultkey)


# unicode编码的解密页面
class Application8(Frame):
    """一个经典的gui"""

    def __init__(self, master=None):
        super().__init__(master)  # super()代表父类的定义
        self.master = master
        self.pack()
        self.createWidget2()

    def createWidget2(self):
        padding = 8  # 设置按钮和输入框之间的间隙

        # 输入密文内容
        self.entry3 = tk.Entry(self)
        self.entry3.grid(row=0, column=1, padx=padding, pady=padding)
        self.button4 = tk.Button(self, text="键入密文内容(字符)", command=self.getitem3)
        self.button4.grid(row=0, column=0, padx=padding, pady=padding)

        # 输入密钥内容
        self.entry4 = tk.Entry(self)
        self.entry4.grid(row=1, column=1, padx=padding, pady=padding)
        self.button3 = tk.Button(self, text="键入密钥内容(10 bits)", command=self.getitem2)
        self.button3.grid(row=1, column=0, padx=padding, pady=padding)

        # 解密按钮
        self.button222 = tk.Button(self, text="解密", command=self.decryptUnicode)
        self.button222.grid(row=2, column=0, columnspan=2, padx=padding, pady=padding)

        # 返回按钮
        self.btnQuit = Button(self, text="返回", command=self.fanhui)
        self.btnQuit.grid(row=3, column=0, columnspan=2, padx=padding, pady=padding)

        # 明文文结果文本框
        self.result_text = tk.Text(self, wrap=tk.WORD, height=5, width=40)
        self.result_text.grid(row=4, column=0, columnspan=2, padx=padding, pady=padding)

        # 添加一个说明标签
        self.info_label = tk.Label(self, text="解密结果将显示在上面:", font=("Arial", 10, "italic"))
        self.info_label.grid(row=5, column=0, columnspan=2, padx=padding, pady=(5, 0))

    def fanhui(self):
        self.master.destroy()
        windows4 = Tk()
        windows4.geometry("500x400+200+300")
        windows4.title("选择页面")

        Appbidget(master=windows4)
        windows4.mainloop()

    def getitem3(self):
        global resultjiamwen
        resultjiamwen = self.entry3.get()

        if len(resultjiamwen) > 0:
            messagebox.showinfo("输入的密文为", resultjiamwen)
        else:
            messagebox.showwarning("ERROR!", "输入错误，请输入有效的文本！")
            resultjiamwen = ""

    def getitem2(self):
        global resultkey
        resultkey = self.entry4.get()
        if (len(resultkey) != 10):
            messagebox.showwarning("ERROR!", "输入错误请重新输入！")
            resultkey = ""
        else:
            messagebox.showinfo("输入的密钥为", resultkey)

    # 解密unicode函数
    def decryptUnicode(self):
        global resultjiamwen, resultkey

        try:
            if not resultjiamwen or not resultkey:
                messagebox.showwarning("警告", "密文或密钥不能为空！")
                return

            binary_list = unicode2binary(resultjiamwen)  # 假设这里是 resultjiamwen 而不是 resultminwen
            final_ciphertext = ''

            for binary in binary_list:
                left = binary[:8]  # 高8位
                right = binary[8:]  # 低8位

                # 解密高8位和低8位
                decrypted_left = decrypt(left, resultkey)
                decrypted_right = decrypt(right, resultkey)

                # 合并解密后的结果
                combined_binary = decrypted_left + decrypted_right

                # 转换为Unicode字符并追加到结果
                unicode_char = chr(int(combined_binary, 2))  # 将二进制转换为整数，再转换为字符
                final_ciphertext += unicode_char
            self.result_text.delete(1.0, tk.END)  # 清空之前的内容
            self.result_text.insert(tk.END, final_ciphertext)  # 插入新的结果

        except Exception as e:
            messagebox.showerror("错误", f"解密过程中发生错误: {e}")


def permute(bits, indices):
    # 根据给定索引对位串进行置换
    return ''.join([bits[i - 1] for i in indices])


def left_shift(bits, num_shifts):
    # 对位串进行循环左移操作
    return bits[num_shifts:] + bits[:num_shifts]


def generate_keys(key_10bit):
    # P10 置换
    p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    key_p10 = permute(key_10bit, p10)

    # 分成左、右两部分
    left_half, right_half = key_p10[:5], key_p10[5:]

    # 执行 LS-1（循环左移1位）
    left_half = left_shift(left_half, 1)
    right_half = left_shift(right_half, 1)

    # P8 置换，生成子密钥 K1
    p8 = [6, 3, 7, 4, 8, 5, 10, 9]
    k1 = permute(left_half + right_half, p8)

    # 执行 LS-2（循环左移2位）
    left_half = left_shift(left_half, 1)
    right_half = left_shift(right_half, 1)

    # P8 置换，生成子密钥 K2
    k2 = permute(left_half + right_half, p8)

    return k1, k2


def sbox(input_bits, sbox):
    # 根据输入位串和 S 盒进行 S 盒变换
    row = int(input_bits[0] + input_bits[3], 2)
    column = int(input_bits[1] + input_bits[2], 2)
    return format(sbox[row][column], '02b')


def fk(bits, key, count):
    # 初始置换 (IP)
    if count == 1:
        # 初始置换 (IP)
        ip = [2, 6, 3, 1, 4, 8, 5, 7]
        bits = permute(bits, ip)

    # print(f"第{count}次：""* "+bits+"*")
    # 分成左、右两部分
    left, right = bits[:4], bits[4:]
    # print("L " + left + "L")
    # print("R " + right + "R")
    # 扩展置换右半部分 (E/P)
    ep = [4, 1, 2, 3, 2, 3, 4, 1]
    right_expanded = permute(right, ep)

    # 与密钥进行异或运算
    xor_result = format(int(right_expanded, 2) ^ int(key, 2), '08b')
    # print(f"第{count}次：""异或 "+xor_result+"异或")
    # S 盒运算
    s0 = [[1, 0, 3, 2],
          [3, 2, 1, 0],
          [0, 2, 1, 3],
          [3, 1, 0, 2]]

    s1 = [[0, 1, 2, 3],
          [2, 3, 1, 0],
          [3, 0, 1, 2],
          [2, 1, 0, 3]]

    left_sbox_input = xor_result[:4]
    right_sbox_input = xor_result[4:]

    # 通过 S 盒进行变换
    sbox_output = sbox(left_sbox_input, s0) + sbox(right_sbox_input, s1)
    # print(f"第{count}次：""Sbox " + sbox_output + "Sbox ")
    # P4 置换
    p4 = [2, 4, 3, 1]
    p4_output = permute(sbox_output, p4)
    # print(f"第{count}次：""S-Pbox " + p4_output + "S-Pbox ")
    # 与左半部分进行异或运算
    left_result = format(int(left, 2) ^ int(p4_output, 2), '04b')
    # print(f"第{count}次：""L " + left + " L  ")
    # print(f"第{count}次：""L XOR R " + left_result + " L XOR R ")
    return left_result + right


def encrypt(plaintext_8bit, key_10bit):
    # 生成子密钥 K1 和 K2(已验证)
    k1, k2 = generate_keys(key_10bit)
    # 使用 K1 进行第一轮加密
    result = fk(plaintext_8bit, k1, 1)

    # 交换左右半部分
    result = result[4:] + result[:4]

    # 使用 K2 进行第二轮加密
    result = fk(result, k2, 2)

    # 逆初始置换 (IP^-1)
    ip_inv = [4, 1, 3, 5, 7, 2, 8, 6]
    ciphertext = permute(result, ip_inv)

    return ciphertext


def decrypt(ciphertext_8bit, key_10bit):
    # 生成子密钥 K1 和 K2
    k1, k2 = generate_keys(key_10bit)

    # 第一轮解密（使用 K2）
    result = fk(ciphertext_8bit, k2, 1)

    # 交换左右半部分
    result = result[4:] + result[:4]

    # 第二轮解密（使用 K1）
    result = fk(result, k1, 2)

    # 逆初始置换 (IP^-1)
    ip_inv = [4, 1, 3, 5, 7, 2, 8, 6]
    plaintext = permute(result, ip_inv)

    return plaintext


def ascii_to_bin(ascii_str):
    return ''.join(format(ord(char), '08b') for char in ascii_str)


def bin_to_ascii(bin_str):
    if len(bin_str) % 8 != 0:
        raise ValueError("Binary string length must be a multiple of 8.")
    chars = [chr(int(bin_str[i:i + 8], 2)) for i in range(0, len(bin_str), 8)]
    return ''.join(chars)


# unicode转换为二进制
def unicode2binary(unicode_str):
    binary_list = []
    for char in unicode_str:
        unicode_val = ord(char)  # 获取字符的 Unicode 值
        binary_str = format(unicode_val, '016b')  # 转换为 16 位二进制字符串
        binary_list.append(binary_str)  # 存储二进制字符串
    return binary_list


# 选择加密或者解密页面
windows = Tk()
windows.geometry("400x300+200+300")
windows.title("选择页面")
app2 = Appbidget(master=windows)
windows.mainloop()



