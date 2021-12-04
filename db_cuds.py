import sqlite3


def create_db(table, data):
    conn = sqlite3.connect('dblife.db', isolation_level=None)
    c = conn.cursor()
    if table == 'EMPLOYEE':
        c.execute('INSERT INTO EMPLOYEE(Eno, Ename, Erole, Eyear, Ewage, Ebonus) VALUES(?,?,?,?,?,?)', data)
    elif table == 'CONTRACT':
        c.execute('INSERT INTO CONTRACT(Cno, Eno, CLno, Ctype, Cactive) VALUES(?,?,?,?,?)', data)
    elif table == 'CLIENT':
        c.execute('INSERT INTO CLIENT(CLno, CLname, Rname, CLhistory) VALUES(?,?,?,?)', data)
    elif table == 'FINANCE':
        c.execute('INSERT INTO FINANCE(Fyear, Capital, LaborCost, Premium, Payout, BonusCost) VALUES(?,?,?,?,?,?)', data)
    elif table == 'CTYPE':
        c.execute('INSERT INTO CTYPE(Ctype, Premium, Payout) VALUES(?,?,?)', data)

    c.execute('SELECT * FROM %s' % table)
    for row in c.fetchall():
        print(row)
    conn.commit()
    backup_db(conn)

    conn.close()


def update_db(table, key, key_value, field, new_data):
    conn = sqlite3.connect('dblife.db', isolation_level=None)
    c = conn.cursor()
    c.execute('UPDATE %s SET %s=:%s WHERE %s=:%s' % (table, field, field, key, key),
              {field: new_data, key: key_value})

    c.execute('SELECT * FROM %s' % table)
    for row in c.fetchall():
        print(row)
    conn.commit()
    backup_db(conn)

    conn.close()


def delete_db(table, field, key):
    conn = sqlite3.connect('dblife.db', isolation_level=None)
    c = conn.cursor()
    c.execute('DELETE FROM %s WHERE %s=:%s' % (table, field, field), {field: key})

    c.execute('SELECT * FROM %s' % table)
    for row in c.fetchall():
        print(row)
    conn.commit()
    backup_db(conn)

    conn.close()


def search_db(select_value, table, where_field, where_value):
    conn = sqlite3.connect('dblife.db', isolation_level=None)
    c = conn.cursor()

    c.execute('SELECT %s FROM %s WHERE %s=:%s' % (select_value, table, where_field, where_field),
              {where_field: where_value})
    for row in c.fetchall():
        print(row[0])
        result = row[0]

    conn.close()
    return result


def show_db(table='*'):
    conn = sqlite3.connect('dblife.db', isolation_level=None)
    c = conn.cursor()

    c.execute('SELECT * FROM %s' % table)
    for row in c.fetchall():
        print(row[0])

    conn.close()


def count_db(table):
    last_key = 0
    conn = sqlite3.connect('dblife.db', isolation_level=None)
    c = conn.cursor()

    c.execute('SELECT * FROM %s' % table)
    for row in c.fetchall():
        last_key += 1

    conn.close()
    return last_key


def backup_db(conn):
    with conn:
        with open('dump.sql', 'w') as f:
            for line in conn.iterdump():
                f.write('%s\n' % line)
            print('Backup Completed')
