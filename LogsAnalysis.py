import sys
import psycopg2
import os


def get_data(query):
    """connect to database and Return Query results ."""
    try:

        db = psycopg2.connect("dbname = news")
        con = db.cursor()
        con.execute(query)
        result = con.fetchall()
        db.close()
        return result

    except:
        os.system('clear')
        print("Error .. Can not connect to database")
        sys.exit()


def report(p_sn):
    """Select the Query and sending to get_data() function to get results and printing ."""
    os.system('clear')
    print("Wait a few moments please ..")

    if p_sn == "1":

        res_data = get_data("Select a.title ,count(log.path) as views_count " 
                            "From articles as a " 
                            "Inner join log on a.slug = reverse(split_part(reverse( log.path ),'/',1)) " 
                            "group by a.title " 
                            "order by views_count desc Limit 3;")
        os.system('clear')
        print("1.The most popular three articles of all time:")
        print()
        print("Articles"+" "*31 + "Views")
        print("-"*45)

        for l in res_data:
            print(l[0] + " "*7 + str(l[1]))

        print("-" * 45)
        print()

    elif p_sn == "2":
        res_data = get_data("Select au.name ,count(log.path) as views_count " 
                            "From authors as au "
                            "inner join articles as a on  a.author = au.id " 
                            "Inner join log on a.slug = reverse(split_part(reverse( log.path ),'/',1)) " 
                            "group by au.name " 
                            "order by views_count desc Limit 3;")
        os.system('clear')
        print("2.The most popular article authors of all time:")
        print()
        print("Authors" + " " * 32 + "Views")
        print("-" * 45)

        for l in res_data:
            print(l[0] + " " * (32-len(l[0])) + " " * 7 + str(l[1]))

        print("-" * 45)
        print()

    elif p_sn == "3":
        res_data = get_data(""
                            # select (A) to get error percentage 
                            "select req_err.day_dd , round((req_err.errors_count::numeric / " 
                            "req_ok.ok_count::numeric)*100,2)  as per "
                            "from " 
                            # select (B) to get error requests 
                            "(select to_char(time,'Mon DD YYYY') as day_dd , count(id) as errors_count "
                            "from log " 
                            "where status != '200 OK' " 
                            "group by day_dd)"  # end (B)
                            "as req_err, " 
                            # select (C) to get 200 OK requests
                            "(select to_char(time,'Mon DD YYYY') as day_dd  , count(id) as ok_count  "
                            "from log " 
                            "where status = '200 OK' " 
                            "group by day_dd)"  # end (C)
                            "as req_ok " 
                            "where req_err.day_dd = req_ok.day_dd " 
                            "and (req_err.errors_count::numeric / req_ok.ok_count::numeric)*100 > 1;")
        os.system('clear')
        print("3.The days did more than 1% of requests lead to errors:")
        print()
        print("Date" + " " * 25 + "Error percentage")
        print("-" * 45)

        for l in res_data:
            print(l[0] + " " * (32-len(l[0])) + " " * 7 + str(l[1])+"%")

        print("-" * 45)
        print()

    input("Press enter to continue..")


#  List of reports
sn = ""
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

#  exit program
os.system('clear')
sys.exit()
