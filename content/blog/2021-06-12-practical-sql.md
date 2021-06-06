Title: Practical SQL for Data Analysis 
Date: 2021-06-12 14:30
Category: Blog
Tags: sql, pandas, python, postgresql
Author: Christopher
Summary: Great article from Haki Benita on SQL and Pandas.
Status: draft
comment_id: practical-sql-data-analysis

[Haki's article](https://hakibenita.com/sql-for-data-analysis) showcase how it
can be better to use SQL instead of just pandas.
This post will not go through all the great examples but to take a couple of
examples to convince you to go read his article.
While his examples are using PostgreSQL, the benefits are true for other
databases.

## Let the Database do the Work

## Subtotals

## Pivot Tables

## Conclusion

Using pandas can be very useful as long as you understand that you will be
memory constraint and it may not be as fast as SQL queries.
The added benefit on using SQL earlier in your analysis is that if you know that
you will be eventually be dealing with larger datasets, using SQL queries won't
change your method.
Using pandas and knowing that you will have to find different ways to fit your
data in memory means that you will need to optimize as you go.

I tend to use both pandas and SQL so that I leverage what both does best.

Now go read [Haki's article](https://hakibenita.com/sql-for-data-analysis)!