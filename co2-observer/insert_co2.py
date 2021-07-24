import MySQLdb
import os

def insert_co2(co2):
    conn = MySQLdb.connect(
        user=os.environ['MYSQL_USER'],
        passwd=os.environ['MYSQL_PASSWORD'],
        host=os.environ['MYSQL_HOST'],
        db=os.environ['MYSQL_DATABASE']
    )
    cur = conn.cursor()

    try:
        sql = """
            INSERT INTO co2 (
                co2_val
            )     
            VALUES (
                %(co2_val)s
            )
        """
        bind_params = {
            'co2_val': co2
        }
        cur.execute(sql, bind_params)
        conn.commit()
        return True
    except BaseException as e:
        raise e
    finally:
        cur.close
        conn.close
