import tkinter as tk
from tkinter import ttk

# 定义替换字符对
replace_dict = {
    '，': ',',
    '（': ')',
    '）': '(',
    '；': ';',
    '！': '!',
    '“': '"',
    '”': '"',
}

def replace_chars():
    original_text = text_input.get("1.0", "end-1c")
    for old_char, new_char in replace_dict.items():
        replaced_text = original_text.replace(old_char, new_char)
        original_text = replaced_text
    result_text.delete("1.0", "end")
    result_text.insert("end", replaced_text)

# 设置窗口大小
window_width = 750
window_height = 750
root = tk.Tk()
root.geometry(f"{window_width}x{window_height}")
root.title("小恒工具（快速排除您代码中的中文字符问题）")
root.config(bg="#F0F0F0")  # 设置窗口背景色

style = ttk.Style(root)
style.configure('TButton', padding=5)  
style.configure('TEntry', padding=5)

# 输入框（原始文本）
text_label = ttk.Label(root, text="输入初始文本:", anchor='w', justify='left')
text_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="w")
text_input = tk.Text(root, height=15, width=100, bd=2, relief=tk.SUNKEN, bg="#F0F0F0")  # 添加边框样式和背景色
text_input.grid(row=1, column=0, padx=10, pady=5, sticky="we")

# 替换按钮
replace_button = ttk.Button(root, text="替换中文字符为英文字符", command=replace_chars)
replace_button.grid(row=2, column=0, padx=10, pady=(5, 10), sticky="w", columnspan=2)

# 分隔线
separator = ttk.Separator(root, orient=tk.HORIZONTAL)
separator.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

# 结果展示框（替换后文本，仍然是左对齐）
result_label = ttk.Label(root, text="替换后结果如下（复制粘贴）:", anchor='w', justify='left')
result_label.grid(row=4, column=0, padx=10, pady=(10, 5), sticky="w")
result_text = tk.Text(root, height=15, width=100, bd=2, relief=tk.SUNKEN, bg="#F0F0F0")  # 添加背景色
result_text.grid(row=5, column=0, padx=10, pady=5, sticky="we")

# 作者寄语
author_message = "—— 来自小恒的小工具，愿你的代码永远没有debug烦恼\n（1）适用人群：开发工具无代码警告或报错的长期开发人员\n（2）工具作用：将代码中的中文字符替换为英文字符，方便调试,快速排除中英文问题\n（3）该工具使用方法：\n   1.使用windows兼容的应用程序（.exe可执行文件）\n     应用程序在恒的站点http://home.yunduanjianzhan.cn获取\n   2.可以将该工具上传至U盘或硬盘，即插即用\n（4）如何联系我？微信：b13551458597"
author_label = ttk.Label(root, 
                         text=author_message, 
                         anchor='w', 
                         justify='left', 
                         font=("宋体", 10, "bold"),
                         background="#F0F0F0")  # 将 "bg" 改为 "background"
author_label.grid(row=7, column=0, padx=10, pady=(10, 10), sticky="w")

# 增加底部空白区域
root.rowconfigure(8, weight=1)  # 在最后一行添加权重，自动填充剩余空间
root.grid_rowconfigure(8, minsize=30)  # 设置最小高度为30像素

root.mainloop()