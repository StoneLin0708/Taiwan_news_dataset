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
    url = r'https://www.epochtimes.com/b5/19/5/19/n11266537.htm'
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
            本文是一名旅居美國的北京法輪大法弟子,以親身經歷憶述李洪志先生當年傳法時所展現出來
            的種種奇蹟,包括1993年在北京東方健康博覽會上治病救人的神蹟。法輪功,也稱「法輪大法
            」,由李洪志先生於1992年5月傳出,是一個以宇宙最高特性「真、善、忍」為根本指導,按照
            宇宙演化原理修煉的佛家修煉功法,至今已洪傳世界120多個國家和地區。 我叫朱萍,北京人
            ,1951年出生,今年68歲,現居住在美國紐約。我於1993年春天得法,迄今修煉近26年。我有
            幸參加了1993年東方健康博覽會,在博覽會上每天師父和他帶的弟子,給好多人治病。 我
            親眼見證了師父治病救人的神蹟。在法輪大法洪傳27周年之際,我在此回憶李洪志師父當年
            在中國大陸傳法時所展現出來的種種奇跡,這些神奇,見證了法輪大法是千載萬載難逢的高德
            大道,也見證了李洪志師父為救度眾生展示神蹟,福澤世人。 那是在1993年冬天12月份左右,
            在東方健康博覽會上我見到了師父,親耳聆聽了師父的講法,在班上師父給我們調理身體兩次,
            我的世界觀發生了根本性的變化,我覺得我是世界上最幸運的人!從此以後,我就每天按照師父
            要求的「真、善、忍」心性標準去做人、去工作。大法的神奇,在我的身上充分展現出來。在
            這25年半的時間裡,我從來沒有吃過一粒藥,也沒有進過一次醫院。上樓梯,我都是一口氣爬到
            11、12層,都不覺得累。 師父在《轉法輪》裡說,「我把我的功分給我帶的弟子,每人一份,
            都是上百種功能合成的能量團。」這些弟子我都見到了。當時法輪功展位上的人特別多,別的
            展位確實沒有多少人;法輪功的攤位上每天都排著三行隊,第一行隊,等著掛上午的號,第二行
            隊等著掛下午的號,隊伍很長,拐了幾個彎,這是我親眼看見的。第三行隊等著師父給簽字,
            當時我在第三行隊伍裡。 聾啞小女孩開口講話 在排隊時,給我印象最深刻的是一個聾啞小
            女孩,四歲左右。小女孩的媽媽很年輕,進來了之後就問:「李大師在哪?李大師在哪?」 在
            國際展覽中心的大廳裡,師父真的與眾不同,細高挑兒,臉上一點皺紋都沒有,神采奕奕。當時
            是冬天,下著大雪,但我每天都想去健康博覽會,想見到師父,每次見到之後就覺得特別親切
            。 我看到這個小女孩,她媽媽跟她說話,她聽不見。她媽媽對師父說:「李大師,我這女兒
            聾啞,聽不見。」師父說:「哦!」然後她把情況向師父說了以後,師父就讓小女孩站在師父
            面前,師父就用手劃拉,在她身體後面上下地劃拉,然後在她頭頂上也劃拉了幾下,當時我沒有
            那麼多想法,後來就是1995年元月《轉法輪》出版以後,知道師父在給她灌頂,師父給她清理
            身體。 圍觀的人很多,師父就對小女孩說:「去!那邊去!」因為博覽中心很大,小女孩聽見了
            就跑去離師父很遠的地兒。小女孩跑很遠後就站在那兒笑,師父特別祥和慈悲地向她招手說:
            「過來!上這來。」小女孩又跑過來了,我看見她媽媽在旁邊感動地哭。小女孩就跑過來,師父
            給她媽媽說:「好了!」她媽媽哭得挺厲害的,然後就抱著女兒,撲通一聲就給師父跪下了。 當
            時好多圍觀的人,好多人都哭了,親眼見證了師父救人的神蹟,就幾分鐘的時間,這小孩就聽見
            了,也能說話了。她媽媽哭得特別厲害,然後師父就說:「起來起來,別這樣。」 我當時就心想
            ,這個年輕的媽媽悟性怎麼那麼好啊。我感覺身後有東西在動,後來知道是師父打出那麼多
            法輪在給我調理身體。我好感動啊!我的眼淚不停地往下流。 這個時候師父就把小女孩帶到
            大廳的一面牆邊上。這時候,小女孩背靠著牆,師父就站在她的面前,師父再一次給她清理身體
            ,給她頭頂上劃拉劃拉,身體前邊劃拉劃拉,後來這小女孩也會說話了,她媽媽特別高興。這是
            我碰到的,親眼看到的師父救人的神蹟,到現在為止在我的腦海裡記憶猶新。 從1993年到現在
            ,已有25年之久,在修煉的過程當中,有時候我想起這小女孩時,曾在心裡呼喚著:「小女孩,
            你在哪裡?我多麼想見你啊!你是多麼幸運啊!」 癱瘓老人邁開了雙腿 還有一件事我記得
            很清楚,有一天好像是下午,我在大廳裡,因為師父和他的弟子一直在給不同的人調理身體,
            然後我就聽見:「李大師在哪?李大師在哪?」我看見四個人抬著一個擔架,擔架上是一個老
            太太,後面還跟著幾個人。 後來找到李大師以後,她請師父給她看一看,師父就問了問情況。
            她的兒女們就把母親的情況告訴師父,「她癱瘓在床好長時間了。」師父說:「知道了。」
            然後師父就問她:「怎麼樣?能聽見我說的嗎?」她點點頭。「能配合嗎?」對方說,「能。」
            由於她躺在擔架上,師父就彎著腰,用手來回劃拉,給她調整身體、清理身體,後來師父就跟
            她說:「你坐起來吧!」她好像不相信自己的耳朵,但是,一下子就坐起來了,在場的人都鼓掌。
            這時候好多人都哭了。 她坐起來以後,師父又給她調整身體,在背後來回地劃拉,也給她灌頂
            了。過一會兒,師父說:「你站起來!」我看她表情似乎在說:「我能站起來嗎?」事實上,她站
            起來了,師父跟她說,「你邁腿」,「來!往前走!」師父往後退著,她在師父的對面,往前走著,
            師父說:「來!來!來!」師父往後退,她就是一步兩步三步走,眼淚一下就從臉上流下來了
            。 她非常地感動,師父說:「來來來,往前走!往前走!」師父讓她轉一圈,在場的人,有的人哭
            了,大家都鼓掌。我聽見我後面的人說:「神啊!真神啊!」有的人就說,「真佛下來啦!」大家
            都在那哭,後來她就圍著那個場又走了一圈,大家都左顧右盼的,這時候她的兒女們,含著眼淚
            全都跑到師父面前,撲通一聲全都給師父跪下。好感人!好多人都哭了。 她的兒女跪著,磕著
            響頭:「謝謝李大師!謝謝李大師!唉呀!我媽媽這下可好了,她癱瘓這麼長時間,謝謝李大師!」
            看到這以後,我也哭了。師父的法輪在轉,給我調整身體,當時不知道為什麼我說不出話來,
            後來才明白師父的場很強,師父的場就是讓人感到非常舒服,無意中就給好多人都調整了身體。
            真的是這樣。 煉功時被能量場罩著 一片輝光 在我身上還有一件非常神奇的事情:早上我和
            同修煉完功,當時我身上帶著一個照相機,我帶去煉功點,給同修照幾張相,留一點資料,因為
            煉完功我們都是在煉功點學法。後來沒想到同修給我照了一張照片,就這張,我記得是1995年
            的秋天,這張照片的神奇就在我身上展現出來, 我當時打坐身體熱乎乎的,周圍都是高能量
            物質包圍著我,一片輝光。 好多同修看了以後,感到驚歎。我們到外地到農村洪法時,有的人
            看到這張照片,以及好多另外空間的其它景象後,從此得法。 奇跡:母雞生了帶把兒的雞蛋 除
            了我身體上發生的這個神奇變化之外,我身邊還發生了一件事。我們煉功點上的一個同修,
            想讓他老伴修煉,他說,「法輪功可好了,你看我現在身體多好,你快煉法輪功吧」。他老伴說:
            「得了吧,除非你養的母雞下蛋帶個把,我就開始修煉。」第二天他們家母雞真下了個帶把的
            雞蛋。結果,他老伴真的開始修煉了。 同修們覺得非常神奇。大家在一起就議論這事情,大家
            說師父太慈悲了,為了讓他們得法,他們家真的下了一顆帶把的雞蛋。 我是怎麼得到這張照片
            的呢?就是有一天,週六週日不上班,就在公園煉功,輔導員悄悄地走到我面前,說:「送你一張
            照片。」我說:「這是啥呀?」後來她就說了帶把兒的雞蛋的故事,我聽後覺得師父真是用心
            良苦,慈悲偉大。
            '''
        ),
    )
    assert parsed_news.category == '北美新聞,美國社會'
    assert parsed_news.company_id == company_id
    assert parsed_news.timestamp == 1558195200
    assert parsed_news.reporter is None
    assert parsed_news.title == '聾啞人能說話 癱瘓人邁雙腿 親歷者憶神蹟'
    assert parsed_news.url_pattern == '19-5-19-11266537'