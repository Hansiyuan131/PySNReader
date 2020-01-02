# SN-Reader

> Smart News Reader     
> 一款让你爱不释手的新闻阅读器  
> 本项目为毕业设计项目，不用于任何商业用途

## 项目结构

``` 
├─.idea
│  └─markdown-navigator
├─service 个性化推荐服务
└─spider 爬虫项目
```

### Spider

> 采用Gerapy+Scrapyd搭建个性化爬虫管理平台    
> 采用Scrapy进行数据爬取


### Service

> 使用Surprise框架实现推荐算法


## 参考文档

### Python相关

- [Python官网](https://docs.python.org/zh-cn/3/tutorial/index.html)
- [廖雪峰的Pyhton教程](https://www.liaoxuefeng.com/wiki/1016959663602400)
- [Django官网](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial01/)

### 爬虫相关

- [Scrapy官网](https://scrapy-chs.readthedocs.io/zh_CN/1.0/)
- [Requests官网](https://2.python-requests.org//zh_CN/latest/)
- [python3网络爬虫开发实战](https://app.gitbook.com/@germey/s/private/python3webspider/)
- [Scrapyd官网](https://scrapyd.readthedocs.io/en/stable/)
- [Gerapy-Github](https://github.com/Gerapy/Gerapy)



### 个性化推荐算法相关

- [模型仓库](https://modeldepot.io/browse)
    - 网站内容主要分为三块，即图像、文本以及文本生成；包括目标检测、图像分类、语音处理、文本分析和语义分割等多个深度学习方向。
- [Surprise](https://github.com/NicolasHug/Surprise)
    - Surprise是一个Python scikit，用于构建和分析处理显式评级数据的推荐系统