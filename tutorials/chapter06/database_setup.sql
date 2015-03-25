-- first how to create a table
-- show the various integrity constraints
-- now do some inserts to show the errors
-- RDBMSs give lots of errors; thats a feature
-- show SELECT * FROM 
-- show WHERE
-- show DELETE
-- show UPDATE... SET


DROP TABLE IF EXISTS person;

CREATE TABLE person (
    personid    integer         NOT NULL    PRIMARY KEY,
    age         integer         NOT NULL    CHECK( age > 13 ),
    lname       varchar(20)     NOT NULL,
    fname       varchar(20)
);

INSERT INTO person VALUES (1,7,'Clark','Joseph');

DROP TABLE IF EXISTS company;

CREATE TABLE company (
    companyid   integer         NOT NULL    PRIMARY KEY,
    name        varchar(40)     NOT NULL,
    founded     char(4)
);

INSERT INTO company VALUES (1,'ASU',1885);

-- you'll find you need to move this
DROP TABLE IF EXISTS job;

CREATE TABLE job (
    personid    integer         NOT NULL    REFERENCES person(personid),
    companyid   integer         NOT NULL    REFERENCES company(companyid),
    position    varchar(10)     NOT NULL,
    startyear   char(4)         NOT NULL
);

INSERT INTO job VALUES (1,1,'Clinical Assistant Professor','2013');

DELETE FROM person WHERE personid=1;

-- inserting one profile into the database takes a lot of queries

INSERT INTO person VALUES (123,40,'McLane','John');
INSERT INTO company VALUES (1001,'NYPD','1845');
INSERT INTO job VALUES (123,1001,'Lieutenant','1988');
INSERT INTO company VALUES (1002,'LAPD','1869');
INSERT INTO job VALUES (123,1002,'Lieutenant','1990');

-- retrieving the full profile is also complicated and doesn't exactly give you a structured document

SELECT fname, lname, company.name, position, startyear
FROM person 
    JOIN job ON person.personid=job.personid
    JOIN company ON job.companyid=company.companyid
WHERE person.lname='McLane';

-- however, you can easily flip it around and query from the company as a starting point
-- which is hard to do in KV or DS databases

SELECT fname, lname, company.name, position, startyear
FROM company 
    JOIN job ON job.companyid=company.companyid
    JOIN person ON person.personid=job.personid
WHERE company.name='NYPD';

-- aggregations: we can count or average or sum data across a result

SELECT company.name, count(personid)
FROM person
    JOIN job ON person.personid=job.personid
    JOIN company ON job.companyid=company.companyid
GROUP BY company.name;

SELECT company.name, average(age)
FROM person
    JOIN job ON person.personid=job.personid
    JOIN company ON job.companyid=company.companyid
GROUP BY company.name;

-- subqueries: for example, comparing something to an aggregation (average in this case)

SELECT average(age)
FROM person;

SELECT fname, lname
FROM person
WHERE age > (SELECT average(age) FROM person);

-- transaction block

BEGIN;
    DELETE FROM job WHERE personid=1 AND companyid=1;
    INSERT INTO job VALUES (1,1,'Full Professor','2015');
COMMIT;




    