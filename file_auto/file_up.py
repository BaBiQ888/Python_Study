import requests

# 定义API端点和文件路径
url = 'https://example.com/upload'
file_path = 'path/to/your/file.txt'

# 创建文件对象
files = {'file': open(file_path, 'rb')}

# 发送POST请求
response = requests.post(url, files=files)

# 打印响应
print(response.text)
