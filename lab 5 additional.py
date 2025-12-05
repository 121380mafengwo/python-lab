import re
import csv


def additional_task_option9():
    # 读取task_add.txt文件
    try:
        with open('task_add.txt', 'r', encoding='utf-8') as f:
            task_add_text = f.read()
    except FileNotFoundError:
        print("错误：找不到task_add.txt文件")
        return
    
    print("附加任务（选项9）：查找隐藏数据")
    print("=" * 60)
    
    # 匹配日期（支持不同分隔符：- / . 和不同格式）
    date_patterns = [
        r' \d{4}[-/.]\d{2}[-/.]\d{2}',  # YYYY-MM-DD, YYYY/MM/DD, YYYY.MM.DD
        r' \d{2}[-/.]\d{2}[-/.]\d{4}',  # DD-MM-YYYY, DD/MM/YYYY, DD.MM.YYYY
        r' \d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}'  # 更灵活的格式
    ]
    
    all_dates = []
    for pattern in date_patterns:
        matches = re.findall(pattern, task_add_text)
        all_dates.extend(matches)
    
    # 去除重复和清理空格
    dates = list(set([date.strip() for date in all_dates]))
    dates.sort()
    
    # 匹配邮箱地址
    email_pattern = r' [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, task_add_text)
    emails = [email.strip() for email in emails]
    emails = list(set(emails))
    
    # 匹配网站URL（包括http/https/www开头的）
    url_pattern = r' (?:https?://|www\.)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}[^\s]*'
    urls = re.findall(url_pattern, task_add_text)
    urls = [url.strip() for url in urls]
    urls = list(set(urls))
    
    # 确保每个类型只取前5个（根据任务要求）
    dates = dates[:5] if len(dates) >= 5 else dates
    emails = emails[:5] if len(emails) >= 5 else emails
    urls = urls[:5] if len(urls) >= 5 else urls
    
    print("找到的日期:")
    for i, date in enumerate(dates, 1):
        print(f"  {i}. {date}")
    
    print("\n找到的邮箱:")
    for i, email in enumerate(emails, 1):
        print(f"  {i}. {email}")
    
    print("\n找到的网站:")
    for i, url in enumerate(urls, 1):
        print(f"  {i}. {url}")
    
    print(f"\n总计: {len(dates)} 个日期, {len(emails)} 个邮箱, {len(urls)} 个网站")


if __name__ == "__main__":
    print("正则表达式实验室 - 任务解决方案")
    print("=" * 60)
    
    # 执行附加任务
    additional_task_option9()
    
    print("\n所有任务完成！")