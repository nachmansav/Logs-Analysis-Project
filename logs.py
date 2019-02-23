#!/usr/bin/env python3

import psycopg2

dbname = "news"

try:
    db = psycopg2.connect(database=dbname)
except psycopg2.Error as e:
    print("Unable to connect to the database")
    print(e.pgerror)
    print(e.diag.message_detail)
    sys.exit(1)

c = db.cursor()


def popular_articles():
    """Display the three most popular articles."""
    c.execute("select articles.title,"
              " count(log.path) as views"
              " from articles, log "
              "where log.path like concat('%',articles.slug)"
              " group by articles.title order by views desc limit 3;")
    result1 = list(c.fetchall())
    print('\n The three most popular articles of all time are:')
    for i in range(len(result1)):
        print('\t {} --- {} views'.format
              (str(result1[i])[2:-10], str(result1[i])[-8:-1]))


def popular_authors():
    """Display the popularity of the authors based on page views."""
    c.execute("select authors.name,"
              " count(log.path) as views"
              " from authors, log, articles"
              " where log.path like concat('%',articles.slug) "
              "and articles.author = authors.id "
              "group by authors.name order by views desc;")
    result2 = list(c.fetchall())
    print('\n The most popular authors are:')
    for i in range(len(result2)-1):
        print('\t {} --- {} views'.format
              (str(result2[i])[2:-10], str(result2[i])[-8:-1]))

    print('\t {} --- {} views'.format
          (str(result2[3])[2:-9], str(result2[3])[-7:-1]))


def days_with_errors():
    """Return the day where more than 1% of requests led to errors."""
    c.execute("with views as (select date(time) as day,"
              " count(id) as views from log "
              "group by date(time) order by day),"
              " errors as (select date(time) as day,"
              " count(id) as errors from log "
              "where status <> '200 OK' "
              "group by date(time) order by day) "
              "select views.day, "
              "cast(round(errors.errors,2) / round(views.views /100,2)"
              " as decimal(10,1))"
              " from views, errors"
              " where views.day = errors.day "
              "and errors.errors > views.views / 100;")
    result3 = list(c.fetchall())
    print('\n The days where more than 1% of requests led to errors:')
    print('\t {} --- {}%'.format(str(result3)[16:27], str(result3)[-7:-4]))
    db.close()


if __name__ == '__main__':
    popular_articles()
    popular_authors()
    days_with_errors()
