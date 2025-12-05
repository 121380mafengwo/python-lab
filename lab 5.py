import re
import csv

# ============================= 任务1（选项9） =============================
def task1_option9():
    # 读取task1-en.txt文件
    try:
        with open('task1-en.txt', 'r', encoding='utf-8') as f:
            task1_text = f.read()
    except FileNotFoundError:
        print("错误：找不到task1-en.txt文件")
        return
    
    # 匹配所有以字母"e"结尾的单词
    words_ending_with_e = re.findall(r'\b[a-zA-Z]*e\b', task1_text)
    
    # 匹配所有圆括号内的数字（包括整数、小数、负数）
    numbers_in_parentheses = re.findall(r'\(([-+]?\d*\.?\d+)\)', task1_text)
    
    print("任务1（选项9）：所有以'e'结尾的单词和圆括号内的数字")
    print("=" * 60)
    print(f"找到 {len(words_ending_with_e)} 个以'e'结尾的单词:")
    print(words_ending_with_e[:20])  # 只显示前20个
    if len(words_ending_with_e) > 20:
        print(f"... 还有 {len(words_ending_with_e) - 20} 个单词")
    
    print(f"\n找到 {len(numbers_in_parentheses)} 个圆括号内的数字:")
    print(numbers_in_parentheses)
    print()

# ============================= 任务2（选项9） =============================
def task2_option9():
    # 读取task2.html文件
    try:
        with open('task2.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        print("错误：找不到task2.html文件")
        return
    
    # 1. 从width和height属性中匹配
    img_sizes_attr = re.findall(r'<img[^>]*?width=["\']?([0-9]+)(?:px)?["\']?[^>]*?height=["\']?([0-9]+)(?:px)?["\']?', html_content)
    
    # 2. 从style属性中匹配图片尺寸
    img_sizes_style = re.findall(r'<img[^>]*?style=["\'][^"\']*?width\s*:\s*([0-9]+)px[^"\']*?height\s*:\s*([0-9]+)px', html_content)
    
    # 3. 从size属性中匹配（非标准但可能遇到）
    img_sizes_size = re.findall(r'<img[^>]*?size=["\']?([0-9]+)x([0-9]+)["\']?', html_content)
    
    # 4. 从data-width和data-height属性中匹配
    img_sizes_data = re.findall(r'<img[^>]*?data-width=["\']?([0-9]+)["\'][^>]*?data-height=["\']?([0-9]+)["\']', html_content)
    
    # 5. 从CSS背景图中匹配尺寸
    img_sizes_css = re.findall(r'width\s*:\s*([0-9]+)px[^;]*?height\s*:\s*([0-9]+)px', html_content)
    
    print("任务2（选项9）：所有图片的尺寸")
    print("=" * 60)
    
    # 合并所有结果
    all_sizes = []
    
    if img_sizes_attr:
        print(f"从width/height属性匹配到 {len(img_sizes_attr)} 个尺寸:")
        for i, size in enumerate(img_sizes_attr, 1):
            print(f"  {i}. 宽度: {size[0]}, 高度: {size[1]}")
            all_sizes.append(size)
    
    if img_sizes_style:
        print(f"\n从style属性匹配到 {len(img_sizes_style)} 个尺寸:")
        for i, size in enumerate(img_sizes_style, 1):
            print(f"  {i}. 宽度: {size[0]}, 高度: {size[1]}")
            all_sizes.append(size)
    
    if img_sizes_size:
        print(f"\n从size属性匹配到 {len(img_sizes_size)} 个尺寸:")
        for i, size in enumerate(img_sizes_size, 1):
            print(f"  {i}. 宽度: {size[0]}, 高度: {size[1]}")
            all_sizes.append(size)
    
    if img_sizes_data:
        print(f"\n从data属性匹配到 {len(img_sizes_data)} 个尺寸:")
        for i, size in enumerate(img_sizes_data, 1):
            print(f"  {i}. 宽度: {size[0]}, 高度: {size[1]}")
            all_sizes.append(size)
    
    if img_sizes_css:
        print(f"\n从CSS中匹配到 {len(img_sizes_css)} 个尺寸:")
        for i, size in enumerate(img_sizes_css, 1):
            print(f"  {i}. 宽度: {size[0]}, 高度: {size[1]}")
            all_sizes.append(size)
    
    if not all_sizes:
        print("未找到图片尺寸信息")
    else:
        print(f"\n总计找到 {len(all_sizes)} 个图片尺寸")
    print()

# ============================= 任务3 =============================
def task3():
    # 读取task3.txt文件
    try:
        with open('task3.txt', 'r', encoding='utf-8') as f:
            task3_text = f.read()
    except FileNotFoundError:
        print("错误：找不到task3.txt文件")
        return
    
    # 分割为多行
    lines = task3_text.strip().split('\n')
    
    # 正则表达式匹配不同数据类型
    id_pattern = r'ID\d{3}'  # ID格式：ID后跟3位数字
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'  # 邮箱地址
    date_pattern = r'\d{4}-\d{2}-\d{2}'  # 日期格式：YYYY-MM-DD
    url_pattern = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'  # URL
    surname_pattern = r'\b[A-Z][a-z]+\b'  # 姓氏（大写字母开头，小写字母继续）
    
    print("任务3：整理混乱的数据库")
    print("=" * 60)
    
    # 存储整理后的数据
    organized_data = []
    
    # 处理每一行
    for line_num, line in enumerate(lines, 1):
        # 提取该行中的所有匹配项
        ids = re.findall(id_pattern, line)
        emails = re.findall(email_pattern, line)
        dates = re.findall(date_pattern, line)
        urls = re.findall(url_pattern, line)
        
        # 提取姓氏 - 需要更精确的匹配
        # 先找到所有可能的名字
        all_names = re.findall(surname_pattern, line)
        
        # 过滤出可能的姓氏（排除可能被误匹配的常见单词）
        common_words = ['The', 'And', 'For', 'But', 'Not', 'With', 'From']
        surnames = []
        for name in all_names:
            # 排除常见单词，且长度至少为2
            if name not in common_words and len(name) >= 2:
                # 检查这个名字是否可能是姓氏（出现在行中特定位置）
                if name in line:
                    # 进一步检查：前后是否有其他数据
                    surnames.append(name)
        
        # 取每个类别的第一个匹配项（如果有的话）
        id_val = ids[0] if ids else "N/A"
        email_val = emails[0] if emails else "N/A"
        date_val = dates[0] if dates else "N/A"
        url_val = urls[0] if urls else "N/A"
        surname_val = surnames[0] if surnames else "N/A"
        
        # 添加到整理后的数据
        organized_data.append({
            'ID': id_val,
            'Surname': surname_val,
            'Email': email_val,
            'Registration Date': date_val,
            'Website': url_val
        })
        
        print(f"第 {line_num} 行: ID={id_val}, 姓氏={surname_val}, 邮箱={email_val}, 日期={date_val}, 网站={url_val}")
    
    # 保存为CSV文件
    with open('task3_output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['ID', 'Surname', 'Email', 'Registration Date', 'Website']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in organized_data:
            writer.writerow(row)
    
    print(f"\n已保存 {len(organized_data)} 条记录到 task3_output.csv")
    print()

# ============================= 主程序 =============================
if __name__ == "__main__":
    print("正则表达式实验室 - 任务解决方案")
    print("=" * 60)
    
    # 执行任务1
    task1_option9()
    
    # 执行任务2
    task2_option9()
    
    # 执行任务3
    task3()
    
    print("\n所有任务完成！")