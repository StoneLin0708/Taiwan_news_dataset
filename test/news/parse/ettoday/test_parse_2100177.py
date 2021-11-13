import re
import textwrap

import news.crawlers.db.schema
import news.crawlers.util.normalize
import news.crawlers.util.request_url
import news.parse.db.schema
import news.parse.ettoday


def test_parsing_result() -> None:
    r"""Ensure parsing result consistency."""
    company_id = news.crawlers.util.normalize.get_company_id(company='東森')
    url = r'https://star.ettoday.net/news/2100177'
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

    parsed_news = news.parse.ettoday.parser(raw_news=raw_news)

    assert parsed_news.article == re.sub(
        r'\n',
        '',
        textwrap.dedent(
            '''\
            賣座的謊言影片 大陸企業家馬雲投資,長達兩個多小時的「長津湖」影片,在大陸反美
            愛國情緒高漲之下,上映以來,票房紀錄飆高,迄自目前收入超過32億人民幣,各官媒與網站
            相關討論更是熱絡,當然千篇一律是贊揚與歌頌抗美援朝志願軍,網站也在流傳「長津湖」
            影片,相關評論也不斷在發表,已形成一股談論風潮,「長津湖」以愛國與宣傳為出發點,打擊
            美軍在韓戰表現為共識,看樣子已經達到目的。 「長津湖」,由大陸影劇界陳凱歌、徐克等
            名人聯合監製並執導,知名戰狼演員吳京等人演出,主要內容就是敘述志願軍連隊,在
            極度嚴寒艱困之下,如何克服逆境勇敢作戰,為「抗美援朝偉大戰役」作出傑出貢獻,讓
            很多大陸愛國觀眾看得如癡如狂,確定「美帝就是一隻紙老虎」因而產生解放軍必勝,
            美軍必敗的信念,有助於大陸凝聚反美抗美意志;不過令人大惑不解的是,解放軍有八一
            電影製片廠,1952年建廠,距今已有69年歷史,拍攝各類題材電影作品將近2,400餘部,
            他們有足夠的拍攝能力,為何不敢拍「偉大的長津湖戰役」?是想到就心虛之故嗎? 毛澤東
            與劉伯承的評價 任何一場戰役,要看最後戰果和評價,長津湖戰役,前共黨中央委員會主席
            毛澤東與前陸軍元帥劉伯承,是志願軍的自家人,二人給的評論如下: 長津湖戰役後,毛澤東
            給二十軍全體指戰員發了一封電報,總結道:看到東線戰鬥的報告,我的心情也極度的沉重,
            東線傷亡4萬多人,其中凍死凍傷就有3萬多人,教訓慘痛啊!大傷了我們的元氣。九兵團
            久居江南,一切戰備訓練都是解放台灣,現在卻來到風雪連天的高寒地區去打仗,先前沒有
            任何準備。 另外,朝鮮軍情十分緊急,部隊在開往東北的火車上才得到通知入朝,沒來得及
            換冬裝就直接渡過鴨綠江。志願軍九兵團將士始終在作戰中保持了大無畏的英雄氣概、顯示了
            超出世界上任何一支軍隊的勇敢精神和戰鬥力。 二次戰役東線戰鬥的勝利,是我們把
            美帝國主義侵略軍於鴨綠江邊打回到三八線上、保障了朝鮮人民的生存,保護了祖國的
            安全。戰鬥的勝利說明我們是不可欺負的,侵略者的進攻是可以擊退的。20軍此次入朝
            作戰,打得比較艱苦,戰役結束之後,可以到咸興五老里為中心進行休整,那裡比較暖和
            。 劉伯承元帥在南京軍事學院教學時,說過一段反應長津湖之最終結局的話:「長津湖一戰,
            一個兵團的兵力圍住美國陸戰第1師,沒有能夠殲滅,也沒有能夠擊潰,付出了10倍於敵人的
            代價,讓美軍全建制地撤出戰鬥,還帶走了所有的傷員和武器裝備...」 這是實話卻使志願軍
            難堪不已,更使指揮入侵的毛澤東大失顏面,因此1958年中國志願軍司令彭德懷,組織了對
            劉伯承軍事教條主義的批判,迫使劉伯承認錯道歉。 雙方兵力相差懸殊 參加長津湖戰役
            的雙方部隊,美軍為陸戰隊第一師與陸軍第7步兵師,總兵力為兩萬七千餘人;中國
            「抗美援朝志願軍」為志願軍第9兵團,下轄:第20軍有第58師、第59師、第60師、 第89師
            ;第27軍有第79師、第80師、第81師、第94師;第26軍有第76師、第77師、第78師;
            共計有3個軍級部隊,11個師級部隊,總兵力為15萬餘人。 長津湖發源於北韓黃草嶺,向北
            在柳潭里和下碣隅里之間形成長津湖,最後注入鴨綠江,長津湖戰役,從1950年11月27日
            至12月6日共進行了十天,對整場韓戰的進程有重大的影響,戰役包括防守下碣隅里、
            柳潭里之地區要域、美軍陸戰隊1師第5團及第7團從柳潭裡突圍撤出碣隅里、第31團作戰隊
            在長津郡東面的戰鬥。中國志願軍阻止了聯合國軍的攻勢,美陸戰1師與陸軍第7步兵師,
            基本上全身而退,而且運走了近10萬難民,能帶走10萬難民就證明美軍戰力損失十分有限
            。 長津湖戰役是志願軍進入朝鮮的第二次戰役,在戰略戰術上是想運用第9兵團的大舉襲擊、
            分割包圍並全殲美軍王牌軍陸戰第1師和步兵第7師,但是最後眼睜睜的看美軍順利突圍脫離,
            志願軍接受悽慘而重大的失敗。 想要大口吞卻牙崩滿地 15餘萬的志願軍對不足3萬的美軍,
            佔有絕對優勢的志願軍,被居於絕對劣勢的美軍打敗,好意思說是偉大的勝利嗎?有意要對美軍
            包圍殲滅的第9兵團,由於戰略指導錯誤,用兵倉促,兵力調遣無彈性,武器裝備落後,
            禦寒冬衣欠缺,糧食不繼,後勤補給不當等原因,造成第九兵團戰鬥傷亡1萬9,202人,
            凍傷2萬8,954人(其中凍死3,000多人),總計減少4萬8,156官兵,兵團受損幅度
            過大。 根據美軍戰後公布的資料,陸戰1師從10月26日至12月15日(是從元山登陸進入
            東線戰場,到從興南登船撤出整個東線作戰,而非僅指長津湖之戰)。陣亡604人,
            傷重死亡114人,失蹤192人,傷3千508人,戰鬥傷亡總數為4千418人。 美軍陸戰1師
            經整補後,陸續執行戰鬥任務;中共黨史出版社「開國第一戰」記載:第20軍和27軍缺席了
            3、4次戰役,參加了第5次戰役,但不再被當作主力使用,代表傷亡過重不能負荷較艱鉅任務
            。主導長津湖戰役的第一主將、中共第9兵團司令兼政委宋時輪,在戰役剛剛結束的
            1950年12月11日,就向中央軍委會遞交了「第9兵團對東線作戰的檢討」,於此同時,參戰的
            第20、27、26三個軍以及各部門也都分別做了檢討。宋時輪自己對長津湖戰役的結論是
            這麼寫的:「這次作戰打得很不好,不僅未能全殲美陸1師及第7師,反遭巨大減員,嚴重
            縮小戰力。」 慘無人道的長津湖戰役 兵團司令官兼政委都坦承失敗,請問「長津湖」
            影片強調的偉大勝利在哪裡?長津湖之役決定倉促,緊急投入部隊連冬服都沒有,在零下
            30到40度極低溫下作戰,因美軍享有空優,志願軍多半利用夜間發起攻擊,白天趴在隱蔽
            攻擊準備位置待機,沒有冬服的部隊官兵,因此一個又一個連,活活被凍死在待機位置,影片
            裡也有提到所謂的冰雕連,只是不敢講不止一個連,而是好多個連慘遭凍死。 志願軍
            部隊糧食欠缺,謹以土豆(馬鈴薯)充飢,士兵一天只分配一個,有些部隊三天都分配
            不到一個,土豆被極低溫凍得比石頭還硬,根本啃不動,用槍托砸碎跟雪一起硬吞下肚,
            官兵就這樣在又冷又餓情況下,全身發抖的頂上火線,極低溫使部隊完全無法施展戰力
            。 志願軍武器耐不住極低溫,故障頻頻,有些機槍步槍子彈不能上膛不能擊發,遇上美軍
            的交叉火網掃射就傻眼,只能在原地被打死,火箭筒根本打不進美軍坦克,美軍的空優掌握,
            以強大的空中火力,炸翻地面看得到的志願軍,而志願軍無防空武器還擊,只能趴在雪地挨炸,
            美軍有厚實的溫暖冬衣避寒,有營養的軍用罐頭食用,有可靠的武器打得志願軍死傷慘重,有
            坦克與火炮近距離提供火力支援,有源源不斷的充足空降補給,跟志願軍樣樣匱乏有雲泥之別
            ,想要包圍殲滅美軍是作夢吧! 美軍陸戰1師訓練精良,裝備現代化,作戰經驗豐富,是美國
            地面戰力最強的部隊,反觀志願軍,欠缺臨戰訓練,第一線官兵毫無經驗可言,有一個連隊
            軍官士官被打死光光,打到後來由19歲的士兵代理連長,19歲的士兵懂兵力分配、懂
            火力運用、懂上級與友軍協同作戰嗎?當然不懂,就憑這樣的素質,能創造出
            「偉大輝煌的勝利」嗎?當然不可能! 殲滅北極熊團的謊言 中共官方一直宣稱,
            此次戰役的一大戰果,是全殲美軍王牌的北極熊團三千餘人,並繳獲其團旗,
            被志願軍殲滅的所謂「北極熊團」,實際上全稱叫做美軍陸1師第31團作戰隊
            (英文縮寫為RCT-31),因為指揮官是來自北極熊團的團長麥克萊恩,所以在美軍中普遍稱其
            為麥克萊恩特遣隊(Task Force Maclean),他們受命擔任陸戰1師撤退的掩護部隊
            。 費斯特遣隊是由北極熊團下屬第3營加上第32步兵團第1營,外加師屬炮兵營的兩個炮兵
            連混編組成的團級作戰單位,是一支混編的部隊,並非真正的北極熊團。只是這支特遣隊
            最初由麥克萊恩指揮並攜帶團旗,團指揮所撤退時團旗遺失,被志願軍拾獲,所以中共單憑
            一幅團旗,稱之為全殲北極熊團。 費斯特遣隊總共只有3千288人,以極為劣勢的兵力,
            抵擋志願軍3個師將近3萬5,000人圍攻,時間長達4天之久,成功掩護了美軍陸戰1師與
            步兵第7師撤退。最後雖然建制被打散,但最終仍有約1千600人成功突圍,除了將約
            1千150餘名傷兵送醫,還將有戰力的490多人被編成1個營,歸建陸戰1師繼續轉戰。
            而真正的北極熊團31團編制仍在,餘部在經過整補後完成重建,繼續由陸戰1師指揮作戰,
            並參加上甘嶺戰役。因抗美情緒高漲之故,「長津湖」影片中充斥謊言,杜撰處處,
            根本就是個化失敗為勝利的騙局!
            '''
        ),
    )
    assert parsed_news.category == '雲論'
    assert parsed_news.company_id == company_id
    assert parsed_news.timestamp == 1634101620
    assert parsed_news.reporter == '宋兆文'
    assert parsed_news.title == '慘無人道的長津湖戰役'
    assert parsed_news.url_pattern == '2100177'
