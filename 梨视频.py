# 1拿到contid
# 2拿到videostatus返回的json  srcurl
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62",
    "Referer": "https://www.pearvideo.com/video_1748413"}  # 处理防盗链
url = "https://www.pearvideo.com/video_1748413"
contid = url.split("_")[1]
videostatus = f"https://www.pearvideo.com/videoStatus.jsp?contId={contid}&mrd=0.2801154989147743"
response = requests.get(url=videostatus, headers=headers)
# print(response.text)
dic = response.json()
srcUrl = dic["videoInfo"]["videos"]["srcUrl"]
systemTime = dic["systemTime"]
srcUrl = srcUrl.replace(systemTime, f"cont-{contid}")
# print(srcUrl)
# https://video.pearvideo.com/mp4/third/20211222/cont-1748413-15195380-222300-hd.mp4        #正确的
# https://video.pearvideo.com/mp4/third/20211222/1640609267131-15195380-222300-hd.mp4       #错误的
# 下载视频
with open('a.mp4', mode='wb') as file:
    print('正在下载---')
    file.write(requests.get(url=srcUrl).content)
    print('下载完成')
