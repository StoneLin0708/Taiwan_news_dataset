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
    url = r'https://www.epochtimes.com/b5/19/12/16/n11726516.htm'
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
            給孩子餵母乳還是奶粉呢?餵母乳時,寶寶咬奶頭怎麼辦?實際上,奶瓶餵奶不利於寶寶語言
            能力的健康發展,也容易導致牙齒畸形。而且餵母乳時,媽媽應該聽好的音樂,不要胡思亂想
            。 我認為,孩子問題的產生是為了給我們智慧,而不是煩惱,關鍵是大人抱著什麼心態去對待
            這些問題。因為人的身體需要花費很大力氣去處理自己的負面情緒,當負面情緒很多時,當
            父母的就不太可能產生智慧。 寶寶咬媽媽乳頭怎麼辦? 現在很多媽媽都有工作,又想母乳
            餵養孩子,就採用先把奶吸引出來,放到奶瓶裡,需要時餵給孩子。媽媽的乳頭與奶瓶的奶嘴有
            很大差別嗎? 雖然用奶嘴餵奶,孩子也可以訓練吸吮力,但母親的乳頭比較軟,彈性好,而且有
            神經,還有溫度。母親的乳頭是有感情的,給孩子真實的感受。而塑膠的奶頭,不論多昂貴,它
            是沒有生命的,沒有溫度的,形狀是固定的,沒有變化。 嬰兒的成長過程非常迅速,也是孩子一
            生中非常重要的階段。我建議,媽媽生小孩之後最好請3年育兒假,在家裡自己帶孩子,這是用
            多少錢也買不到的經驗。 我在教育學生的時候經常說,母親開始的時候多花些時間,少了後面
            多少的麻煩。 不過,餵寶寶母乳時,有時會用力咬媽媽的乳頭,特別是剛剛出牙的時候,會咬得
            很痛。其實,當寶寶咬媽媽乳頭時,可以輕輕捏寶寶的鼻子,他的嘴就會打開了,不要打孩子。
            要注意的是,輕輕地捏孩子的鼻子,自己可以試試看,如何把握力度,比較順地捏鼻子。 這是一
            個互動的過程,一個多月的孩子已經能夠感受到大人的微笑和情緒。你逗他的時候,他會有
            類似微笑的反應。當他用力咬乳頭的時候,媽媽給他溫柔的刺激,他會懂的。這樣多幾次之後,
            孩子就明白了,懂得如何拿捏吸母奶時的力道。 心平氣和地餵母奶 再提醒母親,餵母奶的
            時候不要胡思亂想。最好是聽著溫柔、祥和的音樂,不要看電視、打電話聊天。還有母親需要
            注意自己的飲食,因為如果吃了辛辣或者味道強烈的食物,你的母奶也會是那種味道,孩子會
            突然被嚇到,不願意吃奶。 人的思想會促使不同的荷爾蒙的產生,當媽媽想緊張的事情時,她
            的腎上腺素就會增加,母奶的味道會變得不好吃。當我們喝飲料時,如果一開始是甜的,喝著
            喝著又變成苦的、辣的,可能馬上想吐出來,不想再喝了。孩子也是這樣,他覺得突然變得不
            好吃了,就會停下來,不再去吃奶了。所以不要誤會孩子,可能是媽媽自己的問題導致孩子不
            吃奶。 孩子吃奶時的吸吮力是孩子健康與否的指標,可以幫助判斷孩子的發育是否達到正常
            水平。 孩子總要有長大的時候,總要有發育語言的時候。當孩子吸吮力足夠的時候,他在吃奶
            時會練習臉頰的肌肉,孩子的發音就容易準確。否則的話,孩子會說得稀裡糊塗、劈裡啪啦的,
            聽不清楚他在說什麼。 孩子吃母奶時,鍛鍊的不只是臉部肌肉,還有舌頭,還有手的抓取力量
            。 有人得了中風,在醫院做復健的時候,醫院給一個比較軟的球,中空的,訓練抓取的力量。
            寶寶在吃奶的時候,一般會用手抓著媽媽的乳房玩,也會鍛煉手的抓取力量。如果,用奶瓶吃奶
            ,孩子抓的是奶瓶,硬硬的,是完全不一樣的感受。 給寶寶刁奶嘴對嗎? 以前老人說不要讓
            孩子總含著媽媽的乳頭,但在西方國家,孩子的奶嘴刁到好幾歲,尿布也戴到好幾歲。很多華人
            覺得這樣做很科學,但也有疑問。 我認為,這樣的作法並不一定好,也不是所有的西方教育家
            都鼓勵這樣的作法。我自己生第一胎的時候,出院前,護士阿姨很好心地為我準備了各種嬰兒
            用品,其中就有奶嘴。 當我把孩子抱回家的時候,孩子肚子餓了。一放下,他就開始哭。我忙
            著整理行李,還沒準備好抱著他餵奶,我就想起護士給了一個奶嘴。我就馬上拿出奶嘴塞到
            孩子的嘴裡,想暫時止住他的哭泣。 沒想到,孩子馬上把奶嘴用力吐了出來。我記得很清楚,
            就像拋物線一樣,飛出來掉在地板上。出生才幾天的嬰兒,就有那麼大的力氣把奶嘴吐出來,
            飛得那麼遠。 我馬上意識到,自己做錯了,那是孩子完全不需要的東西。我馬上向孩子道歉:
            媽媽做錯了,從今天開始,媽媽再也不會把奶嘴塞到你的嘴裡了。不管媽媽有多忙,也不管你
            哭得多麼得讓我受不了,我絕不會再做這件事情。 奶嘴養小孩不是科學方法 這件事情過了
            十幾年後,我和最小的孩子討論的時候說,你真的要謝謝哥哥,當年做了這麼一件事情,所以
            老二和老三都再也沒用過奶嘴。 如果你有一個小兒科牙科的朋友,一般也會建議你能不用就
            不要用塑膠奶嘴,因為經常刁著奶嘴,嬰兒的牙齒會變形。但是因為讓大人的耳根清靜,所以
            很多人還是樂此不疲。 很多大人受不了孩子的哭鬧,塞給他們奶嘴是最快最省事的方法。
            教育專家、兒科牙醫都不認為這是科學的方法。 我在台北的鄰居,是一位非常好的退休老師,
            她在台北一個非常有名的私校教了一輩子書。有一天,她和我談現在孩子的行為舉止的問題
            時說,現在的家長不太會當父母了,他們都是用奶嘴養小孩。這是一位前輩老師的智慧。 她
            從幼稚園開始一直看著孩子成長到高中,她有太多太多的經驗告訴家長,不要圖快,不要速效
            地去養孩子。這樣的話,孩子的問題會出現在後面,而且還不容易改,因為他們已經長大了
            。 不是很多人都在做的方法就是對的。這種刁奶嘴的做法,很多華人也都在模仿,其實是
            錯誤的。 人長大了,有很多的個性,其實是累積出來的。所以我經常說,寧可那三年多陪他
            吧,以免日後的30年,你還要被他煩惱。
            '''
        ),
    )
    assert parsed_news.category == '美國,舊金山,生活嚮導,教育,家庭教育'
    assert parsed_news.company_id == company_id
    assert parsed_news.timestamp == 1576425600
    assert parsed_news.reporter == '曹景哲'
    assert parsed_news.title == '哺乳的煩惱 媽媽被咬怎麼辦?'
    assert parsed_news.url_pattern == '19-12-16-11726516'