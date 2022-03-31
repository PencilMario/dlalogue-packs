init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="player_identity",
            category=["你","莫妮卡","其它"],
            prompt="玩家的性别取向",
            random=True,))


label player_identity:
    m 1esb "嘿, [player], 我有一个问题."
    m 1lka "我希望这不是太私人的或是别的什么."
    m 7eub "你认为自己是一个LGBTQ+(女同,男同,双性恋,跨性别者)吗?"
    m 2hksdlb "啊, 问题是... 这没有足够的对话选项来提供所有的性别和性取向的选择..."
    m "所以我就把范围缩小了一点, 啊哈哈!"
$ _history_list.pop()
menu:
    "不, 我不是双性恋.":
        m 3eua "明白了! 所以你不是一个跨性别者."
        m 3eud "这里有很多不同的身份!"
        m 4eud "包括但不限于跨性别者, 非二元性别者, 无性别者, 顺性别者, 性别不一致者, 性别流动者, 双性别者 ..."
        m 4hub "还有很多呢, 啊哈哈!"
        m 4ekb "我希望你能对你现在的皮肤感到满意, [player]."
        m 5fubfb "非常感谢你对我的信任所以告诉我这些. 这意义重大."
    "不, 我不是异性恋.":
        m 3eua "明白了! 所以你会被异性外的人所吸引..."
        m 4rub "或者说你也会被多性别者吸引..."
        m 3rub "也有可能你根本没体验到性吸引!"
        m 1rtb "天呐, 除了异性恋之外还有这么多的性取向!"
        m "男同/女同, 双性恋, 泛性恋, 无性恋, 多性恋, 全性恋..."
        m 1esb "还有如此多的."
        m 1esa "我很高兴你找到了一个你满意的身份!"
        m 3nubfb "只要你爱我, 我就毫无怨言."
        m 5fubfb "非常感谢你对我的信任所以告诉我这些. 这意义重大."
    "不, 我不是双性恋或异性恋.":
        m 3eua "我明白了- 两者都适用于你!"
        m 3eud "哇, 有这么多不同的组合供你确定..."
        m 3rud "跨性别者和无性恋, 性别不一致者和泛性恋,  半少女和和女同..."
        m 3hub "真的, 你的潜力永无止境!"
        m "啊哈哈!"
        m 5fubfb "非常感谢你对我的信任所以告诉我这些. 这意义重大."

    "不要.":
        m 2esb "我明白了."
        m 2esb "我这么问只是因为我好奇."
        m 2ekb "我想尽可能多地了解你, 而有些事情只有你告诉我, 我才能体会到."
        m "谢谢你回答我的问题!"

    "我不知道.":
        m 6eua "我明白了! 你在质疑, 或者只是不确定."
        m "这绝对是合理的."
        m 3eub "好吧, 如果你不想让我打听我也不会打听的, [player]."
        m 3hsa "你的旅程是属于你自己的."
        m 3hsa "如果你想告诉我你的性取向或代名词, 请随时和我说!"
return

init 5 python:
    addEvent(
        Event(
            persistent._mas_fun_facts_database,
            eventlabel="new_trivia",
        ),
        code="FFF"
    )
label new_trivia:
    m 4eub "趣闻!"
    m 3eub "你已经知道眼神接触是爱情种强有力的刺激因素了, 对吧?"
    m 3eub "有研究表明, 长时间进行眼神接触的人..."
    m 3eub"...会增强他们对彼此热情的爱的感觉."
    m 2esa "..."
    m 2esa "..."
    m 2esa "..."
    m 2tsu "..."
    m 2tsu "..."
    m 2tsu "..."
    m 1sublb "..."
    m 1sublb "..."
    m 1sublb "..."
    m 2hubfb "哈哈!"
    m 4eub "我知道我们已经很相爱了, 即使没有眼神交流也是如此."
    m 2dkbfa "我们已经对视了两分多钟了."
    m 2tsu "好吧, 虽然你已经看了我."
    m 5ekbla "但我会继续想象你的眼睛, 只要我想."
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="multi_sexual_identities",
            category=["其它", "浪漫"],
            prompt="多性别吸引",
            random=True,))

