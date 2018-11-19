#!/usr/bin/env python3

import sys
import psycopg2
import os


def connect(query):
    """connect to database and Return Query results"""
    try:
        db = psycopg2.connect("dbname = news")
        con = db.cursor()
        con.execute(query)
        result = con.fetchall()
        db.close()

        return result

    except Exception:
        os.system('clear')
        print("Error .. Can not connect to database")
        sys.exit()
        raise

def get_data(query):
    """connect to database and Return Query results"""
    try:
        db = psycopg2.connect("dbname = news")
        con = db.cursor()
        con.execute(query)
        result = con.fetchall()
        db.close()

        return result

    except Exception:
        os.system('clear')
        print("Error .. Can not connect to database")
        sys.exit()
        raise





def report(p_sn):
    """Select the Query and sending to get_data() function
    to get results and printing.
    """
    os.system('clear')
    print("Wait a few moments please ..")

    if p_sn == "1":
        res_data = get_data("SELECT a.title ,COUNT(log.path) AS views_count "
                            "FROM articles AS a "
                            "INNER JOIN log ON a.slug = reverse(split_part"
                            "(reverse( log.path ),'/',1)) "
                            "GROUP BY a.title "
                            "ORDER BY views_count desc Limit 3;")
        os.system('clear')
        print("1.The most popular three articles of all time:")
        print()
        print("Articles" + " "*31 + "Views")
        print("-" * 45)

        for l in res_data:
            print("{}{}{} ".format(l[0], " "*7, str(l[1])))

        print("-"*45)
        print()

    elif p_sn == "2":
        res_data = get_data("SELECT au.name ,COUNT(log.path) AS views_count "
                            "FROM authors AS au "
                            "INNER JOIN articles AS a ON  a.author = au.id "
                            "INNER JOIN log ON a.slug = reverse(split_part"
                            "(reverse( log.path ),'/',1)) "
                            "GROUP BY au.name "
                            "ORDER BY views_count DESC LIMIT 3;")
        os.system('clear')
        print("2.The most popular article authors of all time:")
        print()
        print("Authors" + " "*32 + "Views")
        print("-"*45)

        for l in res_data:
            print("{}{}{}{}".format(l[0], " "*(32 - len(l[0])),
                                    " "*7, str(l[1])))
        print("-"*45)
        print()

    elif p_sn == "3":
        res_data = get_data("SELECT req_err.day_dd , ROUND((req_err.errors_"
                            "count::numeric /req_ok.ok_count::numeric)*100,1) "
                            "AS per FROM (SELECT to_char(time,'Mon DD YYYY') "
                            "AS day_dd , COUNT(*) AS errors_count FROM log "
                            "WHERE status = '404 NOT FOUND' GROUP BY day_dd)"
                            "AS req_err,(SELECT to_char(time,'Mon DD YYYY') "
                            "AS day_dd  , COUNT(*) AS ok_count FROM log "
                            "GROUP BY day_dd) AS req_ok WHERE req_err.day_dd "
                            "=req_ok.day_dd AND (req_err.errors_count::numeric"
                            " / req_ok.ok_count::numeric)*100 >= 1 ORDER BY "
                            "req_err.day_dd ;")
        os.system('clear')
        print("3.The days did more than 1% of requests lead to errors:")
        print()
        print("Date" + " "*25 + "Error percentage")
        print("-"*45)

        for l in res_data:
            print("{}{}{}{} %".format(l[0], " "*(32-len(l[0])),
                                      " "*7, str(l[1])))

        print("-"*45)
        print()

    input("Press enter to continue..")


def main():

    """ List of reports"""
    while True:
        os.system('clear')
        print("Logs analysis project")
        print("---------------------")
        print()
        print("""
        List of reports
        ---------------

        1.The most popular three articles of all time.
        2.The most popular article authors of all time.
        3.The days did more than 1% of requests lead to errors.
        4.Exit/Quit.
        """)
        sn = input("Select the report?.. ")

        if sn == "1":
            report(sn)
        elif sn == "2":
            report(sn)
        elif sn == "3":
            report(sn)
        elif sn == "4":
            break  # break here

    """ exit program """
    os.system('clear')
    sys.exit()


if __name__ == "__main__":
    main()
