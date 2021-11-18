import re
import textwrap

import news.crawlers.db.schema
import news.crawlers.util.normalize
import news.crawlers.util.request_url
import news.parse.db.schema
import news.parse.epochtimes


def test_parsing_result() -> None:
    r"""Ensure parsing result consistency."""
    company_id = news.crawlers.util.normalize.get_company_id(company='大紀元')
    url = r'https://www.epochtimes.com/b5/19/12/28/n11751714.htm'
    response = news.crawlers.util.request_url.get(url=url)

    raw_news = news.crawlers.db.schema.RawNews(
        company_id=company_id,
        raw_xml=news.crawlers.util.normalize.compress_raw_xml(
            raw_xml=response.text,
        ),
        url_pattern=news.crawlers.util.normalize.compress_url(
            company_id=company_id,
            url=url,
        )
    )

    parsed_news = news.parse.epochtimes.parser(raw_news=raw_news)

    assert parsed_news.article == re.sub(
        r'\n',
        '',
        textwrap.dedent(
            '''\
            看到網上的一個黑色幽默:還有幾天就進入小康社會了,趁著我還沒有被消失,來看看大家,
            算是告個別。這個黑色幽默,是根據中共所說的一個目標演繹來的。中共在十八大曾誇下海口
            ,說到2020年將消滅貧困縣,所有貧窮人口實現脫貧。 眼看著2020年就要到了,算上今天
            (12月28日),總計還有4天時間。那麼中國的經濟狀況怎麼樣了呢?在昨天(12月27日)結束
            的全國財政工作會議上,要求明年把握好「以收定支、量力而行」的原則。中共財政部長劉昆
            呼籲,要樹立「過緊日子」的思想。 一系列的跡象顯示,2020年消滅貧困縣、所有貧窮人口
            實現脫貧僅僅是個「夢」。聖誕節前夕,中共國務院還發文要求各地區「第一時間處置因
            規模性失業引發的群體性突發事件」。2020年中共的危機要來了? 2020「過緊日子」? 
            一連兩天在北京召開的財政工作會議要求,對2020年的財政工作,要著重把握做好「以收定支、
            量力而行」的原則。對明年的財政工作要「提質增效」,注重「結構調整」,從「質」和「量」
            兩方面發力。 劉昆在會上表示,減稅降費是2020年的「頭等大事」,通過「減稅、降費政策
            緩衝貿易戰壓力」。不過他認為,這也造成「政府財政短收」,只能通過「節省非急需支出」
            等方式實現平衡。 他呼籲,牢固樹立「過緊日子」思想,還要求抓好「三保」工作。「三保」
            ,指的是保工資、保運轉、保民生。 當天中共財政部網站在新聞稿表示,對於「一般性支出要
            大力壓減,不必要的項目指出要堅決取消,新增項目支出要從嚴控制,原則上不開新的支出口子
            」。 財政部門的說法,與實現脫貧顯然有著天壤之別。 中國經濟告急? 從中共大呼小叫「
            過緊日子」可以看出,中共的財政狀況可能已經非常吃緊了,兜裡沒錢了。財政吃緊的原因有
            中國經濟自身的羸弱因素,也有貿易戰帶來的影響。內外因素疊加,加速了中國經濟的惡化
            。 馬雲12月21日曾說,他一天接到過5個借錢電話。他的朋友圈中,一個星期當中有10個要
            賣房籌資。馬雲的圈子是這個境況,別人什麼樣呢?馬雲自己都說,「浙商都過不去,其它商家
            肯定也過不去。」而且馬雲補充了一句話,「也許這只是不容易的開始。」 近日,有26位全球
            經濟學家對明年的中國經濟增速做出了預測。《日經新聞》報導,專家們預測明年中國GDP
            增速是5.6%~6.1%,平均值是5.9%。這些外國專家們認為,明年中國經濟的增長率將出現
            1990年以來首度「破6」的情況。 野村證券首席經濟學家陸挺表示,「中國的下滑周期尚未
            結束」,經濟成長被地方政府財政惡化、低線(三線以下)城市信貸收縮,以及製造業投資疲軟
            等拖累。 曾被中共總理李克強邀請分享觀點、素有「中國第一經濟師」之稱的高善文認為,
            今後十年的平均經濟增速不會超過5%。這位安信證券首席經濟學家在11月27日演講中指出,
            明年中國經濟會進入「保四爭五」階段。 高善文的預測比國外的經濟學家更悲觀,用中共的
            說法這是「唱衰」。但是有一個奇怪現象,他的演講內容,最初遭到了全網封殺。不過隨後
            又能在大陸一些網站上找到,似乎是被放行了,是不是他的觀點被北京接受了呢? 儘管第四
            季度GDP增速還沒有公布,但從整體來看,下行仍然明顯。按照前三個季度以0.2%遞減的趨勢
            來看,第四季度會如何呢? 高盛前不久指出,中國經濟第三季度已經跌到了6%,第四季度
            很可能會「跌穿6%」。 體制內知名學者余永定的呼籲也很值得注意,他認為GDP增速在
            「觸6」後應當煞車,「寧可財政狀況暫時惡化」,也要穩住經濟增長。 就是說,國內外的專家
            都不太看好第四季度的經濟增長。 失業潮洶湧? 如果按照26位外國經濟學家的預估中值,
            明年的經濟增速是5.9%,那就意味著2020年的經濟增長,比2019年估算的經濟增速6.25%
            低了0.35個百分點。中共給2019年設定的經濟增長目標是6%~6.5%,且估算是6.25%。 這
            意味什麼呢?自由亞洲引述專家的觀點表示,中國GDP每下降一個百分點,就會造成100到200
            萬人失業。 那麼2019年工人失業狀況如何呢? 中共人力保障部的數字,第三季度末的全國
            城鎮登記失業率是3.61%。這個數字,只比美國現在的失業率3.5%高了0.11個百分點。 美國
            的3.5%失業率是50年來的最低點,反證著美國是充分就業狀態。那麼照此推理,按照中共
            3.61%這個數字來判斷,中國即便不是充分就業,應該也不會太差。或者說,中國工人的就業
            情況應該還是不錯的。 但實際早在今年年初,日本媒體報導,美中貿易戰當時已經造成了500
            多萬家中國企業倒閉,有高達1000萬人失業。現在一年過去了,又有多少工廠倒閉?多少外企
            撤離?多少工人失業呢? 其實從去年下半年開始,中國經濟產業鏈出現破裂後,失業潮就已經
            出現了。大量的建築和工廠工人失業,農民被迫返鄉。中共2018年11月的公布的數據,有高達
            740萬的農民返回家鄉。這些返鄉農民實際就是失業,但中共美其名曰「回鄉創業」。 就連
            曾被看作一向穩定的金融、IT行業也在大規模裁員,曾經的「金飯碗」已經被打破了。今年
            5月,世界軟件巨頭甲骨文裁員近千人,美國在華規模最大的偉創力,通知4萬名員工放假。 另
            外特別提醒大家注意,中共說的「登記失業率」是3.61%。就是說,失業以後在中共那裡登記
            在冊的,才可能被統計進去,不包括沒有登記的。沒登記的,即使失業也不算失業。 原南京
            師範大學副教授郭泉表示,中共的「登記失業率」和「調查失業率」是難以令人相信的,這個
            中共特色的「調查失業率」並不是真實的失業率。 他用了一個簡單的算法,中國真實的失業
            人數=公開的城鎮登記失業人數+城市隱藏性失業人數+農村失業人士。最後他推算出的實際
            失業率大概是在25.48%,也就是說,不到4個人當中,就有一個人失業。 恐爆發大規模暴動
            ? 究竟有多少人失業,中共始終沒有公布過,也不可能公布,這對中共來說可能是個祕密。但是
            從中共的近期動作來看,失業人口很可能已經相當大。 聖誕節前夕,中共國務院發出了一份
            《關於進一步做好穩就業工作的意見》,要求進一步做好穩就業的工作。其中規定打算裁員的
            企業,必須提前30天向工會或者全體職工說明相關情況,並完善突發事件的處理機制。 在
            李克強簽批的這份文件中,重點強調採用6項措施,防範爆發「規模性失業潮」,全力防範化解
            「規模性失業」的風險。 文件要求各地區要「第一時間處置因規模性失業引發的群體性
            突發事件,防止矛盾激化和事態擴大」。 河北學者郭浩對自由亞洲表示,就算沒有美中之間
            的貿易摩擦,中國經濟增長也到了瓶頸階段。他指出,「中國經濟在不斷下滑,貿易戰加劇了
            這種趨勢。很多企業經營非常困難,有的直接倒閉。失業者不斷增加,就業壓力不斷增大。
            失業者越多,維穩就越困難。中共依然用老套路,想行政干預,也就是所謂的保就業。但是
            靠發文件的方式保就業,是保不了的」。 從中共的措辭當中也不難看出,中國的經濟形勢
            已經相當緊迫,規模性失業成了中共最大的隱憂之一。中共擔心,沒錢又沒有工作的人們一旦
            出現問題,很可能會釀成大事件,甚至暴動。 如果出現蝴蝶效應,全國所有的失業人口都
            站起來說話,那麼這種大面積的群體性事件就是飛出的又一隻黑天鵝。 湖南法律界學者
            范魯湘認為,種種原因導致大量的企業裁員,「有些企業本身就難以存活下去,失業潮是必然的。
            現在中共這個《意見》文件反映了失業潮已經出現,人們在失去工作後,各種不滿越來越多,
            必然會導致群體事件」。 北京心病多 僅僅是一個內部經濟問題,已經把中共搞得焦頭爛額。
            在經濟危機之下,大規模失業的工人成了中共一個新的麻煩,又添了一塊大心病。 但中共的
            心病不止是防止工人暴動,香港問題已經讓中共的頭疼了半年多了。儘管中共一再逼迫港府
            升級暴力,港警一再升級武力鎮壓這場民主抗爭,但是暴力威脅壓不倒一城。抗爭了半年之後,
            香港人仍然一如既往地要求北京兌現承諾,無畏無懼、百折不撓。 而大搞強人政治的北京,
            始終不肯向香港人讓步。但在美國的威懾之下,中共也不敢直接動武,美國已經針對侵犯香港
            人權立法。面子大國在香港人的抗爭和美國人的制裁之下,上不來也下不去,就卡在中間,死要
            面子活受罪。 此外還有新疆、西藏、台灣等等諸多問題,都是中共的心病。折騰來折騰去,
            中共在內部已經是危機重重。而在外部,中共同樣四處樹敵,國際反共陣營越來越龐大。 一場
            貿易逆差引起的美中貿易戰,本來可以通過「好朋友」之間的和平商量解決,偏要率先發起關稅
            制裁美國。打了一年多後,雖然近期雙方都在唱好第一階段協議,但是到目前還沒有簽署
            。 即使簽署也不意味著貿易戰結束,雙方還沒有觸及到實質性的問題,談判仍是在淺水區
            。中共經貿政策的結構性問題一旦觸及,那才是大戲開始的時候。多方認為,一旦進入談判
            深水區,貿易戰很可能將重燃戰火。 就目前來說,貿易戰已經擴展到了科技、間諜、軍事等等
            多個領域。日本、加拿大、澳大利亞和歐盟28國,以及北大西洋公約組織等等,都在用不同
            方式,加入到反中共陣營。 人心盡失 習近平面臨多方挑戰 北京當局對國際國內事務的誤判
            和處理不當,已經令習近平相當被動。在海外,圍繞習的正反輿論激戰很明顯。 26日,一名
            化工業網友在知乎發問:「如何徹底清洗細頸瓶」,隨後知乎被指責「違反互聯網相關法律
            法規」。原因是問題中的「細頸瓶」和「習近平」諧音,而且前面有「清洗」二字。 19日,
            「中改研究」等大陸微信號紛紛轉載一篇關於鄧小平廢除「幹部領導職務終身制」的文章,
            影射習的修憲。這篇文章卻沒有被中共網警刪除,令人奇怪。 16日,親共學者、東亞研究所
            所長鄭永年在香港演講,指出中共政治體制的最大問題是「決策權太過集中於中央」。他說過
            分強調「中央集權」於「頂層設計」,地方無法制定出符合當地實際情況的政策。 15日,親共
            的《世界日報》援引中共內部消息說,「習的任期並不一定會超過中共規定的兩屆」;中共
            高層連同習本人,已經對下一屆接班人進行了內定。 文章還指出,由於中共內外交困不斷
            加深,習思想和執政路線「在中共內部更加引起反彈和質疑,習在黨內的威望也不斷下降」
            。 時事評論員李林一表示,中共黨內的改革派已經對習的所謂改革失去了信心,而以江澤民為
            首的貪腐派更是對習虎視眈眈,盼著他早點下台。照這麼走下去,「明年習近平處境更加艱難
            」。 換句話說,北京現在是兩頭都不討好,已經人心盡失了。 中共已走入死胡同 前兩天看了
            諸葛高參在大紀元發表的又一篇力作《2019年終,只剩一人在假睡》,感覺說得非常有道理。
            從現在的結果來看,北京是走了智障到家的臭棋,把自己搞亂了。沒看清路,也沒看懂人心,
            都是自己惹的禍,還沒法問責,如今左右為難、騎虎難下。 文中說北京當局的「脫貧也是個
            臆想,還拍腦門定個目標時間點:2020。初一看這日子,我就差點笑岔氣了。現在看,還剩
            幾天,中國人民統統都小康嘍。隨便哪國人到牆國走走,都知道這就是個夢話,黃粱夢囈
            。」 不久前,美國著名的中國問題專家林蔚對英文大紀元透露,有一位和習近平關係密切的
            幕僚,曾坦率地告訴他,中共體制內的人都知道「已經走投無路了」。 林蔚引述那位習近平
            幕僚的話說,「每個人都清楚這個體制已經完了,我們(中共)進了死胡同,不知道下一步該
            怎麼走,處處是雷,踏錯一步就可能粉身碎骨。」
            '''
        ),
    )
    assert parsed_news.category == '新聞看點'
    assert parsed_news.company_id == company_id
    assert parsed_news.timestamp == 1577462400
    assert parsed_news.reporter is None
    assert parsed_news.title == '危機來了?官稱過緊日子及防暴動'
    assert parsed_news.url_pattern == '19-12-28-11751714'