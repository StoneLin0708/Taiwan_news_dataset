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
    url = r'https://www.epochtimes.com/b5/19/11/2/n11629034.htm'
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
            家屬作說客 看守所其實離城不遠,只是被幾家飯店、一片樹影輕輕遮住,尋常無從得見。走過
            一段荒僻的馬路,到處鹽鹼斑駁,野草叢生,真的有高牆電網,哨兵崗樓,一如傳說中的樣子。
            剛剛經過紅塵萬丈,繁花似錦,驟然見此,心中怔忡,如進夢中。 最初的日子,親友可以隨意
            進出,法輪功學員們則被分別關在一排辦公室。我幾乎日日前去探視,見了我家先生卻也並無
            多話,心比石堅,何用再說。 城裡的學員俱是故友,從鄉鎮押來的幾位年輕女子,身姿婀娜,
            氣質如蘭,那種內在的明澈與乾淨,讓人一見難忘。印象最深的一位名叫秀葉,口角含笑,鎮靜
            自若。「車禍讓我在床上躺了整整三年,是法輪功救了我。大恩不言謝,讓我說師父的壞話,
            打死不能。」「別死心眼,你兒子有病,又快高考了,只要寫個不修煉的保證書,立馬放你回去
            。」「這不好吧?有一說一,有二說二,隨便撒謊,我可做不來」。秀葉慢聲細語,卻堅不鬆口
            。警察再三努力之後,只好搖頭而去。 一撥又一撥家屬、朋友、同事、同學,像浪潮一樣湧來
            ,官府動用了法輪功學員幾乎所有的人脈,像大江大河中的漩渦,喧囂四起,浪花飛濺。或苦口
            婆心,或憤然呵責,有的掩淚而別,有的不屑而去。這些死硬的法輪功修煉人,像海邊的礁石,
            任憑風高浪急,潮起潮落,兀自挺立,由世人評說。 兒子悄悄把我拉到一邊,竊竊私語:「媽媽
            ,警察叔叔給我棒棒糖吃了。」「奥?!」「叔叔還問我,誰和爸爸一起商量煉功上訪的事?」
            「那你說啥了?」我一把抓住兒子的肩頭。「媽!」兒子抗議地掙出身子:「我又不傻。我一邊
            吃棒棒糖,給他說,我啥也不知道,啥也沒聽說。」「好!好!」我激賞地擰了一下兒子的臉,
            心裡兀自驕傲,不愧是我的兒子,有種!」 天天出入,家屬們慢慢熟識了,經常溝通消息。一個
            個憂心忡忡,強打精神。不知道這樣彼此對峙,堅守不退,日後會是一個什麼結局。 先生被
            丟入牢房 終於,官府耗盡了最後一點耐心。將法輪功學員全部關入號子。就像每個蜂群都
            供奉著一個蜂王,高高在上,不事生產,每間號子都有牢頭獄霸,叱吒風雲,號令上下。多是江湖
            綠林出身,凶神惡煞之輩。每個人初進牢房,必定一群人一擁而上,拳腳侍候,打個七暈八素,
            倒地不起。城裡人往往手無縛雞之力,人為刀俎,我為魚肉,一旦進入,任憑收拾,更何況打不
            還手,罵不還口的法輪功學員,簡直羊入虎口,受盡蹂躪。 那年冬天,滴水成冰。我家先生被
            剃成光體,聳肩縮背,面如土色。我見了,心頭大震,半晌無語。只好輾轉托了熟人,送了幾次
            饅頭,幾袋包子。聽說,牢裡的伙食極其惡劣,一天就給小孩拳頭大的兩個饅頭。 就算這樣,
            因為家在城裡,早晚有人照顧,先生的情況遠不是最糟糕的。秀葉既城裡無人,又家境清寒,
            更是吃盡苦頭。數九寒天,朔風凜冽,警察在她的個人牢房裡灌滿涼水,不給棉衣被褥。白天,
            一地是冰,夜裡蜷縮在冰冷的水泥台子上。牢門之外,有人時時盯著,一想打坐煉功,輒被拳打
            腳踢。一個月過去,終於舊病復發,不能直立。只好手足並用,在牢裡爬行。 等先生拘留期滿
            ,一個月後回家。左肋時時作痛,不小心碰到,就疼得吸氣。「怎麼了?」先生不願細談,只說「
            應該是斷了一根肋骨,讓號裡人打的。牢頭叫劉剛,出了名的混混。刑警隊的大隊長專門安排
            我去那裡。」我能說什麼?嘆氣而已。 幾進幾出,軟禁、拘留,居然成為常態。早就聽老輩人
            說過,四九年以後,凡是信佛信道,講究什麼積德行善,屢教不改者,抓進大獄,誰也別想活著
            回來,罪名叫「反革命會道門」。當時聽了,不以為意,還開玩笑說,人爭一口氣,佛爭一炷香,
            難道西方的馬恩列斯為爭王道,一定要對儒釋道古風施以鐵拳? 三十出頭的先生形如槁木 一
            個月明星稀之夜,先生被鐐銬加身,從家裡被一群公安帶走,送進了淄博王村,山東第二勞教所
            。 時隔一月,公公去世,先生都沒能回家送終。等夫婦相見,可憐公公的墳上已是草色青青,
            天人分隔,再回首已是百年。 隔窗相見,才三十出頭的先生已形如槁木,彷彿喬木被火,觸目
            皆是焦煙。先生更沉默了,吶吶不能成言,雙目失焦,如古井不波。整個身子都佝僂著,瘦得
            脫了形。 乍見了泥塑木雕般的先生,心中的沉重猶如巨石壓頂,不知道他在牢獄之內經歷了
            什麼,數月之間竟成如此模樣。相見時難別也難,臨行幾度回首。嘆先生原是家中獨子,天性
            清高,如今明珠蒙塵,任人踐踏。 而今,漫天風雨,我唯有成為一棵大樹,屹立不倒,極力伸出
            枝椏,護衛家中方寸之地。遙想九百年前,岳母帶著幼子,坐在簸籮裡,在天地一色的大水中
            漂流,不也是四顧茫茫,生死未卜?忠臣之後,自有龍天眷顧。相信一切都將過去,終會還我朗朗
            乾坤,青天白日。 一月一探監,每週一封信,人在囹圄中,家書抵萬金,每次,都寫上厚厚一沓
            。深夜孤燈,孩子已經熟睡,幾次淚下,點點滴滴總把信紙洇透,卻不敢嗚咽出聲。 這就是我們
            的祖國嗎? 輾轉傳來消息,濟南那家書店的女老闆,早被勞教。替我扛麻袋的劉建,那個人高
            馬大的小伙子,被關進一個小小的鐵籠子,酷刑之下,數月殞命。 死!劉建?那個憨厚的,強壯
            的小伙子?他扛著麻袋,穩健如山的影子,彷彿就在眼前。我無法想像那麼一個山東大漢,居然
            被塞進狗籠子裡。 這個可怕的消息,鬼魅一般,緊緊掐住我的咽喉,讓我胸口憋悶,無法呼吸
            。 我不相信!我不相信!我真的不敢相信!為什麼?為什麼呀? 沉痛的心境,日甚一日,憤懣和
            絕望堆積如山,終於使我下肢沉重,不良於行,得雙手撐住桌子,才能慢慢站直。 我不再出門
            。這個世界上,已經沒有了可以行走的路。沒有王法,沒有曲直,只有不由分說的強權。你上訪
            ,你爭執,就會鐐銬加身,大獄侍候。你死了,你斷了骨頭,你椎心泣血,你呼天搶地。長夜如死
            ,鐵幕沉沉,讓你發不出哪怕一絲一毫的聲音。 人如草芥,命如螻蟻。 祖國啊,祖國!這就是
            我們心心念念,立志為之奮鬥的祖國嗎? 我發誓,從此之後,我再也不會為這片土地唱什麼
            讚歌!
            '''
        ),
    )
    assert parsed_news.category == '美國,舊金山,灣區廣角,文化腳步'
    assert parsed_news.company_id == company_id
    assert parsed_news.timestamp == 1572624000
    assert parsed_news.reporter is None
    assert parsed_news.title == '紀實散文:一夜驚夢'
    assert parsed_news.url_pattern == '19-11-2-11629034'

    