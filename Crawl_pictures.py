# -*- coding:utf-8 -*-

# 爬取糗百热图（https://www.qiushibaike.com/imgrank/）
# 输入页码，抓取指定页面上的图片并保存到本地文件夹；
# 采用多线程技术进行爬取，减少等待时间；
# 可选要求：将程序打包为 exe 文件；

import requests,re,threading,os


def get_pic_url(i,headers):
    url='https://www.qiushibaike.com/imgrank/page/%d/'% i
    req=requests.get(url,headers)
    data=req.text
    pic_url_list=re.findall(r'//pic.qiushibaike.com/system/pictures\S*\.jpg',data)
    return pic_url_list


def download_pic(pic_url,headers):
    get_pic=requests.get('http:'+pic_url,headers)
    pic_name=r'pic_file\%s'% str(pic_url.split('/')[-1])
    try:
        with open(pic_name,'wb')as f:
            f.write(get_pic.content)
            print('%s下载完成'%str(pic_url.split('/')[-1]))
    except:
        print('%s下载失败'%str(pic_url.split('/')[-1]))

def main():
    headers = {'User-Agent': 'Chrome'}

    isExist = os.path.exists('pic_file')
    if not isExist:
        os.makedirs('pic_file')

    begin_page = int(input('请输入起始页: '))
    end_page = int(input('请输入终止页：'))

    if end_page >= begin_page:

        print('开始下载')

        pic_url_list_set = []

        for i in range(begin_page, end_page + 1):
            pic_url_list = get_pic_url(i,headers)
            pic_url_list_set += pic_url_list

        dl_threads = []

        for i in range(len(pic_url_list_set)):
            threads = threading.Thread(target=download_pic, args=(pic_url_list_set[i],headers ))
            dl_threads.append(threads)

        for i in range(len(pic_url_list_set)):
            dl_threads[i].start()

        for i in range(len(pic_url_list_set)):
            dl_threads[i].join()

        print('结束下载')

    else:
        print('输入有误，程序终止')

if __name__=='__main__':
    main()


