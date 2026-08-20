import pymysql


def get_connection():

    conn = pymysql.connect(

        host="mysql-1cda855a-dlu-2927.l.aivencloud.com",

        port=19787,

        user="avnadmin",

        password="AVNS_uw9lNTZe8Pu_WFHMiFF",

        database="company1",

        ssl={
            "ca": "ca.pem"
        }

    )

    return conn
