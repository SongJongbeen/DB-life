from db_cuds import create_db, update_db, delete_db, search_db, show_db, count_db
import os

while True:
    print('0. new contract 1. new employee 2. activate contract 3. fix contract '
          '4. fix db 5. next year 6. analysis 7. terminate program')
    command = int(input('command: '))
    if command == 0:
        key = count_db('CONTRACT') + 1
        Eno = int(input('input the number of employee in charge: '))
        CLno = int(input('input the name of the client (if new client, input 0): '))
        if CLno == 0:
            CL_key = count_db('CLIENT') + 1
            CLname = input('input the name of client: ')
            Rname = input('input the name of recipient: ')
            CLdata = [CL_key, CLname, Rname, 0]
            create_db('CLIENT', CLdata)
        else:
            CL_key = CLno
        Ctype = input('input the type of the contract: ')
        Cdata = [key, Eno, CL_key, Ctype, 0]
        create_db('CONTRACT', Cdata)
    elif command == 1:
        key = count_db('EMPLOYEE') + 1
        Ename = input('input the name of new employee: ')
        data = [key, Ename, 0, 0, 2600, 0]
        create_db('EMPLOYEE', data)
    elif command == 2:
        key = input('input the contract code: ')
        update_db('CONTRACT', 'Cno', key, 'Cactive', 1)
    elif command == 3:
        key = input('input the contract code: ')
        print('which part do you want to fix? 1. employee in charge 2. client 3. contract type')
        field = input('input: ')
        new_data = input('input new data: ')
        update_db('CONTRACT', 'Cno', key, field, new_data)
    elif command == 4:
        print('input \'.exit\' to terminate')
        os.system('sqlite3 dblife.db')
    elif command == 5:
        print('1. 모든 직원 임금 및 성과금 지출 (Capital - LaborCost - BonusCost)')
        print('2. 모든 보험료 수익 정산 (Capital + Premium)')
        print('\t2.1. Premium 계산법: sum(from CONTRACT count Ctype = 각 A~E 따라서 from CTYPE 에서 Premium)')
        print('3. 모든 보험금 지출 정산 (Capital - Payout)')
        print('\t3.1. Payout 계산법: sum(from CONTRACT select Cactive = 1 count Ctype = 각 A~E 따라서 from CTYPE 에서 Payout)')
        print('4. Cactive가 1인 CONTRACT data 모두 삭제')
        print('5. CLhisotry 업데이트: 각각 낸 금액만큼 더해줌')
        print('6. 직원 정보 업데이트: 아래의 규칙을 따름')
        print('\t6.1. 직원 모두의 Eyear += 1')
        print('\t6.2. Erole: Eyear이 5 이상이면 주임 / Eyear이 7년 이상이면 대리 / Eyear이 10년 이상이면 과장 / '
              'Eyear이 15년 이상이면 차장 / Eyear이 19년 이상이면 부장')
        print('\t\t6.2.1. 이 과정에서 승진하게 되는 사람 리스트에 따로 정리')
        print('\t6.3. Ewage: 엑셀 파일 참조')
        print('\t6.4. Ebonus: from CONTRACT Eno가 본인인 것의 개수 * 100')
        print('\t\t6.4.1. 이 과정에서 가장 Ebonus가 높았던 사람 따로 정리')
        print('7. 다음 년도 Fyear row 생성. 1~3 계산한 값이 Capital값. 각 값 계산은 아래를 따름.')
        print('\t7.1. LaborCost: Ewage의 합산값')
        print('\t7.2. BonusCost: Ebonus의 합산값')
        print('\t7.3. Premium: sum(from CONTRACT count Ctype = 각 A~E 따라서 from CTYPE 에서 Premium)')
        print('\t7.4. Payout: sum(from CONTRACT select Cactive = 1 count Ctype = 각 A~E 따라서 from CTYPE 에서 Payout)')
        print('8. 분석 결과 보여주기')
        print('8.1. 당해 승진한 사람은 ~~ 입니다. 축하합니다.')
        print('8.2. 지난해 1년간 결산 결과는 흑자/적자 입니다. 총+/-~~~~원을 벌/잃었습니다. Fyear 당해년도 Capital - 작년도 Capital')
        print('8.3. 지난해 최우수 실적은 ~~ 입니다. 축하합니다. 가장 Bonus가 높았던 직원')
        print('8.4. 지금까지 최우수 고개은 ~~ 입니다. 가장 CLhistory가 높은 고객')
    elif command == 6:
        print('가장 많은 계약을 따낸 직원 이름')
        print('가장 보험료를 많이 지출한 고객 이름 (VIP)')
        print('해당년도 현자금 / 예상 인건비 지출/ 예상 보험료 수입/ 예상 보험금 지출/ 예상 성과금 지출')
    elif command == 7:
        break
