# S-DES加密算法开发手册

## 一· S-DES基本概念与原理

​	S-DES（Simplified Data Encryption Standard）是一种简化版的对称密钥加密算法，它模拟了更复杂的DES（数据加密标准）算法的基本思想，但具有更简单的结构和较小的密钥长度。

### （一）密钥长度：

​	S-DES使用一个10位的密钥，通常表示为一个二进制数，例如 1010000010。

### （二）数据块大小：

​	S-DES对64位的数据块进行加密，这与传统的DES算法相同，但S-DES的操作更为简化。

### （三）加密过程：

​	S-DES的加密过程分为多个步骤，包括：

#### 	①密钥生成：

​		从10位密钥生成两个子密钥（K1 和 K2），用于两个加密轮。

#### 	②初始置换（IP）：

​		对输入数据块进行初始置换。

#### 	③轮函数（F）：

​		包含非线性变换和扩展的置换，使用子密钥进行加密。

#### 	④交换：

​		经过两轮加密后，交换数据块的左右部分。

#### 	⑤逆初始置换（IP⁻1）：

​		对结果进行逆置换，得到最终的密文。

### （四）解密过程：

解密过程与加密过程相似，但使用的子密钥顺序相反（先使用K2再使用K1）。

### （五）安全性：

​		虽然S-DES比DES简单且更易于实现，但它并不适合实际应用的安全需求。S-DES的主要目的是帮助学习者理解对称加密的基本概念。

## 二·代码实现

### （一）核心函数

```python
#密钥生成
def generate_keys(key_10bit):

#S盒变换
def sbox(input_bits, sbox):
    
#轮函数
def fk(bits, key,count):

#加密函数
def encrypt(plaintext_8bit, key_10bit):

#解密函数
def decrypt(ciphertext_8bit, key_10bit):

# 根据给定索引对位串进行置换
def permute(bits, indices):

# 对位串进行循环左移操作
def left_shift(bits, num_shifts):

#将ASCII码转成二进制
def ascii_to_bin(ascii_str):
    
#将二进制转成ASCII码
def bin_to_ascii(bin_str):
```

### （二）关键原理

#### 	①P10置换与P8置换（用于生成子密钥）

```python
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
```

​		P10置换和P8置换是密钥生成过程中的两个重要步骤。它们的主要作用是对输入的密钥进行置换和简化，以生成用于加密的子密钥。

P10与P8置换的输出位分别是[3, 5, 2, 7, 4, 10, 1, 9, 8, 6]和[6, 3, 7, 4, 8, 5, 10, 9]，通过此两次置换将原本的10-bit密钥压缩为8-bit，而P10与P8置换通过”permute(bits, indices)“函数实现

```python
def permute(bits, indices):
    # 根据给定索引对位串进行置换
    return ''.join([bits[i - 1] for i in indices])
```

#### 	②轮函数（F）

​		S-DES函数公式：
$$
f_k(L,R)=(L \oplus F(R,k_i),R)
$$
​		轮函数（F）是整个算法最核心的环节，它包括四个转换步骤：

##### 		（1）扩展置换：

```python
    # 分成左、右两部分
    left, right = bits[:4], bits[4:]
    # 扩展置换右半部分 (E/P)
    ep = [4, 1, 2, 3, 2, 3, 4, 1]
    right_expanded = permute(right, ep)
```

##### 		（2）用轮密钥：

​			扩展后的部分与原先子密钥（8-bit）进行异或运算:

```python
 # 与密钥进行异或运算
    xor_result = format(int(right_expanded, 2) ^ int(key, 2), '08b')
```

##### 		（3）替换盒S-Boxes

​			在S-DES中，有两个S盒，分别称为S盒0（S0）和S盒1（S1）。这两个S盒用于将输入的4位二进制数替换为不同的4位二进制数。S盒通过非线性映射来实现这种替换，这增加了密码的复杂性，使得输出与输入之间的关系不容易被猜测。

```python
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
```

​		sbox函数如下：

```python
def sbox(input_bits, sbox):
    # 根据输入位串和 S 盒进行 S 盒变换
    row = int(input_bits[0] + input_bits[3], 2)
    column = int(input_bits[1] + input_bits[2], 2)
    return format(sbox[row][column], '02b')
```

##### 		（4）直接置换（P4置换）

```python
# P4 置换
    p4 = [2, 4, 3, 1]
    p4_output = permute(sbox_output, p4)
    # print(f"第{count}次：""S-Pbox " + p4_output + "S-Pbox ")
    # 与左半部分进行异或运算
    left_result = format(int(left, 2) ^ int(p4_output, 2), '04b')		
```

## 三·代码测试

主界面：

<img src="photos\image-20241005200547692.png" alt="image-20241005200547692" style="zoom:50%;" />

有不同的功能可以进行选择：01bit进行加解密，ASCII码加解密，，求解密钥，封装测试。

### （一）第1关：基本测试

​	根据S-DES算法编写和调试程序，提供GUI解密支持用户交互。输入可以是8-bit的数据和10-bit的密钥，输出是8-bit的密文。



​	假设输入明文为10101010，输入密钥为1001011000，加密结果显示如下：

<img src="photos\image-20241004193549321.png" alt="image-20241004193549321" style="zoom:50%;" />

### （二）第2关：交叉测试

#### 	①其他开发团队的加密结果：

<img src="photos\image-20241004204218816.png" alt="image-20241004204218816" style="zoom:50%;" />

​		假设明文为10011001，密钥为1100101011，则生成的密文为11111101

#### 	②本开发团队的解密结果：

​		  <img src="photos\image-20241004204321916.png" alt="image-20241004204321916" style="zoom:50%;" />

​		解出的明文为10011001，交叉测试成功。

### （三）第3关：扩展功能

