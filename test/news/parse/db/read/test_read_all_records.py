from typing import Final

import news.db
import news.parse.db.create
import news.parse.db.read
import news.parse.db.schema
import news.parse.db.util
import news.parse.db.write


def test_read_all_records(db_name: Final[str], cleanup_db_file: Final) -> None:
    # Randomly create two records.
    # Note that sqlite's index start with 1.
    news_list = [
        news.parse.db.schema.ParsedNews(
            idx=1,
            article='abc',
            category='def',
            company_id=123,
            datetime=456,
            reporter='ghi',
            title='jkl',
            url_pattern='mno',
        ),
        news.parse.db.schema.ParsedNews(
            idx=2,
            article='cba',
            category='fed',
            company_id=321,
            datetime=654,
            reporter='ihg',
            title='lkj',
            url_pattern='onm',
        ),
        news.parse.db.schema.ParsedNews(
            idx=3,
            article='aaa',
            category=None,
            company_id=111,
            datetime=222,
            reporter=None,
            title='bbb',
            url_pattern='ccc',
        ),
    ]

    try:
        db_path = news.parse.db.util.get_db_path(db_name=db_name)
        conn = news.db.get_conn(db_path=db_path)
        cur = conn.cursor()
        news.parse.db.create.create_table(cur=cur)
        news.parse.db.write.write_new_records(
            cur=cur,
            news_list=news_list,
        )
        conn.commit()
    finally:
        conn.close()

    # No error is good.
    all_records = news.parse.db.read.read_all_records(db_name=db_name)
    assert len(all_records) == len(news_list)
    for r1, r2 in zip(all_records, news_list):
        assert r1.idx == r2.idx
        assert r1.article == r2.article
        assert r1.category == r2.category
        assert r1.company_id == r2.company_id
        assert r1.datetime == r2.datetime
        assert r1.reporter == r2.reporter
        assert r1.title == r2.title
        assert r1.url_pattern == r2.url_pattern