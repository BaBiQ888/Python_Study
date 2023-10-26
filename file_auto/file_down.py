import requests

# 定义文件下载链接
url = 'https://example.com/download/file.txt'

# 发送GET请求
response = requests.get(url)

# 检查响应状态码
if response.status_code == 200:
    # 获取文件名
    filename = url.split('/')[-1]
    # 保存文件到本地
    with open(filename, 'wb') as f:
        f.write(response.content)
else:
    print('文件下载失败')
