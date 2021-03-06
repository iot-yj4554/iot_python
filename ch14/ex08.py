# 종합적으로 연습하기
# Mission : config.ini 에 담긴 정보를 읽어서 원하는 형태의 파일로 저장 후 불러오기

import sys
import traceback

def load_config():
    config = {}
    with open('config.ini', 'rt') as f: # 해당 파일은 영어이기 때문에 인코딩 옵션 주지 않아도 됨
        entries = f.readlines()
        for line in entries:
            line = line.replace('\n','')
            config[line.split('=')[0]] = line.split('=')[1]
    return config


def load(fpath, encoding):
    with open(fpath, 'rt', encoding=encoding) as f:
        return f.readlines()


def make_book(lines):
    book = {}
    book_index = lines[0].replace('\n','').split(',')
    for line in lines[1:]:
        line = line.replace('\n','').split(',')
        book[line[0]] = line[1:]
    return book, book_index


def init():
    config = load_config()
    lines = load(config['FNAME'], config['ENCODING'])
    book, book_index = make_book(lines)
    return book, config, book_index


def select_menu():
    print()
    print('1)목록  2)상세보기  3)추가  4)수정  5)삭제  6)종료')
    menu = int(input('입력 : '))
    print()
    return menu


# menu mode 1
def print_book(book):
    print('==============================================')
    print('                  주소록')
    print('==============================================')
    names = sorted(list(book.keys()))
    for name in names:
        print(f'{name} : {book[name][0]}, {book[name][1]}, {book[name][2]}')


# menu mode 2
def print_detail(book):
    name = input('찾는 사람의 이름을 입력하세요 : ') # 완전 일치 검색
    if name in book.keys():
        print(f'*** {name} : {book[name][0]}, {book[name][1]}, {book[name][2]} ***')
    else:
        print(f'{name} 님은 목록에 없습니다.')
    print()


# menu mode 3 -> data update 반드시 필요
def add_entry(book):
    name = input('등록할 이름을 입력하세요 : ')
    if name in book.keys():
        print(f'{name} 님은 이미 존재합니다.')
        return
    
    phone = input('전화번호를 입력하세요 : ')
    email = input('이메일을 입력하세요 : ')
    addr = input('주소를 입력하세요 : ')
    book[name] = [phone, email, addr]
    print()
    print('등록이 완료되었습니다.')


# menu mode 4 -> data update 반드시 필요
def update_entry(book):
    name = input('수정할 이름을 입력하세요 : ')
    if name not in book.keys():
        print(f'{name}은 목록에 없습니다.')
        return
    
    modify_num = int(input('수정할 항목을 선택하세요. 1)전화번호 2)이메일 3)주소 : '))
    modify_data = input('수정할 내용을 입력하세요 : ')
    book[name][modify_num-1] = modify_data
    print()
    print('수정이 완료되었습니다.')


# menu mode 5 -> data update 반드시 필요
def del_entry(book):
    name = input('삭제할 사람의 이름을 입력하세요 : ')
    if name not in book.keys():
        print('{name} 님은 목록에 없습니다.')
        return
    
    del book[name]
    print(f'{name} 님이 삭제되었습니다.')


def save(book,fpath,encoding, book_index):
    with open(fpath, 'wt', encoding=encoding) as f:
        f.write(','.join(book_index) + '\n')
        for k,v in book.items():
            line = k + ',' + ','.join(v) + '\n'
            f.write(line)


def exit(book, fpath, encoding, book_index):
    if input('정말로 종료하시겠습니까? y/n: ') == 'n':
        return
    save(book, fpath, encoding, book_index)
    sys.exit(0)


def run(menu, book, config, book_index):
    if menu == 1:  # 목록
        print_book(book)
    elif menu == 2: # 상세보기
        print_detail(book)
    elif menu == 3: # 추가
        add_entry(book)
    elif menu == 4: # 수정
        update_entry(book)
    elif menu == 5: #삭제
        del_entry(book)
    elif menu == 6: # 종료
        exit(book, config['FNAME'], config['ENCODING'], book_index)
    else:
        print('잘못 선택하였습니다. 다시 선택해 주세요.')


def main():
    try:
        book, config, book_index = init()
        while True:
            menu = select_menu()
            run(menu, book, config, book_index)
    except Exception as e:
        print('예외 발생', e)
        traceback.print_stack() # 예외 위치까지 오는데 거친 함수 목록을 출력
        traceback.print_exc() # 구체적인 예외 내용을 출력

main()

# refactoring
# 구조화 (structure/계층화) / Tree 구조   <--->   평탄(평평)하다 flat

# main
#     init
#         load_config
#         load
#         make_book
#     select_menu
#     run
#         add_entry
#         del_entry
#         :
#         :


# 이차원 딕셔너리 만드는 것 -> 나중에 해보기
""" def make_book(lines):
    book = {}
    index_name = lines[0].replace('\ufeff','').strip().split(',')
    # print(index_name)
    # index_name = lines[0].split(',')
    for line in lines[1:]:
        line = line.replace('\n','').split(',')
        name = line[0]
        print(name)
        print(line)
        # for ix, i_n in enumerate(index_name[1:]):
        #     book[name][i_n] = line[ix]
        # book[index_name[0]] = line.split(',')[0]
        # book[index_name[1]] = line.split(',')[1]
        # book[index_name[2]] = line.split(',')[2]
        # book[index_name[3]] = line.split(',')[3]
    
    return book """
