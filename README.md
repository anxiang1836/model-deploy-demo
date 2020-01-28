# 基于Flask简单实现模型部署

> - 模型也并没有部署太过复杂的模型：FastText的训练的一个简单文本分类器；
> - 由于并不是前端开发出身，也没有深研究Vue之类的做华丽的前端。
>
> 仅作为Demo吧，依托于heroku，部署在了互联网上，链接为：https://fasttest-shown.herokuapp.com/

受教于Guilame Genthial的一篇名为：[《Serving a simple python API with Flask》](https://guillaumegenthial.github.io/serving.html)的帖子，

抄起家伙操作了一番（曾经操练过的前端是忘得一干二净了，白扯了，哎~）

## 简单原理

![](https://raw.githubusercontent.com/anxiang1836/FigureBed/master/img/20200128225043.png)

- [Flask](http://flask.pocoo.org/) ：来建立用于操作后端 **API** (back-end)
- [jquery.ajax](http://api.jquery.com/jquery.ajax/) ：前台监听处理requests，然后交互给后端的API。

余下的内容还是直接参看原贴吧，不在这里赘述了！

## [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)

本着要做就做完整了的想法，所以就选择了一个可以部署轻量级的应用的平台，所以我就选择了[Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)（当然也是帖子中推荐的，确实很棒）

![](https://raw.githubusercontent.com/anxiang1836/FigureBed/master/img/20200128225916.png)

## 最终效果

本来也是以Demo形式呈现的，所以，简单看看就好。

FastText我只简单的训练了对如下几个方向的分类识别：

- 科技（technology）
- 军事（military）
- 体育（sport）
- 娱乐（entertainment）
- 汽车（car）

后面有时间学习一波前端的知识，换一些模型再来好好来重新优化~。

## PS：期待

在交流群中见过做类似应用展示做的很好的典范，附上链接，时常记得激励自己，做就要向这个方向做，才像那么回事呀！~~

https://www.zq-ai.com/?from=groupmessage&isappinstalled=0#/nlp/medicalner

![](https://raw.githubusercontent.com/anxiang1836/FigureBed/master/img/20200128231230.png)
