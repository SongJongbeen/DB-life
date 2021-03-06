from db_cuds import create_db, update_db, execute_db, delete_db, search_db, count_db, search_max_min_db
import os


while True:
    try:
        # 메뉴 인터페이스
        print('')
        print('0. new contract 1. new employee 2. activate contract 3. fix contract '
              '4. open db 5. next year 6. analysis 7. terminate program')
        # 메뉴 입력
        command = int(input('command: '))
        # 새로운 계약
        if command == 0:
            # 사원번호와 고객번호를 입력받음.
            key = search_max_min_db('Cno', 'CONTRACT') + 1
            Eno = int(input('input the number of employee in charge: '))
            CLno = int(input('input the number of the client (if new client, input 0): '))
            if CLno == 0: # 신규 고객인 경우
                CL_key = search_max_min_db('CLno', 'CLIENT') + 1
                CLname = input('input the name of client: ')
                Rname = input('input the name of recipient: ')
                CLdata = [CL_key, CLname, Rname, 0]
                create_db('CLIENT', CLdata)
            else:  # 아닌 경우
                # 데이터 베이스에서 고객 번호를 가지고 온다.
                CL_list = execute_db('SELECT CLno FROM CLIENT', role='findmany')
                CL_list = dict.fromkeys(CL_list, 0)
                # 고객이 존재 하는지 확인 후 처리
                try:
                    CL_list[CLno]
                except KeyError:
                    print('존재하지 않는 고객입니다.')

                    input("\n\n계속하려면 Enter를 누르세요")
                    os.system("cls")
                    continue

                CL_key = CLno
            # 계약 타입을 입력받고 데이터베이스에 추가함.
            Ctype = input('input the type of the contract: ')
            Cdata = [key, Eno, CL_key, Ctype, 0]
            create_db('CONTRACT', Cdata)
            print('new contract created')

        # 새로운 직원 고용
        elif command == 1:
            key = count_db('EMPLOYEE') + 1
            Ename = input('input the name of new employee: ')
            data = [key, Ename, 0, 0, 2600, 0]
            create_db('EMPLOYEE', data)
            print('new employee hired')

        # 계약 발동
        elif command == 2:
            key = input('input the contract code: ')
            update_db('CONTRACT', 'Cno', key, 'Cactive', 1)
            print('contract activated')

        # 계약 내용 수정
        elif command == 3:
            key = input('input the contract code: ')
            print('Eno (Employee Number) / CLno (Client Number / Ctype (contract type)')
            field = input('input the field name: ')
            new_data = input('input new data: ')
            update_db('CONTRACT', 'Cno', key, field, new_data)
            print('contract fixed')

        # 데이터베이스 직접 열기
        elif command == 4:
            print('input \'.exit\' to terminate')
            os.system('sqlite3 dblife.db')

        # 연말정산 및 내년도로 넘어가기
        elif command == 5:
            # 현재 연도
            year = int(search_max_min_db('Fyear', 'FINANCE'))
            # 안내 문구 출력
            print('%s년 연말정산을 진행하고 다음 년도로 넘어갑니다.' % year)

            # 자금 계산
            Capital = search_db('Capital', 'FINANCE', 'Fyear', year, fetch='one')
            LaborCost = execute_db('SELECT SUM(Ewage) FROM EMPLOYEE')
            BonusCost = execute_db('SELECT SUM(Ebonus) FROM EMPLOYEE')
            Premium = execute_db(
                'SELECT SUM(Premium) FROM (SELECT COUNT(C.Ctype) * Premium AS Premium FROM Ctype T, CONTRACT C WHERE C.Ctype = T.Ctype GROUP BY C.Ctype)')
            Payout = execute_db(
                'SELECT SUM(Payout) FROM (SELECT COUNT(C.Ctype) * Payout AS Payout FROM Ctype T, CONTRACT C WHERE C.Ctype = T.Ctype AND C.Cactive = 1 GROUP BY C.Ctype)')
            # 발동된 계약이 NULL값일 경우 계산을 위해 0으로 변경
            if Payout == None:
                Payout = 0

            prev_Capital = Capital
            Capital = Capital - LaborCost - BonusCost - Payout + Premium
            update_db('FINANCE', 'Fyear', year, 'Capital', Capital)

            # 발동된 계약 제거
            delete_db('CONTRACT', 'Cactive', 1)

            # CLhistory 업데이트
            CLhistory_id = execute_db('SELECT C.CLno FROM Ctype T, CONTRACT C WHERE C.Ctype = T.Ctype;', role='findmany')
            CLhistory = execute_db('SELECT T.Premium AS CLhistory FROM Ctype T, CONTRACT C WHERE C.Ctype = T.Ctype;',
                                   role='findmany')

            for i in range(len(CLhistory_id)):
                execute_db('UPDATE CLIENT SET CLhistory = %d WHERE CLno = %d' % (CLhistory[i], CLhistory_id[i]),
                           role='else')

            # 가장 많은 금액을 지불한 고객 구하기
            vip = execute_db('SELECT CLname from CLIENT where CLhistory = (Select max(CLhistory) from CLIENT)',
                             role='findmany')

            # 직원 정보 업데이트 - 연차 +1 & 승진
            execute_db('UPDATE EMPLOYEE SET Eyear = Eyear + 1', role='else')
            execute_db('UPDATE EMPLOYEE SET Erole = 1 WHERE Eyear >= 5 AND Eyear < 7', role='else')
            execute_db('UPDATE EMPLOYEE SET Erole = 2 WHERE Eyear >= 7 AND Eyear < 10', role='else')
            execute_db('UPDATE EMPLOYEE SET Erole = 3 WHERE Eyear >= 10 AND Eyear < 15', role='else')
            execute_db('UPDATE EMPLOYEE SET Erole = 4 WHERE Eyear >= 15 AND Eyear < 19', role='else')
            execute_db('UPDATE EMPLOYEE SET Erole = 5 WHERE Eyear >= 19', role='else')

            # 직원 정보 업데이트 - 승진자 조사
            promotion = execute_db(
                'SELECT Ename FROM EMPLOYEE WHERE Eyear=5 OR Eyear=7 OR Eyear=10 OR Eyear=15 OR Eyear=19', role='findmany')

            # 직원 정보 업데이트 - 연봉 인상
            execute_db('UPDATE EMPLOYEE SET Ewage = 2600 + 200 * Eyear WHERE Eyear <= 2', role='else')
            execute_db('UPDATE EMPLOYEE SET Ewage = 3300 WHERE Eyear = 3', role='else')
            execute_db('UPDATE EMPLOYEE SET Ewage = 4200 WHERE Eyear = 4', role='else')
            execute_db('UPDATE EMPLOYEE SET Ewage = 4200 + (Eyear - 4) * 300 WHERE Eyear = 5 OR Eyear = 6', role='else')
            execute_db('UPDATE EMPLOYEE SET Ewage = 5200 WHERE Eyear = 7', role='else')
            execute_db('UPDATE EMPLOYEE SET Ewage = 5200 + (Eyear - 7) * 300 WHERE Eyear >=  8 AND Eyear < 18', role='else')
            execute_db('UPDATE EMPLOYEE SET Ewage = 8000 WHERE Eyear = 18', role='else')
            execute_db('UPDATE EMPLOYEE SET Ewage = 10000 WHERE Eyear = 19', role='else')
            execute_db('UPDATE EMPLOYEE SET Ewage = 10100 WHERE Eyear = 20', role='else')

            # 가장 수익이 좋은 직원 조사
            mvp = execute_db(
                'SELECT Ename FROM EMPLOYEE WHERE Eno = (SELECT Eno FROM (SELECT Eno, COUNT(Eno) * 100 AS Ebonus FROM CONTRACT GROUP BY Eno ORDER BY Ebonus DESC LIMIT 1))',
                role='findmany')

            # 보너스 계산
            Ebonus_id = execute_db('SELECT Eno FROM CONTRACT GROUP BY Eno', role='findmany')
            Ebonus = execute_db('SELECT COUNT(Eno) * 100 AS Ebonus FROM CONTRACT GROUP BY Eno', role='findmany')

            for i in range(len(Ebonus_id)):
                execute_db('UPDATE EMPLOYEE SET Ebonus = %d WHERE Eno = %d' % (Ebonus[i], Ebonus_id[i]), role='else')

            # 내년도 FINANCE row 추가
            LaborCost = execute_db('SELECT SUM(Ewage) FROM EMPLOYEE')
            BonusCost = execute_db('SELECT SUM(Ebonus) FROM EMPLOYEE')
            Premium = execute_db(
                'SELECT SUM(Premium) FROM (SELECT COUNT(C.Ctype) * Premium AS Premium FROM Ctype T, CONTRACT C WHERE C.Ctype = T.Ctype GROUP BY C.Ctype)')
            Payout = 0

            # 내년 자금은 우선 올해 자금으로 입력
            create_db('FINANCE', [year + 1, Capital, LaborCost, Premium, Payout, BonusCost])

            # 흑자여부 계산
            Difference = Capital - prev_Capital
            finance_result = ''
            if Difference > 0:
                finance_result = '흑자'
            elif Difference == 0:
                finance_result = '변동없음'
            elif Difference < 0:
                finance_result = '적자'

            # 분석 결과 출력
            print('분석 결과입니다.\n')
            print('올해 남은 금액은 %d 원입니다.' % Capital)
            print('한 해간 결산 결과는 %s 입니다. 변동 금액: %d 원' % (finance_result, Difference))

            print('\n승진한 사람 명단입니다. 축하합니다.')
            for person in promotion:
                print('  ' + person)
            print('\n가장 실적이 좋았던 직원 명단입니다. 축하합니다.')
            for person in mvp:
                print('  ' + person)
            print('\nVIP 고객 리스트입니다. 확인바랍니다.')
            for person in vip:
                print('  ' + person)

        # 분석 & 분석 결과 열람
        elif command == 6:
            # 현재 연도 구하기
            year = int(search_max_min_db('Fyear', 'FINANCE'))

            # 가장 수익이 좋은 직원 & 가장 보험금을 많이 지급한 고객 구하기
            mvp = execute_db(
                'SELECT Ename FROM EMPLOYEE WHERE Eno = (SELECT Eno FROM (SELECT Eno, COUNT(Eno) * 100 AS Ebonus FROM CONTRACT GROUP BY Eno ORDER BY Ebonus DESC LIMIT 1))',
                role='findmany')
            vip = execute_db('SELECT CLname from CLIENT where CLhistory = (Select max(CLhistory) from CLIENT)',
                             role='findmany')

            # 결과 출력
            print('가장 실적이 좋았던 직원 명단입니다. 축하합니다.')
            for person in mvp:
                print('  ' + person)
            print('\nVIP 고객 리스트입니다. 확인바랍니다.')
            for person in vip:
                print('  ' + person)

            # 현재 자금 상황 출력 (연말정산에 비해 엄밀하지 않음, 참고용)
            total_finance = [execute_db('SELECT Capital FROM FINANCE WHERE Fyear = %d' % year),
                             execute_db('SELECT LaborCost FROM FINANCE WHERE Fyear = %d' % year),
                             execute_db('SELECT Premium FROM FINANCE WHERE Fyear = %d' % year),
                             execute_db('SELECT Payout FROM FINANCE WHERE Fyear = %d' % year),
                             execute_db('SELECT BonusCost FROM FINANCE WHERE Fyear = %d' % year)]
            intro_sent = ["해당년도 현자금", "예상인건비 지출", "예상 보험료 수입", "예상 보험금 지출", "예상 성과금 지출"]
            result = {}
            for i in range(len(total_finance)):
                result[intro_sent[i]] = total_finance[i]

            print()
            for k, v in result.items():
                print(f"{k}: {v}")

        # 프로그램 종료
        elif command == 7:
            break

        # 잘못된 명령어일 경우
        else:
            print("Invalid Command!")

    # 오류 처리 코드
    except Exception as e:
        print("오류가 발생했습니다. 처음으로 돌아갑니다.")
        print("오류내용:", e)

    # 프로그램 실행
    input("\n\n계속하려면 Enter를 누르세요")
    os.system("cls")