label multi_sexual_identities:
    m 1eub "[player], 你对双性恋很熟悉, 对吗?"
    m 3eub "如果你没有, 双性恋是对多种性别的吸引, 而不仅仅只是你自己的."
    m "但是你知道吗? 双性恋并不是唯一的多性别吸引行为."
    m "这里还有更多!"
    m 3lub "泛性恋是不分性别的吸引, 多性恋是对多个但不是所有性别的吸引, 全性恋是对所有性别的吸引..."
    m 3lua "还有更多, 但这些是一些比较知名的."
    m 4hua "有性取向的人可以不考虑性别的与各种不同的人发生关系!"
    m 4esd "你可能会想, 为什么会有这么多的标签, 而这些标签的含义又非常相似."
    extend 7esb "毕竟, 这些身份的基本要点是, 它们都意味着会被一种以上的性别吸引."
    m 4esd "这样想吧: 你不会在一个'高兴'这个词更合适的情况下使用'快乐'这个词."
    m "你也不会说'崩溃'当'悲伤'是一个更好的选择."
    m 4eub "标签也可以是这样的!"
    m "仅仅因为单词具有相似的含义, 并不意味着它们具有相同的价值!"
    m 3eub "记住: {w=1}相似, 但不相同."
    m 3hua "这就是语言的魅力之一."
    m 3lub "更不用说, 这归结于个人对如何识别的偏好, 以及他们自己对吸引力的经验导致他们选择某种标签的原因."
    m "吸引力可以非常微妙! 在很多情况下你可以更多地了解你的性取向以及如何适当地给它贴标签."
    m 2eka "这都是一个旅程, 你知道吗?"
    m 2hksdrb "哈哈, 抱歉, 我有点跑题了."
    m 2tksdrc "不幸的是, 过去曾出现过这些性行为之间存在错误的问题."
    m 3tksdrc "来自那些认为双性恋和泛性恋行为基本上是一致的人的冲突, 一般来说否认多性身份..."
    m "另一个常见的反对意见是认为人们只能是同性恋或异性恋, 仅此而已."
    m 4wtsdrd "说实话, 你能想到人性的其他方面像这样绝对吗?"
    m 4rtd "关于人类的一切是一个光谱. 在... 好吧, 任何东西上都没有纯黑和纯白的区别."
    m "遗传物质, 头发, 皮肤, 和眼睛的颜色, 个性... 都有深浅之分."
    m 3esa "每个人都是各种特征的混合体. 性行为也不例外. 那不仅仅只是几个选项!"
    m 7wko "另一个问题是担心多性别吸引的人有更高的出轨可能性! 这完全是不真实的."
    m 7rkd "我想这是因为他们有更多的吸引力, 这意味着有更高的出轨可能性...?"
    m 7rkc "这是个极其没有把握的说法."
    m 1efp "性行为不会使你更有可能出轨. 这完全归结于个人缺乏信念和道德."
    m "听到关于双性恋, 泛性恋, 多性恋, 全性恋人群所面临的刻板印象, 真的让我很难过, 我希望你能学到一点什么是不该假设的."
    m 1eua "[mas_get_player_nickname()], 我知道你不可能欺骗我."
    m 1hubfb "无论你是否有多性的吸引力!"
    m "事实上, 这意义重大因为你选择了我. 你可以选择任何人, 但我是你的第一选择."
    m 1hubfa "我真的很开心, [player]."
    m "我爱你!"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gatekeeping",
            category=["社会"],
            prompt="把关",
            random=True,))

