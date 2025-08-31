from typing import List, Dict, Optional
from datetime import datetime

#개별 책 정보와 상태를 저장
class Book:
    def __init__(self, title: str, author: str, isbn: str, year: int):
        self._title = title #책 제목
        self._author = author #책 저자
        self._isbn = isbn #책 isbn
        self._year = year #책 년도
        self._is_borrowed = False #대출 여부 저장

    def borrow(self): #대출 처리
        self._is_borrowed = True 
    
    def return_book(self): #반납 처리
        self._is_borrowed = False 

    def is_available(self): #대출 가능 여부
        return not self._is_borrowed 
    
    def get_info(self): #책 정보
        return {
            "제목": self._title,
            "저자": self._author,
            "ISBN": self._isbn,
            "출판연도": self._year,
            "대출가능": self.is_available()
        }
    
    def __str__(self):
        status = "대출가능" if self.is_available() else "대출중"
        return f"{self._title}/ {self._author}/{self._isbn}/{self._year}/{status} "

#도서관의 전체 책 목록 관리 + 대출/반납 기능 제공
class Library:
    def __init__(self): # 도서 리스트 
        self._books = []  

    def add_book(self, book): #도서 추가
        self._books.append(book) 

    def remove_book(self, isbn): #도서 삭제
        for b in self._books: 
            if b._isbn == isbn: 
                self._books.remove(b) 
                return f"{b._title} 도서가 삭제되었습니다."
        return "해당 ISBN의 도서를 찾을 수 없습니다."

    def search_books(self, keyword): #도서 검색
        return [book for book in self._books if book.matches(keyword)]

    def borrow_book(self, isbn): #도서 대출
        for book in self._books:
            if book._isbn == isbn:
                if book.is_available():
                    book.borrow()
                    return f"{book._title} 대출 완료"
                else:
                    return "이 도서는 현재 대출 중입니다."
        return "도서를 찾을 수 없습니다."

    def return_book(self, isbn): #도서 반납
        for book in self._books:
            if book._isbn == isbn:
                if not book.is_available():
                    book.return_book()
                    return f"{book._title} 반납 완료"
                else:
                    return "이 도서는 대출된 상태가 아닙니다."
        return "도서를 찾을 수 없습니다."

    def list_all_books(self):
        return [str(book) for book in self._books]

#회원 기본정보 및 대출목록 관리
class Member:
    def __init__(self, member_id: str, name: str):
        self._member_id = member_id #회원 고유 ID
        self._name = name #회원 이름
        self._borrowed_books = []  # 현재 회원들이 대출중인 책 저장 리스트

    def borrow_book(self, book): #책 대출
        self._borrowed_books.append(book)

    def return_book(self, book): #책 반납
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)

    def get_borrowed_books(self): #어떤 책 대출했는지 
        return self._borrowed_books

    def __str__(self):
        return f"회원 이름: {self._name}, ID: {self._member_id}"

# 책 생성
book1 = Book("호의에 대하여", "문형배", "1111", 2025)
book2 = Book("다크 심리학", "다크 사이드 프로젝트", "2222", 2024)

# 도서관 객체 생성
lib = Library()
lib.add_book(book1)
lib.add_book(book2)

# 도서 대출
print(lib.borrow_book("1111"))  # 호의에 대하여 대출 완료
print(lib.borrow_book("1111"))  # 이 도서는 현재 대출 중입니다.

# 도서 반납
print(lib.return_book("1111"))  # 호의에 대하여 반납 완료
print(lib.return_book("1111"))  # 이 도서는 대출된 상태가 아닙니다.

# 회원 생성
member = Member("001", "김수현")
member.borrow_book(book1)
print(member.get_borrowed_books())  # 대출한 책 목록 출력
