# 统计参数中每个英文单词出现的次数
def stats_text_en(text):
    elements=text.split()
    words=[]
    symbols=',.*-!'
    for element in elements:
        for symbol in symbols:
            element=element.replace(symbol,'')
        if len(element):
            words.append(element)
    counter={}
    word_set=set(words)

    for word in word_set:
        counter[word]=words.count(word)
    #函数返回值用return进行返回,如果没有return 返回值则为None
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)

# 统计参数中每个中文汉字出现的次数
def stats_text_cn(text):
    cn_characters=[]
    for character in text:
        #unicode 中 中文字符的范围
        if'\u4e00'<= character<='\u9fff':
            cn_characters.append(character)
    counter={}
    cn_character_set=set(cn_characters)
    for character in cn_character_set:
        counter[character]=cn_characters.count(character)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)

en_text='''
The Zen of Python, by Tim Peters
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambxiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    '''

cn_text='''
花钱VS学知识
周三出差到广州，在飞机上翻看海航的航机杂志，看到一篇写知识付费的文章，作者总结了自己的知识付费的历史，尤其是买了很多得到老师的专栏，仔细的写出了自己的收获和尴尬，值与不值存乎一心，文章给了我一个启发，我也可以写一下自己在得到平台的花的钱和获得的知识，算算投资回报率怎样。

不算不知道，算算吓一跳。从第一次在得到付费购买《李翔商业内参》开始，到上周刚刚买的《张潇雨.经典案例课》，我总计买了14个专栏，每个RMB199，这算大的专栏吧，花费RMB2800；小的课程竟然买了20个，价格不贵RMB19.9/个，唯一梁宁的《产品思维三十讲》是RMB99，小课总计花费RMB500，单单是在得到上我就买了RMB3300元的付费课程。

我想从几个角度来谈谈收获的事情，第一是我会分析有收获的专栏，有的很多，有的几乎没有，有好几个我都没有听完，就谈不上收获了；第二点是这些专栏的起名字的学问；第三个就是给出我自己的最佳课程推荐，以及为什么推荐这些课程。

专栏的收获
收获最大的是李笑来的专栏《通往财富自由之路》，自己曾经有一段时间每天都留言，感觉有种打通任督二脉，人生准备开挂的体验。虽然学习专栏没有能够让我到达财富自由的目标，但是也让我知道了去财富自由目标那里的方法，整个学习的过程充满欢乐，有些核心的概念确实颠覆了自己的认知，让自己看到了之前以为不存在的风景。像是元认知能力的获得和培养；注意力是你最重要的资源；多维竞争力；投资的方法论；活在未来而不是活在当下；很多的知识，学习之后还需要在实践中践行才真正可以学会。
还有很重要的收获是通过这个专栏加入了007的写作社群，前两天在《把时间当作朋友》里面找一个案例，无意中读到了，笑来老师说的，培养一个不太费钱的业余爱好，绝对是获得幸福生活的好方法。这本书读了四五遍，但是这段话好像第一次看到。现在每周在微信公众号写一篇文章，用这件事锚定了自己的生活，也是蛮开心的一件事。而且写作不但是省钱还锻炼了大脑思考能力和逻辑思维能力，顺便还认识了很多上进的好战友，拓展了自己的社交圈和生活圈。
仔细回顾了所有的专栏，只有这个专栏自己几乎是每一篇文章都写了留言，因为要写东西必须要思考，投入了时间和精力，当时是有点辛苦的，但是现在回想起来，正是因为这样的辛苦才了有这些收获，而其他只是看一看，没有留言的专栏，现在几乎都忘记了。不是老师的专栏内容不精彩，而是自己投入不够多，花时间太少，单单是花钱并不代表你会有收获，于我而言，这还真是花钱学到的经验之谈。
如果单纯从专栏的内容上来说，我最喜欢和菜头的专栏《槽边往事》，嬉笑怒骂之间，让一个胖子替自己说出了心中的话，点评了自己想看的电影，骂了骗人的奸商，学会了很多让生活更幸福的方法。我相信一个喜欢看书的人都会喜欢和菜头的文章，有时让你笑，有时让你沉思，有时让你花钱，有时让你感动。虽然他的专栏我很少写留言，但是我会按照他的文章说的方法去做，比如去买机械键盘，确实提升了打字的幸福感；比如去尝试不同口味的啤酒，试了才知道啤酒还有这些不同的口感；再比如去看他推荐的电影，《一个叫欧维的男人准备去死》，《四个春天》《海边的曼彻斯特》多了些观影乐趣。
其它大的专栏都很好，可是因为自己的原因，我现在都不太记得讲的是什么了，倒是有几个小专栏，给我带来了惊喜，有的甚至深深的改变了我的工作生活习惯。
首推《怎样学会正念冥想》，我基本可以保持每天都做冥想10-30分钟，跟着童慧琦老师的音频更容易静下心来。很多的牛人都冥想的粉丝，像是桥水基金的瑞达里奥，台湾股王，大立光的少帅也是每天必须冥想一个小时，似乎笑来老师也是要每天冥想一个小时的，冥想的好处太多，说也说不完，谁做谁知道。据说国外的科学家已经通过严谨的实验证明，冥想可以让大脑的灰质沟回变深，也就是可以让大脑的灰质层变大，人会变得更聪明。
其次是戴愫老师的《有效提升与陌生人的社交能力》，虽然只有19.9，但是我从中学到很多，自己之前也转么写过一篇文章，讲述自己使用专栏里讲到的方法收到的良好的反馈。怎样才算是真正的倾听；如何打破僵局，开场，怎样和陌生人聊天。有时候参加一些活动自己还会刻意练习使用这些方法，都有不错的效果。
张展晖的《有效管理你的健康》，自己算是很喜欢运动的人了，但是还是有很多错误的体育锻炼的知识，跟着张老师学习了正确的有氧锻炼方法，通过控制饮食减肥的方法。现在我还会时不时的拿出来听一听，逐渐的改变自己错误的锻炼方法，使用正确的方法控制自己的饮食，增强身体的心肺功能，提高柔韧性，提高肌肉的力量。三分练，七分吃，减肥的秘密管住嘴更重要，减肥锻炼最好的方法不是跑步，而是在自己的适合心率范围内在跑步机上上坡走。
王雨豪的《怎样成为演讲高手》，让我在公司的会议致辞时表达出了自己的心声，找到了适合自己的演讲的风格。里面有很多很具体的方法论，像是先用口语说的方式把演讲稿录下来，用讯飞语记应用把内容转成文字，再慢慢修改，试了一次之后，就发现用口语的方式来讲确实更容易一些，因为是自己的语言，在演讲时就是真正的在讲，而不是表演，因为真实的，真诚表达是做一个好演讲的核心法门。用录像的方式把自己做演讲的表现录制下来自己检查，会发现很多小毛病或者大缺点，根据录像去调整自己演讲的仪态，声调，很有效果。
总结下来就是，买一个专栏，最重要不是花多少钱，而是花费了多少时间和精力去学习，去练习，而且需要经常练习，要温故而知新。太阳下面没有新鲜事，这些方法都是孔夫子再三千年前讲的，我们上小学的时候老师就交给我们了，随着学的高级知识越来越多，这些初级的知识我们都忘记了，但是大的道理往往是简单的，反复的刻意练习，直到自己练出肌肉记忆，做动作时不需要调动大脑去思考。凡是自己花了时间去练习，多次的重复收听音频，阅读文字版，留言，在实践中践行，自己脑海中存留的内容比较多，收益也比较大。
专栏名字的奥秘
小的专栏的取名技巧很容易看的出来，只要把所有的专栏名字写下来就可以知道了。基本上采用解决痛点的起名方式，直接击中用户的要害，要么满足用户的一个担心，要么提升用户的一个能力，使用的界面非常友好。

怎样成为演讲高手
如何提升男士职场形象
有效提升与陌生人的社交能力
大的专栏名字也分几种

内容派—李笑来《通往财富自由之路》《关系攻略》
人物品牌—《香帅的北大金融学课》《薛兆丰的经济学课》《吴军的谷歌方法论》
推荐的专栏
其实可以在得到上开专栏的老师，水平都是非常高的，每个人的知识都值得我们学习，肯定也都会有收获。现在买这些课程，钱其实不是最大的问题，最大的问题反而是时间和精力，愿不愿意花功夫自己的阅读，收听，实践专栏中讲的内容，如果有这样的心理准备的话，完全按照自己的兴趣去选就好。

不过我还是想推荐几个专栏，个人学习，实践之后觉得真的很好的专栏和作者，让大家有一个参考，一千个人有一千个哈姆雷特，我只是给出我的个人建议，供大家参考，如果有不同的意见，大家可以一起探讨，有碰撞和交流才有火花和创意产生。

首先推荐李笑来的《通往财富自由之路》，这不是一个教你致富的专栏，这是一个彻底改变你的认知的思维升级程序，安装了之后可以让你的系统能力得到根本提升和发展；童慧琦老师的《怎样学会正念冥想》只需19.9把一个冥想老师请回家，随时随地教你，陪你一起冥想，想想就开心；张展晖《有效管理你的健康》身体是革命的本钱，有了好的身体，才有资本干革命，张老师很多正确的健身知识让我少走了弯路；刚刚读了张潇雨的《经典商业案例课》，干货满满，强力推荐，很多的洞察确实需要一个懂的人去帮我们分析，分享我们才可以看出其中的端倪。

从在得到平台上的花费和收获来看，我认为还是很值得，总计花费3300元，其实只是半部苹果手机的价格，但是自己从得到上专栏学习过程中收获的东西，价值远远大于3300元钱。因为认识了很多做投资的朋友，让我进入了区块链的市场，亲身参与这个时代最有争议的行业其中，那种刺激和收获，花少也钱买不来；因为学习了资本的正确概念，使得我只会用自己可以判无期徒刑的钱去投资，标的价格的波动起伏对我根本没有丝毫影响，那个幸福感，让人陶醉。另外，复盘之后我才发现自己专栏的利用率太低了，因为时间上投入的太少，当然不可能有大的收获，现在要做的是把所有自己订阅的专栏自己的读三到五遍，每一篇都写留言，在工作和生活中认真的去用它们，让专栏的知识真正变成自己的本领，这才不枉费自己的时间和金钱的投入，才能把投资回报率提高。
'''
 
# 搜索_name_==_main_
# 一般情况下在文件内测试代码的时候用以下的方式
if __name__=='_main_':
    en_result=stats_text_en(en_text)
    cn_result=stats_text_cn(cn_text)
    print('统计参数中每个英文单词出现的次数==>\n',en_result)
    print('统计参数中每个中文汉字出现的次数==>\n',cn_result)
    
    