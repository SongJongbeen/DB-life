import sqlite3


# 새로운 값을 데이터베이스에 삽입하는 기능
def create_db(table, data):
    # 데이터 베이스 열기
    conn = sqlite3.connect('dblife.db', isolation_level=None)
    c = conn.cursor()
    # 각 테이블에 맞는 value를 요구
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

    # 바뀐 부분 출력 (결과 확인용)
    # c.execute('SELECT * FROM %s' % table)
    # for row in c.fetchall():
    #     print(row)

    # 데이터베이스에 반영 및 백업
    conn.commit()
    backup_db(conn)

    # 데이터베이스 닫기
    conn.close()


# 데이터베이스 특정 값 수정하는 기능
def update_db(table, key, key_value, field, new_data):
    # 데이터 베이스 열기
    conn = sqlite3.connect('dblife.db', isolation_level=None)
    c = conn.cursor()
    # 명령어 실행
    c.execute('UPDATE %s SET %s=:%s WHERE %s=:%s' % (table, field, field, key, key),
              {field: new_data, key: key_value})

    # 바뀐 부분 출력 (결과 확인용)
    # c.execute('SELECT * FROM %s' % table)
    # for row in c.fetchall():
    #     print(row)

    # 데이터베이스에 반영 및 백업
    conn.commit()
    backup_db(conn)

    # 데이터베이스 닫기
    conn.close()


# 특정 명령어 실행하는 기능
def execute_db(message, role='find'):
    # 데이터 베이스 열기
    conn = sqlite3.connect('dblife.db', isolation_level=None)
    c = conn.cursor()

    # 명령어 실행하기
    c.execute(message)

    # 특정 값을 찾기 위함일때
    if role == 'find':
        result = c.fetchone()[0]
        conn.close()
        return result
    # 특정 여러 값을 찾기 위함일때 (리스트 형태로 반환)
    elif role == 'findmany':
        result = []
        for row in c.fetchall():
            result.append(row[0])
        return result
    # 그 외 명령어 실행만이 목적이었을때
    elif role == 'else':
        # 데이터베이스 닫기
        conn.close()


# 데이터베이스 특정 열 삭제하는 기능
def delete_db(table, field, key):
    # 데이터 베이스 열기
    conn = sqlite3.connect('dblife.db', isolation_level=None)
    c = conn.cursor()
    # 명령어 실행
    c.execute('DELETE FROM %s WHERE %s=:%s' % (table, field, field), {field: key})

    # 바뀐 부분 출력 (결과 확인용)
    # c.execute('SELECT * FROM %s' % table)
    # for row in c.fetchall():
    #     print(row)

    # 데이터베이스에 반영 및 백업
    conn.commit()
    backup_db(conn)

    # 데이터베이스 닫기
    conn.close()


# 데이터베이스에서 특정 열/값 검색하는 기능
def search_db(select_value, table, where_field, where_value, fetch='many'):
    # 데이터 베이스 열기
    conn = sqlite3.connect('dblife.db', isolation_level=None)
    c = conn.cursor()

    # 명령어 실행
    c.execute('SELECT %s FROM %s WHERE %s=:%s' % (select_value, table, where_field, where_field),
              {where_field: where_value})
    # 여러개를 찾을 경우 (리스트형태로 반환)
    if fetch == 'many':
        result = []
        for row in c.fetchall():
            result.append(row[0])
    # 하나를 찾을 경우
    elif fetch == 'one':
        result = c.fetchone()[0]

    # 데이터베이스 닫기
    conn.close()
    # 결과값 출력
    return result


# 데이터베이스 특정 부분 열람하는 기능
def show_db(table='*'):
    # 데이터 베이스 열기
    conn = sqlite3.connect('dblife.db', isolation_level=None)
    c = conn.cursor()

    # 출력
    c.execute('SELECT * FROM %s' % table)
    for row in c.fetchall():
        print(row[0])

    # 데이터베이스 닫기
    conn.close()


# 데이터베이스 특정 테이블 요소 개수 세는 기능
def count_db(table):
    # 개수 초기값
    nvm = 0
    # 데이터 베이스 열기
    conn = sqlite3.connect('dblife.db', isolation_level=None)
    c = conn.cursor()

    # row 마다 개수에 1씩 추가
    c.execute('SELECT * FROM %s' % table)
    for row in c.fetchall():
        nvm += 1

    # 데이터베이스 닫기
    conn.close()
    # 결과값 출력
    return nvm


# 최대 / 최소 값 찾는 기능
def search_max_min_db(field, table, role='max'):
    # 데이터 베이스 열기
    conn = sqlite3.connect('dblife.db', isolation_level=None)
    c = conn.cursor()

    # 명령어 실행
    c.execute('SELECT %s(%s) FROM %s' % (role, field, table))
    result = c.fetchone()[0]

    # 데이터베이스 닫기
    conn.close()
    # 결과값 출력
    return result


# 데이터 백업하는 기능
def backup_db(conn):
    # 데이터 베이스 열기
    with conn:
        # 백업 문서 작성
        with open('dump.sql', 'w') as f:
            for line in conn.iterdump():
                f.write('%s\n' % line)
            # 안내 문구 출력 (작동 확인용)
            # print('Backup Completed')
