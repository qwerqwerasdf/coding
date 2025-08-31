address_book = {
    "김수현" : {
        "전화번호": "010-0000-0000",
        "이메일": "kim@kakao.com",
        "주소": "서울특별시"
    },
    "김태니" : {
        "전화번호": "010-1111-1111",
        "이메일": "tae@kakao.com",
        "주소": "광주광역시"
    }
}

def add_contact(name, phone, email, address):
    if name in address_book:
        print(f"{name}은 이미 존재합니다.")
    else:
        address_book[name] = {
            '전화번호': phone,
            '이메일': email,
            '주소':address
        }
        print(f"{name}의 연락처가 추가되었습니다.")

def delete_contact(name):
    if name in address_book:
        del address_book [name]
        print(f"{name}의 연락처가 삭제되었습니다.")
    else:
        print(f"{name}은 주소록에 없습니다.")

def search_contact(name):
    if name in address_book:
        print(f"{name}의 정보: {address_book[name]}")
    else:
        print(f"{name}을 찾을 수 없습니다.")

def update_contact(name, phone=None, email=None, address=None):
    if name in address_book:
        if phone:
            address_book[name] ['전화번호'] = phone
        if email:
            address_book[name] ['이메일'] = email
        if address:
            address_book[name] ['주소'] = address
        print(f"{name}의 정보가 업데이트 되었습니다.")
    else:
        print(f"{name}을 찾을 수 없습니다.")

def show_all_contacts():
    if not address_book:
        print("연락처가 없습니다.")
    else:
        for name, info in address_book.items():
            print(f"이름: {name}")
            for key, value in info.items():
                print(f" {key}: {value}")
            print("-" * 30)

while True:
    print("\n--- 주소록 프로그램 ---")
    print("1. 연락처 추가")
    print("2. 연락처 삭제")
    print("3. 연락처 검색")
    print("4. 연락처 수정")
    print("5. 모든 연락처 보기")
    print("0. 종료")

    choice = input("선택: ")

    if choice == "1":
        name = input("이름: ")
        phone = input("전화번호: ")
        email = input("이메일: ")
        address = input("주소: ")
        add_contact(name, phone, email, address)

    elif choice =="2":
        name = input("삭제할 이름: ")
        delete_contact(name)

    elif choice =="3":
        name = input("검색할 이름: ")
        search_contact(name)
    
    elif choice =="4":
        name = input("수정할 이름: ")
        phone = input("새 전화번호: ")
        email = input("새 이메일: ")
        address = input("새 주소: ")
        update_contact(name, phone, email, address)
    
    elif choice =="5":
        show_all_contacts()
    
    elif choice =="0":
        print("프로그램 종료")
        break

    else:
        print("잘못된 입력입니다.")
