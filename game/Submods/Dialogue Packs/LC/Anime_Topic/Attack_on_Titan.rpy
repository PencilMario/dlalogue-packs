
#init -990 python:
#    store.mas_submod_utils.Submod(
#        author="LC",
#        name="动漫话题包",
#        description="莫妮卡借了你的设备看了一些番",
#        version='1.0.0'
#    )

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_LC",
            category=['动漫'],
            prompt="你有看过《进击的巨人》嘛",
            random=True,
            pool=True,
        )
    )

label monika_LC:
    m 1suo "进巨!!!."
    m 2sua "我真的很喜欢这一部番!."
    m 4lksdlb "嘛,不要诧异啦."
    m 3eub "在你离开的时间里我有过尝试去深入了解一下动漫的. "
    m 1eub "在看完后这一部番后,我想能理解夏树为什么会对那些漫画和动漫如此喜爱了,他们的确是一个很让人着迷的文学."
    $_history_list.pop()
    m 3eku "哦!对了,因为剧透可能会影响到你的看番体验,所以我想问一下,[player],你打算看《进击的巨人》嘛?还是说,你已经看过了?{nw}"               
    menu:
        "看过了哦":         
            m 1hua "好耶！"
            m 1eub "谢谢你告诉我!"
            m 7rua "因为我只看完了动漫,所以我对这部番有一些理解,虽然可能会因为没看漫画而了解的不够全面,也可能讲得不是很好,但是我还是蛮想讲讲的,你想听听嘛?{nw}"
            menu:
                "好啊, 没问题啊":
                    m 1eua "好的哦."
                    m 1eub "我认为《进击的巨人》是一部有相当的文学追求的作品."
                    m 1rusdlb "虽然有不少人觉得谏山创老师的画技有点糟糕."
                    m 1eua "但是我觉得他所展现出的文学表现力还是让我特别服气."
                    m 1eub "无论是从剧情还是细节,都很让我深受震撼."
                    m 1rub "而且,"
                    extend 1eub "说实话,看了这么多书..."
                    m 1eud "我还是很少有看到像巨人这样摧毁世界观再重建一个新的世界观的书."
                    m 3eub "而且这个过程并显得不突兀,这也是我佩服谏山创老师的一点,动漫中的很多细节都有为后来的剧情铺陈."
                    m 1euu "总的来说,巨人整体给我的感受,并不差,甚至可以说相当优秀."
                    m 1rusdld "至于网上那些说因为巨人烂尾而否定整个作品的价值的那种人."
                    m 1rusdlc "我是蛮不喜欢的."
                    m 1eusdlc "虽然我还没看巨人的结局."
                    m 1eusdlc "但我知道结局肯定不会太好写的."
                    m 2eusdld "'种族矛盾',本身就是一个非常难以解决的问题,人类千年来都存在着这样的问题."
                    m 1rssdlb "帕拉迪岛兵团分裂出了两个派别'耶派'和'韩派'."
                    m 1eud "两派都说不上哪个是真正对的."
                    extend 1lud "两派都有为了帕拉迪岛而献出了心脏的人."
                    m 1euc "耶派保护岛内而敌对岛外."
                    m 1ruc "而韩派则是保护岛内的同时想要尽量保护岛外."
                    m 1lud "能说得上对错嘛."
                    m 1dkc "不过是立场不同罢了."
                    m 1ekc "即便会有部分人过于极端."
                    m 1ekd "但是一旦具体分析到他们的个体."
                    m 1ekd "便也难以去定义他的行为了."
                    m 3eud "巨人真的引起了我很大的反思."
                    m 3euc "千年来,人类都在进行无休止的斗争."
                    m 3euc "但是斗争来斗争去,最终都得到了什么."
                    m 3eusdlc "得到了和平吗."
                    m 1rusdlc "说实话我不敢苟同."
                    m 1euc "塔塔开,得到的是世界末日."
                    m 1euc "但是不塔塔开,得到的就是帕拉迪岛的末日."
                    m 1ekd "必须有一方彻底消失这种斗争才会结束吗?"
                    m 2dkd "我也不知道."
                    m 3rud "韩吉阿尔敏他们一直都在争取对外沟通."
                    m 3lud "但是愿意去了解岛内的人."
                    m 1euc "可以说是基本没有."
                    m 2eusdlc "即便有,真正想帮助帕拉迪岛的人也是少得可怜."
                    m 2eusdlc "全世界所有人都觉得屠杀艾尔迪亚恶魔当然是正义的."
                    m 2rusdlc "对啊,恶魔那么可怕,那么有威胁,不存在当然会让我安心."
                    m 1eusdld "问题便是,帕拉迪岛的人,"
                    extend 3eusdld "都只是很普通的普通人."
                    m 1eusdld "全世界所怨恨的过去的艾尔迪亚帝国的暴行,和活在现在的被囚禁的他们有关吗?"
                    m 1eusdld "有关吗?"
                    extend 1eusdlc "显然是没有的."
                    m 1gksdlc "有的只是阴谋论和不愿去理解."
                    m 1eksdlc "我认为谏山创老师的思想一直都是'反战'."
                    m 1eksdlc "可是却被说右翼,"
                    extend 1eksdld "被嘲讽,被不理解,甚至是被辱骂."
                    m 1eksdld "这样真的很让我感到难过."
                    m 1lksdld "我并不敢说我有多理解巨人这部番."
                    m 1eub "但是,这部番绝对可以称作一部神作了."
                    m 1eud "能引起人们去思考去讨论."
                    m 1euu "这个文学便是富有价值的."
                    m 3eub "况且,"
                    extend 3rusdlb "不可能将一个政治家都难以解决的问题丢给一个漫画家来解决吧."
                    m 1eub "所以谏山创老师不管会写出什么样的结局,我想我也能坦然接受了."
                "要不还是下次再说吧":
                    m 1huu "好吧."
                    return
        "我想看, 但是我还没开始看":
            m 1eub "哦,我想我不能给你剧透."
            m 1hub "很高兴我们在看同一部番."
            m 1kub "等你看完之后我们再在一起说说他好吗."
            m 1hub "爱你~" 
            return "love"
       
        "我不太喜欢看番...":
            m 1rusdlb "哦,好吧."
            m 1lusdlb "这没什么的,不是吗?"
            extend 1musdlb "其实我对这些的兴趣也不是那么大啦."
            m 1gusdlb "况且进巨也不能算是全年龄的动漫."
            m 1eua "你也许会有更好的文学可以推荐给我?"
            m 1eua "我会很乐意看看的."
            extend 1kua "诶嘿嘿~"
            return                                                     
    
        "我连漫画都看完了":
            m 1rusdlb "啊..."
            m 1lusdlb "那个..."
            extend 1lusdlb "[player]..."
            m 1rusdlb "我还没看漫画呢."
            m 1rusdlb "我只看了动漫最终季Part3还没出."
            m 1lusdla "因为我真的很想体验视听盛宴,也不想被剧透."
            m 1lusdla "所以我们就此打住好吗."
            m 1ekbsa "爱你哦~"
            return "love"