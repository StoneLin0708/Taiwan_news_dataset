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
    url = r'https://www.epochtimes.com/b5/19/12/19/n11733936.htm'
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
            週三(12/18)習近平抵達澳門訪問。澳門安保空前嚴厲,輕軌停駛,多家港媒記者被拒入境,
            外傳中共有意給予澳門優惠政策,將其打造成金融中心。 不過在習訪問前夕, 國際評級機構
            惠譽剛把澳門評級展望降至「負面」。 中共的「優惠政策」能把澳門變成香港嗎? 澳門是
            「一國兩制」成功的範例嗎? 嘉賓: 唐靖遠 陳破空 主持:方菲 【熱點互動】打造「金融
            中心」,北京要拿澳門作秀?相比香港,澳門為什麼這麼「乖」? 主持人:今天是12月18日,
            星期三。就在今天,習近平抵達澳門,開始為期三天的訪問。澳門安保非常嚴厲,據說香港媒體
            的一些記者都被拒絕入境。那麼外媒報導,中共想要給澳門更多的優惠政策,把澳門打造成
            一個金融中心。不過習近平訪澳前夕,國際評級機構「惠譽國際」(Fitch Group)把澳門的
            評級調降為負面。那麼中共的優惠政策能不能把澳門變成香港?澳門是不是一國兩制的成功
            範例? 今晚我們請來兩位嘉賓一起來談一談這些熱點問題,那麼一位是在現場的時事評論員
            唐靖遠先生,唐靖遠先生,您好。 唐靖遠:主持人好,觀眾朋友大家好。 主持人:嗯,好的。
            那麼還有一位是大家熟悉的政論家陳破空先生,不過今天他是通過skype和我們連線,破空
            先生,您好。 陳破空:主持人好,各位觀眾好。 主持人:嗯,好的。好感謝二位,那我們在節目
            開始還是先來看一個背景短片。 (短片播放開始) 澳門回歸20周年將舉行慶祝活動,習近平
            於18日到澳門三天,視察並出席相關活動。澳門全天有直升飛機在上空盤旋,通車不到一星期
            的澳門輕軌氹仔線宣布,18日下午1時起暫停客運服務3天。燃油和瓦斯公司更要求用戶在17日
            前加滿油缸,三天內嚴禁載有易燃物品的車輛在市面上行走,導致加油站出現排隊加油的長龍。
            另外街頭和巴士上到處都有「天眼」監控。 由於香港反送中抗爭持續進行,為了防止香港
            抗議者到澳門,澳門當局對入境者的嚴格審查更是史上首見。而珠海市公安局早前公布,自
            本月10日到22日,在港珠澳大橋東人口島設立安檢站,檢查由香港前往澳門及珠海的人士和
            交通工具。澳門媒體人崔子釗16日向自由亞洲電台表示,他和一些記者同行近日先後受到身分
            不明人士的威脅,個別記者甚至被當局「強制旅遊」。 (播放結束) 主持人:好,觀眾朋友
            歡迎您在節目中間跟我們互動,您可以發手機簡訊,或者在youtube上觀看我們的直播。好的,
            那第一個問題我想先問一下陳破空先生,破空先生就是我們看到說這個新聞中也提到了,習近平
            這一次訪問澳門,澳門的安保可以說是空前的嚴密。那麼就是說港媒有一些記者被拒絕,甚至
            包括馬雲旗下的這個《南華早報》的記者都被拒絕入境。您怎麼看這一次澳門當局這樣一個
            如臨大敵的這樣一個氣氛?為什麼連這個自己人的媒體的記者都被拒絕入境呢? 陳破空:這
            說明中共領導人所到之處都是擾民工程,在內地更是如此,現在又把內地的擾民工程的模式
            搬到了澳門,三步一崗五步一哨。那麼除了表面上大家看到的是,輕軌鐵路停運三天,還有香港
            和澳門之間的客運,就是客船,所謂這個輪渡,由每15分鐘一班,改成每30分鐘,就是取消了
            一半。所以是嚴重的擾民,就這一個象徵性的動作,這個象徵性的意思就是說:中共所到之地
            不是要澳門便利,而是不便利。 就中共所到之地帶給澳門的不是繁榮和穩定,而是帶來了混亂
            和擾亂。所以可以看到澳門市不僅是三步一崗,五步一哨。澳門的警力完全不夠,應該是從
            內地,尤其廣東,尤其珠海,調度了大量的警力,他們穿著便衣,或者穿上了澳門的警察的制服,
            在那裡值勤。 所以這都需要大量的人力、物力、財力,而所謂「天眼」工程這個監控也是
            內地化,這些都是象徵,就是澳門在中共的統治下,變成了不是「一國兩制」,而是「一國一制
            」。中共在宣稱澳門的「一國兩制」成功的時候,在外界看來,尤其在澳門人民的感受看來,
            應該是「一國兩制」的失敗。 國際評級機構惠譽 為何把澳門的評級下調? 主持人:好的,
            確實是,唐靖遠先生就我們看到的說,澳門這個最近確實接連拒絕了不同的人入境,包括前一陣
            香港美國商會的會長早泰娜(Tara Joseph)進澳門的時候也被拒絕入境。所以就是我們看到
            習近平訪問澳門之前,國際評級機構「惠譽」,它把這個澳門的評分從,好像是從正面調到負面。
            這可以說讓中共領導人非常尷尬,您怎麼解讀它(惠譽國際)這樣一個調整的原因,以及它可能
            造成的影響呢? 唐靖遠:其實按照「惠譽」它自己的說法,就是它們這一次把澳門的評級下調,
            原因何在,它在今年9月份的時候曾經也有把香港的那個IDR就是下調。本來香港應該是
            「AA+」,它把香港下調到了「AA」這樣一個級別,就是稍微的往下,作了一個級別。它
            (惠譽國際)說這個原因是一樣的,就是一個原因,就是澳門現在和中國大陸的這種在政治、
            經濟以及金融方面的聯繫是日趨的越來越緊密,那麼就會造成二者之間在這種主權評級上面的
            這種,就是評價的這個指標是日趨同化。 換句話說,其實我們說白了,就是說澳門日益的內地
            化,這個傾向越來越明顯,所以它們認為這樣一個內地化的傾向,其實對澳門的這種就是主權
            信貸的評級是不利的。因為我們看見,其實可以從兩個方面來看啦,站在北京的角度,北京我們
            現在看到是越來越多的在發表這樣的一些。就是這種政策出來,說是要對澳門繼續大力的扶持
            啦,怎麼的啦,要加強對澳門的溝通。 其實它(中共)越這樣做,它其實就是只起到一個結果,
            就是使得澳門加速內地化,使得澳門在粵港澳這個大灣區的異己化,其實也是在加速。這樣做
            其實得到的效果是適得其反,因為站在國際機構的評級來看,它(惠譽國際)就認為你越內地化,
            那麼你的信用級別其實是越低的。 那麼對澳門來說,今年它也還有一個很大的原因,就是它的
            經濟出了問題。因為我們都知道澳門的經濟它其實是高度依賴於那個「博彩業」,就是賭博
            行業。它(澳門)的這個GDP的70%以上都來自於博彩業,就它的經濟結構非常的單一,單一的
            經濟結構就意味著它是比較脆弱的。所以澳門今年前11個月,接著現在12月還沒完。 但是前
            11個月的經濟數據已經出來,它們就在同比同年的比較下,至少是下降了2.4%。而「惠譽」
            的這個評級它們對今年整個全年,就是還有最後的一個月,它們也有一個預估,它們預估這個
            還更嚴重,就是可能會超過,下降會超過2.5%。那麼要站在這個「惠譽」的角度來看,它就會
            認為你的經濟明顯的受到了中國大陸的影響,因為澳門的博彩業它受很大影響,就是跟大陸,
            它最主要的客人的來源是跟大陸有關系,而大陸今年因為跟貿易戰的關係是吧,眾所周知。
            所以經濟嚴重的下行,就明顯的影響到了澳門的經濟,所以澳門經濟的挫折,其實也是導致
            「惠譽」就是把它給下調的主要原因之一。 主持人:是,來賭博的人少,所以某種方面也
            可以說,「惠譽」認為說中國的經濟下行,其實是影響到了澳門。 唐靖遠:對,而且還有一個
            因素就是,「惠譽」評級的這種下調,它直接又影響到澳門的投資前景。因為國際機構這種
            評級,它最大的影響就是對你的整體這個經濟體這個地區的投資風險,和未來經濟的指標,非常
            關鍵的一個指標。它會直接影響到這些投資金的流向,尤其是在歐美這些發達國家,很多它
            (投資基金)還是有一些規定的。 就是那種高質量的這種一些金融基金,它的投資必須得要
            投資到那些,就是評級達到多少多少以上的,你才可以去投資。如果澳門的評級下調,其實這個
            毫無疑問對習近平來說是潑一盆冷水,就是說他(習近平)不是想要建金融中心嗎,這相當於
            就是給你一盆冷水一樣。 澳門具備成為金融中心的條件嗎? 主持人:是,這個是頗具諷刺
            意味啊!那也想請破空先生分析一下,因為我們看到說確實這個像路透社報導說,中共想要把
            這個澳門現在打造成金融中心,並且中共的官員稱,他說之前我們都是把優惠政策留給香港,
            現在我們要分散。所以先請您談談,您覺的為什麼中共現在要發出這樣一個信息,要打造澳門。
            這背後有什麼樣的原因、動機和因素呢? 陳破空:說打造澳門取代香港,或者對香港取而代之,
            實際上第一個層次是北京領導人情緒化的表現,實際上情緒化做國家領導人就是大國領導人,
            往往會帶來敗局。英語有句話叫作Be emotional could be a loser.就你如果太情緒化
            你可能是個失敗者。那麼現在北京領導人做這件事情,就是做給香港看,就是「我就要」、
            「我偏要」、「我非要」,我就不答應你們的五大訴求,我就不要香港雙普選。 你香港說金融
            地位受到影響,我(中共)依賴你外資,依賴你的金融,沒關係,我到澳門去搞。所以這是賭氣,
            這是情緒化的做法,因為接下來是根本不可能的事,澳門的面積是香港的1/4,人口是香港的
            1/7,而它至今的產業非常的單一。要把澳門變成香港曠日持久,恐怕百年都不能夠完成的一個
            工程,所以說的是不實際的事情。 再一個,這是一廂情願,北京的一廂情願。因為香港之所以
            成為國際大都市,擁有高度的關稅特殊地位,或者是金融,或者是轉口的地位是國際上的承認,
            和長期的國際上投資的接納。如果沒有國際上的承認、沒有國際上的這個互動,你根本不可能,
            所以同樣澳門。 澳門你中共想打造什麼,你以為國際上就承認嗎?你把它打造成一國一制跟
            中國內地城市一樣,甚至你把珠海全納進去,珠海納進去跟香港面積一樣大,人口甚至更多,
            只要國際不認你這個帳,你就是一廂情願。 實際上中共在澳門的這個做法,最終會歸建到砸錢,
            就是跟一帶一路或者是跟其他國家砸錢一樣,砸錢在目前中共這一屆政府都失敗了。一帶一路
            是處處失敗,那就不重複了,那麼就是在香港砸錢都失敗了,在香港最早搞了一個經貿安排。
            但是不僅沒有促進香港的經濟發展,反而促進了香港經濟走低、貧富分化、然後是扶持到了
            這個官商階層、官商勾結,讓升斗小民苦不堪言。所以香港這個民生問題和經濟下滑的問題,
            反而成了關鍵。 同樣中共試圖跟台灣建立某種所謂ECFA(《海峽兩岸服務貿易協議》)的
            這些經貿關係,也都是對台灣經濟帶來的危害,就中共的錢、撒錢所到之處都是失敗,就說它們
            一直撒錢給北朝鮮,最後陷入了一片赤貧。然後它們撒錢給非洲、撒錢給中東,沒有一個國家
            富起來,全都是倒楣。 所以說現在在澳門最後是想撒錢,不僅不會成功反而是個失敗,就多年
            之後驗證呢可能是成為現任領導人又一個失敗工程。從一帶一路到廁所革命到澳門,這個賭氣
            最後就恐怕還是一個⋯⋯就是『把錢砸進水裡,冒個泡都不冒』,最後是得個負分。 主持人:嗯,
            說到賭氣啊,唐靖遠先生確實有不少人認為說中共這樣一個舉動,可能某種意義上是用來懲罰
            香港,來獎勵澳門。所以一個請您也補充一下,您覺的它這樣做的背後出於什麼樣的用意?另外
            一個到底這個中共所謂的優惠政策,有沒有可能把澳門打造成一個金融中心? 唐靖遠:首先
            我覺的其實習近平的這一個動作呢,它的政治意義遠遠大於它的實際意義,因為首先呢我覺的
            在整個中共高層他們在醞釀這件事情的時候,它有一個巨大的盲點。我覺的他們出現了一個
            就是思維的一個思路的錯位,為什麼這麼說呢,什麼意思呢?就說我們看見整個高層在就是說
            澳門要建這個金融中心這個問題上,他們是有一個思維的模式,就是它其實是採取了之前就是
            國內要建一個什麼開發區⋯⋯。 主持人:對。 唐靖遠:像當年鄧小平圈點了什麼深圳要建一個
            經濟特區,它完全就是這樣的一種思路,這種思路是什麼意思呢?就是由政府高投入,政策的
            這種傾斜,強制性地、用政府的這種政策性的力量,就是強制性地建立起來、堆積起來這麼一個
            經濟的特區,堆積出來一個的經濟發展。 但是它就帶來一個巨大的問題就是,你政府投入得
            越多,其實就往往意味著政府的干預是越來越多的。甚至是很多最重要的東西,都是由政府來
            進行主導的,那麼你去投資你通過這樣的模式,你可能會推積出來一個經濟開發區,這個好像是
            沒有什麼問題。 但是對一個國際金融中心來說,可能是恰恰相反。因為我們知道就是金融中心
            你要想建成,金融中心它必須要滿足這個幾大基本的條件,首先是資本的自由的流動、信息的
            這個完全的開放和自由的流動,以及人才的流動還有完善的這種法治,獨立、透明的這種
            法治的這種體系等等。所有這一切都是它要成立的一個前提,就是政府的干預要越來越少
            。 主持人:反而是矛盾的。 唐靖遠:對,它必須是建立在市場經濟這樣一個完全自由化的一個
            背景之上的。那麼你看這不就是完全是南轅北轍嗎?你政府越來越投入干預越來越多,像剛才
            我們舉的那個例子,提到那個匯率的評級一樣的,你投入越多可能你評級打得越低。最後你是
            什麼都撈不到,你完全是相反的,所以我覺得這個就是它(中共)一個思維的錯位。 另外一個
            剛才我們也提到,從澳門的現實的這種情況來看是吧,你要建成一個金融中心,你至少是要滿足
            這麼幾大條件。首先是你的硬件,就是你在交通、這個互聯網這些基礎的建設之上,你能不能
            達到能夠支撐起一個龐大的世界級的金融中心,這樣一個程度。那個就涉及到一些土地、人口、
            你的經濟總量⋯⋯很多因素在裡面,這個是硬件。 那麼還有一些軟件,就剛才我們說的,就是
            比如說你涉及到就是資本的自由流動、貨幣的這種自由的兌換以及這個信息的高度的開放是吧
            ?包括人才,你這個地方的生活環境怎麼樣?能不能夠留住這些人才到這來長期的定居啊、生活
            啊! 這些可以說屬於軟件是吧,這些內容你把它跟澳門的現狀進行個對比,你會發現澳門這
            四大因素幾乎是一條都不占。硬件的東西我們覺的,比如說通過中央政府的大力投入,你可以
            把這一部分給它彌補起來。 主持人:您是指土地嗎? 唐靖遠:對,就像這個土地啊,還有基礎
            的設施、建設啊,包括這些東西我覺得是可以的。但是軟件這個東西,至少澳門現在是基本不
            具備,或者說是有些它雖然具備一部分,但是是非常欠缺的;就說還不夠完全的成熟。那麼在
            這樣一個的基礎之上,他(習近平)要想把澳門建立成金融中心來取代香港,這個其實是一個
            笑話,我覺得是不可能的事情。 我覺得其實習近平他自己心裡頭應該還是有一個底盤的,就說
            他可能要想取代香港的可能是不太現實。但他為什麼還要這樣做,我覺得可能有一個主要的
            原因就是,他真正的目的就是分散風險。 主持人:嗯。 唐靖遠:他(習近平)也沒有指望說是
            澳門能夠取代香港,但是呢,他可能必須得要為萬一香港出現最懷的情況,因為我們都知道有
            那個《香港人權與民主法案》在那,就像頭上懸了一把刀,是吧?!未來發生一個什麼樣的狀況,
            他心裡是沒底的。 所以他就是有一種思維:不能把所有的雞蛋都放在一個籃子裡,我現在要把
            它給分開,深圳放一部分或者說澳門放一部分。我覺得他可能有這個意圖在裡邊,對。 主持人
            :嗯,是。那破空先生也請您再展開談一談就是澳門到底有沒有可能成為金融中心,且不說它
            代替香港。另外就是說中共它特別是現在的高層,它一路以來一直引用這樣的思維,就是說
            「雄安」也好,「深圳」也好,「上海」也好,「海南」現在又是「澳門」,一直以來並沒有
            太多的成色,但它一直要這麼去做,您覺得它背後是不是有什麼樣的政治和經濟壓力呢
            ? 陳破空:對,這屆政府我們看了所謂「雄安特區」也好,「上海自貿區」也好還是「海南島
            自貿區」,實際上最後都是虎頭蛇尾,甚至不了了之。原因就是顧慮重重,政治上顧慮重重,
            深怕衝擊到一黨專政,它跟上個世紀八九十年代的開放,八十年的開放完全不同。 八十年代的
            胡耀邦、趙紫陽主政時期,說開放就開放,動作非常雷厲風行。比如說依靠香港建立一個經濟
            特區「深圳」,依靠澳門建立一個經濟特區「珠海」,後來又擴大建立了兩個經濟特區,「汕頭
            」或者「海南」都是雷厲風行。馬上就做、說到做到,而且是立竿見影,效果就立即出來了
            ! 到了現在這個政府可以說是相當的保守,一方面還羨慕過去的成就,還躺在過去的功勞。
            躺在前人的功勞簿上,但另一方面又裹足不前,在政治上顧慮重重。所以現在說到澳門,最後
            我相信最後也是一個不了了之、虎頭蛇尾的事情。 而且中共如果真正要在香港大動干戈的話,
            帶來深重的腐敗,因為澳門本來已經是一個賭場、是一個博彩業,現在主要的客戶是中國內地
            的,而中國內地又以官員和商人為主。那麼如果再在那裡大量投資的話,澳門本來是葡萄牙的
            法律體系,那麼現在不管是人大的栗戰書還是現在領導人習近平,都宣稱好像澳門的「一國
            兩制」成功。 意思就是說按照共產黨的模式,聽黨的話成功,沒有抗議遊行示威,這實際上是
            「一國兩制」的失敗和悲哀。在這樣的情況下,那麼將來的法律體系可能會受到侵蝕,一旦投資
            一到,那到處都是伸手高級官員,那嚴重的腐敗就會氾濫。最後澳門變成可能是真正是個臭港
            或者是腐敗大港。 我們想想在美國,誰能夠想到說要把拉斯維加斯從一個賭城,突然打造成
            金融中心,沒人有這個發瘋的念頭。那麼同樣這個紐約是一個巨大的金融中心和國際轉運中心,
            也沒有說突然把紐約變成另外一個性質。 這就是它各自有各自的來源和基礎,這個中共的
            賭氣賭到這個什麼地步呢?領導人賭氣到就說:你以為我離了香港就下不了鍋了?就吃不了飯
            了?我就偏不!寧願我不服從香港的要求,我寧願不給你雙普選,我就另起爐灶。 巨大的人力
            、物力、財力去另起爐灶,然後若干年之後來看兩頭都失敗了。一個是香港也失敗了,在澳門
            也失敗了,今天這些短視的、情緒化的領導人所布的局,可以說這個未來的途徑已經很清楚了
            。 相較香港,澳門為什麼一直比較「乖」? 主持人:嗯,是。不過唐靖遠先生,相比香港而言,
            澳門確實是屬於好像是比較乖,比較溫和的,一直沒有什麼大的動盪。澳門的議員呢,他也說,
            他說澳門人對於民主和普選的訴求,不如香港人那麼強烈。在您看來為什麼就是說比較香港,
            澳門是這樣一種比較溫和、比較乖一直是這樣的一種狀況呢? 唐靖遠:我覺得它最主要是涉及
            到兩方面的原因:一方面的原因就是屬於歷史上的原因,其實中共早在文革那個時期開始,對
            澳門其實就已經有很深度的滲透,在文革1966年的時候,曾經澳門爆發過一次暴動,其實很有名
            的,歷史上叫作「123暴動」,它在12月3日這天發生的。 這個暴動其實說起來挺複雜,不過
            我們簡單一點說,其實就是澳門底層的這些勞工,他們為了子女讀書的一些權益,權利問題和
            當時葡奧當局發生了一些衝突,但在這個衝突的過程中,中共那時候已經很多勢力滲透到民間
            的一些組織,什麼商會、工聯、學聯、青聯、婦聯,反正很多民間組織,其實都是中共這種紅色
            勢力在控制著,它們就加入進去。加入進去之後就把這個衝突就鬧得很大,最後演變成一場
            大規模的暴力衝突,有很多人死傷。 最後衝突的結果是葡澳當局最後做了讓步,做了讓步結果
            就導致了一個非常不好的結果,就是在那個時候,其實整個澳門,尤其是民間社會,實質上它的
            控制權,已經被掌握在這些中共操縱的這些所謂的民間組織,民間團體的手中。 主持人:好像
            把一些臺灣(中華民國)的勢力趕走。 唐靖遠:對!那個時候它(中共)不就一句話嗎?說澳門
            已經成為半個解放區。意思就是說,它把大量的親共人士都扶植上位,把親中華國民國的,很多
            以前臺灣在那邊留下來的很多人全部都清除出去了,所以這樣導致成一個結果,澳門其實在那個
            時候起,就已經可以說是深度地被這種紅色染紅,紅色勢力所染紅。 到了主權移交以後,又
            經歷了20年,這種滲透和這種控制其實是更嚴格的,更多的。所以很多東西其實澳門已經,包括
            澳門從上面整個政權的機構,我們看到最近還有新聞曝光出來,中共在澳門主權移交之前好
            幾年,8年還是9年的時候,就已經有派遣了大批的官員,一部分官員就到澳門去,表面上說是
            協助移交順利,其實它(中共)就已經占據到政府管制系統的一些關鍵的位置上面。 所以這樣
            造成一個局面,整個澳門政治的氛圍從政府到民間這種政治氛圍,它其實跟香港是完全不同的
            一種生態,這是歷史原因。 那麼還有一個現實的原因就是跟基本法有關係,因為我們知道澳門
            的基本法,它其實基本上是照抄香港基本法,最主要的那些條款基本是照抄,但是唯獨有一個
            重要的東西它沒有抄過去,遺漏掉了,就是在香港的基本法裡面是明確的,明文寫的規定:香港
            人可以逐步地實現雙普選。就是特首和立法會的雙普選,但是澳門基本法在抄的時候就沒有
            這部分。 換句話說從基本法的字面上,至少中共沒有給你(澳門)這個承諾,沒有承諾澳門給
            你雙普選,所以如果澳門的民眾想像香港人這樣來爭取普選,或爭取一個民主的權利,中共知道
            在表面上它可以有一個冠冕堂皇的一個理由:我(中共)當初就沒有答應要給你,所以你這算是
            一種額外的要求。 這個跟香港不一樣,是吧?香港民眾出來抗爭是因為你當初答應了,而且是
            白紙黑字寫進了基本法的,所以我希望你能夠兌現你的諾言,所以從道義上,道理上,中共輸
            道理,跟澳門在這一點上情況是不一樣的,所以我覺得主要是基於這兩個原因,會出現我們看到
            的這種情況。 澳門現在是「一國兩制」嗎? 主持人:我想問一下破空先生,我們知道澳門的
            政府其實是比較配合的。像唐靖遠先生剛剛說,它好像十年前就已經引進國安法,所謂的23條,
            所以已經實行10年了。對於中共來講,它就會覺得你看這個也沒什麼問題,23條在澳門實行了
            還是這麼平靜。所以這一次基本上不管從習近平還是從官媒都稱讚澳門說是「一國兩制」的
            典範,顯示「一國兩制」的活力,這方面您怎麼看呢? 陳破空:澳門之所以有這個現狀,令中共
            很滿意,覺得有一個網路上的說法叫『乖寶寶』,這個說法有歷史的成因和現實的成因。歷史
            上來看,因為澳門和香港相比,它非常單一結構,它就是一個賭城,一個博彩業,它不像香港,
            香港是一個綜合性的國際大都市,除了它有強勁的經濟、貿易、金融中心這些以外,它還有很多
            的大學、學術機構還有各種政治、文化深層次的一些聯繫。 像香港這些大學,香港大學、
            香港中文大學,有很多的學術成果,科研成果和這些國際交流,但是在澳門,像澳門大學幾乎就
            沒有什麼國際聲望,交流也非常單一。 而澳門的居民基本上就大多數的就業都依附於博彩業,
            這個博彩業說起來是比較俗的,登不上大雅之堂,就業的人也就是為了一個生計,澳門就是要麼
            一個是博彩業,再一個是依賴於博彩業,維持生計而已,也就是說主要就是一個生活。 澳門
            我們看到不僅博彩業,還有澳門賭王叫何鴻燊,他有四位太太甚至更多,什麼姨太太,這都是
            可以看到,從某種意義上講一種腐朽的、沒落的、墮落的一種生態和生活方式。 所以這個跟
            香港完全不能相比,香港就是完全是可以跟紐約,跟倫敦,跟巴黎,跟這些國際大都市相提並論
            的一個頂尖的國際大都市,整個世界都可以說嚮往的,所以叫「東方之珠」,叫「亞洲四小龍」
            ,澳門跟香港來比連腳趾頭都比不上,所以回頭來看現在的成因,除了剛才唐先生提到的一些
            成因之外,中共覺得澳門是太容易控制了,同時也生出了大量的這些它自己的觸角,因為人口少
            。 而且澳門這一次,剛才在開始的時候,主持人提了問題忘了回答,說拒絕香港的媒體入境
            或者記者,還包括《南華早報》,為什麼會這樣呢?我想中共可能有兩個用意,把《南華早報》
            也列為被禁之列,《南華早報》本來已經現在被馬雲阿里巴巴所收購,馬雲應該是共產黨員,
            應該屬於中共的體系了,但是一方面它的意圖要假裝,裝作沒有給《南華早報》特殊待遇,免得
            被說是中共媒體,還繼續掩護《南華早報》。 但另外一點,南華早報不見得屬於在中共黨內的
            ,不見得屬於習近平體系,屬於另外的派系,也就是說派系鬥爭可能體現在澳門中,有可能習近平
            到達澳門之後,把《南華早報》排斥在外,也有可能是中共的派系鬥爭也延伸到了澳門。 事實
            上去年10月份的時候,中共駐澳門的中聯辦主任最高的首長中央委員鄭曉松突然墜樓身亡,而且
            中共立即宣布他是憂鬱症,立即就派了工作組去處理,連警方保留現場,保留屍體或者破案這些
            程序都省了。說明內部的政治鬥爭延伸到了澳門,慘烈的程度以至於有人被跳樓、被墜樓、
            被身亡。所以中共對澳門是鐵腕緊緊抓住。但是回頭來看,中共所說的澳門,它很滿意是成功
            模式,意思就是說你們要當奴才,你們要當太監,你們要當乖寶寶,這就是成功,聽黨話,跟黨走
            就是成功。 中共自己定義了一個成功的標準,當這個標準放到國際上的時候,就完全相反,跟
            整個國際社會,跟時代格格不入,既違背世界前進的步伐,又跟國際文明世界準則相違背,也就
            註定了它想把澳門變成所謂的金融中心或者國際大都會,這種努力將會失敗。 因為它在價值
            上,在政治上,在法治上絕對會跟國際相牴觸,沒有任何的外資、外國企業或者跨國企業或者
            其它國家,尤其西方國家會來青睞澳門,響應中共的號召跑到那裡投資,所以中共最終都是
            自說自話一廂情願,最終這一切都會歸於失敗,歸於泡影。 主持人:唐靖遠先生也請您展開來
            談一談,我的問題是因為中共說澳門是「一國兩制」的範例。但是現在澳門到底還算不算
            「一國兩制」?您怎麼看中共這個說法,說澳門是「一國兩制」的範例? 唐靖遠:首先第一個
            問題我覺的,我特意去看了新華社發表一篇社評,說澳門是一國兩制的成功範例,偉大實踐的
            非凡意義如何,這篇文章裡面很長,但是我看它的核心內容就只有三條列出來,為什麼說澳門
            是成功的,第一條是說澳門的GDP增長了很多,第二條是說澳門政府的外匯儲備和它的政府財政
            的結餘也是有大幅的增長,第三就是指著澳門的居民個人收入,每個月的平均月收入也是增長
            了不少,而且失業率有所下降。你會發現中共官方媒體黨媒,最高級別他們羅列出來的為什麼
            說澳門成功這三條理由,其實我覺的合起來可以說一句話,就是「錢包鼓」了⋯⋯ 主持人:物質
            生活。 唐靖遠:就是政府的錢包「鼓」了一些,這個民眾的錢包也「鼓」了一些,這個就是它
            唯一能拿得出手的一個理由。但是我們看到的澳門,它實質上錢包是鼓了,但是我們如果說回到
            就這個「一國兩制」它的本來的定義。「一個兩制」本來的定義是說資本主義制度和這種生活
            方式,在同樣一個國家之內,它是不變的。 那麼資本主義的這種制度和它的生活方式它的涵義
            就很廣了。它涵蓋了很多的公民基本的權利啊、人權啊,以及這種透明獨立的法制的體系啦。
            還有就是很多相應的就是這種狀態生活下的那種氛圍,以及這種生活的方式。它其實全都沒有
            啦。 其實換句話說,中共相當於給了你一把錢,然後換走了你的人權,換走了澳門人幾乎所有
            的人權。它其實就是這麼一個過程。而且我們還可以看到,澳門所謂的錢包鼓了,它(中共)
            特意列舉的是從1999年以後。那麼也就是從1999年以後澳門富裕的這個過程。其實它正好
            和中共整個大陸,在入世以後發生了這種經濟。 這段時間大概就是二十年時間,經濟的一個
            快速暴富的一個過程是同步的。換句話說呢,澳門這所謂的錢包鼓了,它其實只不過是中共大陸
            在這一段經濟暴富的過程中,分了一杯羹的結果。換句話說,它也是就是中共這個中央嘛,對
            澳門給了一些政策的傾斜,有意識地就是給你一些紅利。 那麼我們借用一個過去大家經常來
            說的一句話,就是那個「胡蘿蔔大棒」。換句話說其實是它(中共)給了一些胡蘿蔔,在需要你
            的時候給了你一些胡蘿蔔。但是如果將來它(中共)不需要的時候,它可能會變成大棒。它其實
            就是這麼一個關係。 那個你剛才提到的第二個問題就是說,澳門它究竟是不是一個真正意義上
            的「一國二制」?其實我覺得澳門現在可以說事實上已經是一國一制了,為什麼呢?因為我們
            看看澳門現在的社會現狀,首先第一個澳門這種公民權利的倒退是非常顯著的。因為澳門至少
            我們看到現在通過了二個法案,一個是《維護國家安全法》,相當於是澳門版的那個
            《二十三條》。 主持人:對,這個十年前好像就聽過。 唐靖遠:對,在2009年就已經通過的。
            最近馬上要通過是《網路安全法》,就這個《網路安全法》呢,它和大陸其實就是同步的。就是
            你要使用手機必需要實名,實名才能夠上網。那麼第二個就是,我們看見澳門它其實已經無形
            開始成為一個警察社會,澳門已經建立了一個祕密警察制度。同時剛才陳先生有提到,它那個
            天眼監控系統。這個系統據說在2028年預計,現在這個天眼系統已經覆蓋澳門最主要的大部分
            地區。它們預計到2028年要覆蓋整個澳門所有的地區,無死角地全監控。 那麼第三個方面,
            澳門這種民生的生態,尤其是在教育界。澳門現在已經有大概70%的中小學,都是採用大陸的
            教科書。由其是歷史教材和所謂的這個什麼政治思想、品德那些教材,都是採用大陸的課本。
            它其實就是對它進行這種紅色的洗腦,而且這些教科書裡面,它首先舉個簡單的例子。它對
            文革是進行粉飾美化的,把文革說成是共產黨的⋯⋯ 主持人:艱辛探索。 唐靖遠:為了探索特色
            的社會主義制度的艱辛付出。然後呢,對「六四」這樣的事情是隻字不提的。所以呢,你就可以
            看到它(中共)已經有意識地在文化上,在整個的、就是對澳門人進行這種洗腦。那麼文化上面
            的表現就是我們可以把它叫作文化上北京希望表現得更突出。現在的澳門人,他們這個聯繫
            朋友啊,直接通過手機聯繫,他們是使用什麼?他們是使用微信;他們接受資訊是使用微博;看
            電視看的全是幾乎都是大陸的那個電視台。 主持人:基本上跟大陸沒什麼區別了。 唐靖遠:
            對,所以你就可以看到澳門人現在實際的生活狀態,在二十年的這種溫水煮青蛙的過程中,
            它已經實質上和大陸基本沒什麼區別,高度的內地化了可以這麼說。所以你從這個角度上講,
            它所謂的「一個兩制」,只不過是一張皮,一個名義上的一個東西。它實質上我覺得基本上就
            已經是「一國一制」這樣的情況。 主持人:實際上,我覺得澳門在回歸之前跟香港也不太一樣,
            香港可以說是真正的資本主義制度,澳門可能起點就比香港低很多。所以像您剛才說的,它回歸
            之前就已經是半個解放區了,所以在回歸之前都已經談不上是「一國兩制」了。更不要提回歸
            以後。 習近平見林鄭老調重彈? 破空先生,大家現在大家關注的就是澳門和香港的對比,中共
            想要把澳門打造成金融中心。也是對香港的一種懲罰也好,或者是怎麼也好。那我們看到最近
            就是林鄭月娥她去北京又見了習近平。 見面中,習近平又再度肯定了林鄭的這樣一個什麼
            擔當喔。而且又把這個三條什麼堅定支持又提了一下。您覺得這一次見面,對於香港發出什麼
            信息?您怎麼解讀這一次見面,它是一種就是北京有什麼新的政策,或者是新的態度,還是說是
            老調重彈? 陳破空:現在的領導人都非常的僵化、非常的保守,可以說是所謂改革開放來僅見
            。所以這個姿態是跟香港民意對著幹。就是說不管是林鄭月娥,還是另外一個律政司司長
            鄭若驊。這些人在香港已經喪盡民心,都是過街老鼠,人人喊打。但是中共領導人還是力挺,
            不僅是跟香港民意對著幹,其實跟林鄭月娥本身的意志也對著幹。 因為林鄭月娥在路透社
            兩次洩露出來的錄音談話,她要有選擇的話她根本就可以辭職,她根本不想幹。因為她覺得自己
            犯了天大的罪,她請求饒恕。因為她畢竟還是一個天主教徒,不管有多真誠或者多不真誠。
            另外她承認給香港帶來了災難,所以她自己驚恐萬狀,然後是中共槍桿子頂住她,繼續幹下去。
            也就是說做一個香港特首很悲哀,政治上本來已經是儡傀了,但是連辭職的自由都沒有。 她
            就說我如果有選擇的話,我寧願怎麼怎麼樣,但是她卻沒有選擇。因為她是地下黨員要服從黨的
            組織紀律。同樣的鄭若驊這個律政司長本來要留在倫敦,就不回來了。也被北京勒令回去,而且
            回去是先到北京軟禁了一段時間再放回香港。所以她(鄭若驊)回到香港的時間,她不是去官邸
            辦公,她在自家自租的地方去辦公,都顯示她根本都不想幹,但是連辭職的自由都沒有。 這個
            世界上任何一個國家和地區,正常國家、民主國家如果出了這麼大的事情,一定有官員引咎
            辭職,也會有上面中央政府去問責。但是中共這個操作是完全相反,就比方說跟香港的民意
            對著幹。 當然這次習近平和李克強會見林鄭月娥,表現不同的調子。習近平強調的是嚴正支持
            警方,嚴正執法。雖然說話有氣無力,就那一句話顯得有一點力度。那麼李克強強調的是維護
            香港的長期繁榮穩定;習近平強調的是過去一年這個香港多麼的複雜、困難,支持林鄭月娥
            怎麼樣的克盡職責。 但是李克強表達,在經濟上、在未來的作為做抒困,這個叫作救企業,
            救失業這方面,所以高層領導人的分歧已經表現出來,就說習近平所持的強硬路線、極左路線,
            和李克強所持的相對開明、和溫和的路線也是一個對照。所以說林鄭月娥恐怕也會無所適從,
            究竟聽誰的? 主持人:那麼唐靖遠先生您覺得這樣一次會面,對於香港未來的局勢發出什麼樣
            的信息呢? 唐靖遠:我覺的首先第一個林鄭月娥對她這個未來,她可能將來想要像過去那樣
            採取非常強硬的、高壓的、暴力的這種方式,來解決的這種難度會更大。因為首先第一個,
            我們可以看到明顯的香港這個抗爭已經長期化了。 我相信中共高層已經意識到這個問題,其實
            習近平主動提出來要把澳門建成金融中心。這背後本身就代表他已經意識到,香港問題可能
            不是說在短期之內就能夠解決的。因為如果香港很快就能夠解決,他有這樣一個判斷,他就
            沒有必要費這麼大的勁,把精力、錢投入到澳門上面去了,這是第一個。 那麼既然香港這種
            抗爭變成長期化,就意味著林鄭月娥很難採取這種急風暴雨的方式來結束這個局面。 那
            第二個呢,就是還有一個外部因素。就是我們看到美國《香港人權法案》的通過,這個法案通過
            以後,它確確實實起到一個緊箍咒的作用。因為習近平我覺得他還是比較在乎。至少目前他
            還是不想因為香港局勢的惡化,導致這個法案被實施。 所以這個其實無形中對林鄭月娥也會
            形成一個制約,就是如果說習近平,不想香港被幹掉。那林鄭月娥你要是捅了簍子,把這個事情
            ,要是這個法案給實施的話,惡化的話。那這個責任可能將來追究起來,她可能承擔吃不了
            兜著走。 那麼最後還有一點,林鄭月娥她還面臨了一個巨大的挑戰,就是因為今年這個區選,
            區議會選舉大敗。她其實是要承擔大部分責任的,而且她還面臨明年那個立法會的選舉。那麼
            立法會選舉她能不能夠扳回局面,這個可能是習近平給她最後的一關考驗。所以她最主要的
            精力可能我覺得會放在那個上去。 主持人:所以其實也反映出了在香港這個局勢的處理上,
            中共還是處於兩難局面,並沒有一個好的辦法。 唐靖遠:對的。 主持人:好的,非常感謝二位
            。那今天節目時間很快就要到了,我們也感謝觀眾朋友的收看,我們還是下次節目再見。
            '''
        ),
    )
    assert parsed_news.category == '熱點互動'
    assert parsed_news.company_id == company_id
    assert parsed_news.timestamp == 1576684800
    assert parsed_news.reporter is None
    assert parsed_news.title == '打造金融中心 北京拿澳門作秀?'
    assert parsed_news.url_pattern == '19-12-19-11733936'