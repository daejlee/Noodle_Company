
use stock_db;
create table kor_ticker
(
	종목코드 varchar(6) not null,
    종목명 varchar(20),
    시장구분 varchar(6),
    종가 float,
    시가총액 float,
    기준일 date,
    EPS float,
    선행EPS float,
    BPS float,
    주당배당금 float,
    종목구분 varchar(5),
    primary key(종목코드, 기준일)
)
create table kor_fs
(
	계정 varchar(30),
	기준일 date,
	값 float,
	종목코드 varchar(6),
	공시구분 varchar(1),
	primary key(계정, 기준일, 종목코드, 공시구분)
)

create table kor_sector
(
    IDX_CD varchar(3),
    CMP_CD varchar(6),
    CMP_KOR varchar(20),
    SEC_NM_KOR varchar(10),
    기준일 date,
    primary key(CMP_CD, 기준일)
);

select * from kor_ticker;
select * from kor_fs;