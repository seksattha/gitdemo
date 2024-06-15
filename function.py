import sqlite3
def demo1():
    for i in range(1,10):
        print(i)

demo1()

def demo2():
    try:
        with sqlite3.connect("test.db") as con:
            sql_cmd = """
                create table t1 
            """
    except Exception as e:
        print(f'error {e}')