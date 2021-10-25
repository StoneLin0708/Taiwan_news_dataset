import re
import textwrap

import news.crawlers.db.schema
import news.crawlers.util.normalize
import news.crawlers.util.request_url
import news.parse.cna
import news.parse.db.schema


def test_parsing_result() -> None:
    r"""Ensure parsing result consistency."""
    company_id = news.crawlers.util.normalize.get_company_id(company='中央社')
    url = r'https://www.cna.com.tw/news/aipl/201501010071.aspx'
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

    parsed_news = news.parse.cna.parser(raw_news=raw_news)

    assert parsed_news.article == re.sub(
        r'\n',
        '',
        textwrap.dedent(
            '''\
            2014年巴西舉行世界盃足球賽和總統選舉,對經濟發展造成負面影響,中央銀行對成長值
            預估幾近零,專家預測2015年巴西經濟應該不會發生太大變化。
            '''
        ),
    )
    assert parsed_news.category == '產經'
    assert parsed_news.company_id == company_id
    assert parsed_news.datetime == 1420041600
    assert parsed_news.reporter == '唐雅陵聖保羅'
    assert parsed_news.title == '2015巴西經濟可能停滯成長'
    assert parsed_news.url_pattern == '201501010071'