​		考虑到向实用性扩展，加密算法的数据输入可以是ASII编码字符串(分组为1 Byte)，对应地输出也可以是ACII字符串(很可能是乱码)。

#### 	①代码实现：

​      ASCII码加密过程：

```python
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
        messagebox.showinfo("加密结果", final_ciphertext)
        self.result_text.delete(1.0, tk.END)  # 清空之前的内容
        self.result_text.insert(tk.END, final_ciphertext)  # 插入新的结果

```

​		ASCII码解密过程：

```python
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
            messagebox.showinfo("解密结果", final_plaintext)
            self.result_text.delete(1.0, tk.END)  # 清空之前的内容
            self.result_text.insert(tk.END, final_plaintext)  # 插入新的结果

        except Exception as e:
            messagebox.showwarning("ERROR!", str(e))
```

#### 	②实际操作界面：

​		输入明文为adadada，密钥为1000101001，加密结果为îìîìîìîü

<img src="photos\image-20241004195614481.png" alt="image-20241004195614481" style="zoom:50%;" />

#### ③ASCII码的局限性：

由于S-DES 处理的是 8 位二进制数据，而 ASCII 码作为表示字符的一种编码方式，它的字符通常以 7 位或 8 位二进制数表示。故运用S-DES 加密 ASCII 码时可能会出现异常。

为解决以上问题，可以运用Unicode编码，因为S-DES 需要处理固定长度的 8 位二进制数据，而 Unicode 字符的长度可以从 1 到 4 字节不等。这意味着 Unicode 可以表示更广泛的字符集，包括 ASCII 字符集和其他语言的字符。

##### 代码实现：

```python
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
        messagebox.showinfo("加密结果", final_ciphertext)
        self.result_text.delete(1.0, tk.END)  # 清空之前的内容
        self.result_text.insert(tk.END, final_ciphertext)  # 插入新的结果

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

            messagebox.showinfo("解密结果", final_ciphertext)
            self.result_text.delete(1.0, tk.END)  # 清空之前的内容
            self.result_text.insert(tk.END, final_ciphertext)  # 插入新的结果

        except Exception as e:
            messagebox.showerror("错误", f"解密过程中发生错误: {e}")
```

以下是将Unicode编码转化为二进制的函数：

```python
# unicode转换为二进制
def unicode2binary(unicode_str):
    binary_list = []
    for char in unicode_str:
        unicode_val = ord(char)  # 获取字符的 Unicode 值
        binary_str = format(unicode_val, '016b')  # 转换为 16 位二进制字符串
        binary_list.append(binary_str)  # 存储二进制字符串
    return binary_list

```

##### 实际操作界面：

<img src="photos\image-20241005203014630.png" alt="image-20241005203014630" style="zoom:50%;" />

### (四)第4关：暴力破解

​		假设你找到了使用相同密钥的明、密文对(一个或多个)，请尝试使用暴力破解的方法找到正确的密钥Key。

#### 		①代码实现：

```python
 def qiumiyao(self):
        keys_found = []  # 用于存储所有找到的密钥
        time_found= [] #用于储存所有的时间搓

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
                    timex=time2-start_time
                    time_found.append(timex) # 如果匹配，将时间添加到列表中
                count += 1

            end_time = time.time()  # 记录结束时间
            elapsed_time = 1000 * (end_time - start_time)  # 将耗时转换为毫秒

            # 将所有找到的密钥输出到一个页面
            if keys_found:
                keys_output = "找到的密钥及耗时:\n"
                for key, time2 in zip(keys_found, time_found):
                    time222=time2*1000
                    keys_output += f"密钥: {key}，破解时间: {time222:.3f} 毫秒\n"

            else:
                keys_output = "没有找到匹配的密钥。"

            keys_output += f"\n\n暴力破解总耗时: {elapsed_time:.3f} 毫秒"  # 保留3位小数并输出毫秒

            # 使用 messagebox 显示结果
            messagebox.showinfo("求解密钥", keys_output)
            self.result_text.delete(1.0, tk.END)  # 清空文本框
            self.result_text.insert(tk.END, keys_output)  # 显示加密结果
        else:
            messagebox.showwarning("error", "密文或者明文不能为空")
```

#### 		②实际操作界面：

<img src="photos\image-20241004200634466.png" alt="image-20241004200634466" style="zoom:50%;" />

​			假设输入明文为10011011，密文为10101010，一共找到了两把可能的密钥，并记录了分别耗时与总耗时。

### （五）封装测试

#### 		①代码实现:

```python
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
                messagebox.showinfo("求解成功", keys_output)
                self.result_text.delete(1.0, tk.END)  # 清空文本框
                self.result_text.insert(tk.END, keys_output)  # 显示加密结果
            else:
                messagebox.showwarning("ERROR", "不存在不同密钥产生相同密文的情况")
```

#### 		②实际操作界面：

<img src="photos\image-20241004201349576.png" alt="image-20241004201349576" style="zoom:50%;" />

## 四·总结

​	本次实现S-DES算法的困难主要集中在几个方面：

​		密钥生成过程涉及复杂的置换和循环左移

​		S盒替换的逻辑需要精确处理行和列，且调试时难以定位问题

​		位操作和数据类型处理也可能导致实现上的混淆

​	为了提升实现的质量，采取的措施有：

​		将算法模块化，便于维护和理解

​		在输入阶段进行有效性验证，减少错误输入

​		编写单元测试确保各模块的正确性

## 五·鸣谢

·课程名称：信息安全导论
·教学班级：992987-002
·任课教师：向宏
·单位：重庆大学大数据与软件学院
·小组：猫的摇篮
·成员：刘子昂、冉紫阳、刘鲲遥
·若有任何疑问或建议，请联系开发团队：1318147137@qq.com