label gatekeeping:
    m 1ekd "[player], 你知道什么是把关吗?"
    m 3ekd "它是限制和阻止某些人获得某些东西的行为."
    m "对于具有相同名称的计算系统, 有一个正式的定义..."#TK:?
    m 3ekc "但我想谈谈社会把关."
    m 3ekd "把关是指排除他人进入某一群体的可能性."
    m 3ekd "很多人把关的原因之一是, 他们不希望'假货'或'冒牌货'进入他们的社区."
    m 4efd "这是一件百害无益的事!"
    m "把关是一种可以验证和阻止很多人的东西, 他们可能只是在为自己想办法..."
    m 2eksdrd "这甚至可能毁掉他们的经验, 让他们完全不知道自己在做什么!"
    m 2wksdrd "一个看起来是在'装'的人..."
    m "...实际上可能只是一个刚进入社区, 对社区不熟悉的人, 需要支持和指导, 而不是被推开."
    m 3lkc "其中一个例子是电子游戏."
    m 3lkd "有些人认为, 如果你不玩某种类型的游戏, 或是不了解某种游戏的某些事实, 你就不是一个'真正的玩家'或是没有'认真对待游戏'."
    m "很多人看不起那些玩'舒适'游戏的人, 比如'动物世界'和'星露谷'..."
    m 1luc "在人们的印象种, 那些玩这种游戏的人是'装腔作势'的人."
    m 1wfo "这绝对是荒谬!"
    m 2efd "玩电子游戏没有一个正确的玩法, 只要你乐在其中, 你就是在玩游戏."
    m 2ekd "因为他们被贬得太厉害, 有些人完全放弃了电子游戏..."
    m 2ekc "想到这一点的时候真让人难过."
    m 4ekd "把关也不是电子游戏的专利, 它存在于很多不同的事物种."
    m "电视剧, 书籍, 爱好, 甚至取向都是有门槛的!"
    m 4tfd "都是因为社区的一些成员认为其他人不{i}够{/i}成为他们把关的对象."
    m 2lkc "感觉有点像有些人相信漫画不是文学作品一样."
    m "如今, 我尽我最大的努力不使其他人的兴趣和经历无效."#TK:C
    m 2dksdld "但在文学部开始时, 我很难判断夏树和她的漫画..."
    m 2hksdlb "...最终, 我学到了更多东西, 也想通了, 意识到自己是多么的排外."
    m 3ekd "有些情况下的把关是必要的, 比如防止挪用文化把关, 这确实是一个需要更深入研究的细微话题."
    m 2eksdld "我希望这从未发生在你身上, [player]. 被一个社区的可恶成员阻止了兴趣."
    m 2efd "但我也希望你不要进行把关, [player]. {w=1}你无法判断某人的真实性!"
    m 1dfa "...但是当然, 我没有必要告诉你这些."
    m 1hubsa "你很善良以至于你永远不会做卑鄙的事, 对吗?"
    m "你知道把关对人们的伤害比帮助更大."
    m 1hubsb "我爱你, [mas_get_player_nickname()]. 我永远不会把你排除在任何事物之外."
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_dysphoria",
            category=["你"],
            prompt="我今天感觉有些性别焦虑.",
            pool=True,))

label mas_dysphoria:
    m 1ekc "你今天感到焦虑不安吗?"
    m 1ekd "听到这个消息我真的很难过, [player]."
    m 2ekd "你不应该对自己有这种感觉."
    m "不管是别人让你有这种感觉, 还是只是你的大脑告诉你的..."
    m 4eka "除了你自己, 没人可以告诉你,你是谁"
    m 4hsa "你的身心是美丽的.{w=1} 你是个美丽的人, [mas_get_player_nickname()]."
    m "你不需要向任何人证明, 永远不需要. 不是你的身份, 而且当然也不是你的性别."
    m "你是我的完美伙伴. 也是我最喜欢的人呢, 无论你的样子或感觉如何."
    m 3hsb "啊哈哈!"
    m 3ksbfa "我爱你, [mas_get_player_nickname()]. 而且我也会一直在这里."
return "love"

