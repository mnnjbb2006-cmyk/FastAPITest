from fastapi import FastAPI, HTTPException
from typing import List, Annotated, Optional
from pydantic import BaseModel, Field


class BookBase(BaseModel):
    title: Annotated[str, Field(min_length=3, max_length=100)]
    author: Annotated[str, Field(min_length=3, max_length=100)]
    year: Annotated[int, Field(gt=1000, le=2026)]
    publisher: Annotated[str, Field(min_length=3, max_length=100)]


class Book(BookBase):
    book_id: int


class BookUpdate(BaseModel):
    title: Optional[Annotated[str, Field(min_length=3, max_length=100)]] = None
    author: Optional[Annotated[str, Field(
        min_length=3, max_length=100)]] = None
    year: Optional[Annotated[int, Field(min=1000, max=2026)]] = None
    publisher: Optional[Annotated[str, Field(
        min_length=3, max_length=100)]] = None


books = [
    Book(book_id=1, title='Weapons of Math Destruction',
         author="Cathy O'Neil", year=2016, publisher='Penguin Books, Limited'),
    Book(book_id=2, title='Saxon Math 8/7', author='Stephen Hake',
         year=2003, publisher='Saxon Publishers, Incorporated'),
    Book(book_id=3, title='Mathematics for Class 10', author='R. D. Sharma',
         year=2017, publisher='Dhanpat Rai Publications'),
    Book(book_id=4, title='A Mind for Numbers', author='Barbara A. Oakley',
         year=2014, publisher='Jeremy P. Tarcher/Penguin'),
    Book(book_id=5, title='Naked Statistics', author='Charles J. Wheelan',
         year=2013, publisher='Brilliance Audio'),
    Book(book_id=6, title='Everything and more', author='David Foster Wallace',
         year=2003, publisher='Norton & Company, Incorporated, W. W.'),
    Book(book_id=7, title='The Boy who Loved Math',
         author='Deborah Heiligman', year=2013, publisher='Roaring Brook Press'),
    Book(book_id=8, title='Math for All Seasons', author='Greg Tang',
         year=2001, publisher='Turtleback Books Distributed by Demco Media'),
    Book(book_id=9, title='Saxon Math Homeschool 7/6',
         author='Hake Saxon', year=2004, publisher='Saxon Publishers'),
    Book(book_id=10, title='The Numberverse', author='Andrew Day',
         year=2014, publisher='Crown House Publishing LLC'),
    Book(book_id=11, title='I wish i knew that', author='Steve Martin',
         year=2011, publisher="Reader's Digest Association"),
    Book(book_id=12, title='Math Fables', author='Greg Tang',
         year=2004, publisher='Scholastic Press'),
    Book(book_id=13, title='Saxon Math 1 (Saxon Math Grade 1)', author='Nancy Larson',
         year=2004, publisher='Saxon, a trademark of Harcourt Achieve'),
    Book(book_id=14, title='The Indian clerk', author='David Leavitt',
         year=2007, publisher='Yediʻot aḥaronot'),
    Book(book_id=15, title='Probability and statistics with R',
         author='María Dolores Ugarte', year=2008, publisher='Chapman and Hall/CRC'),
    Book(book_id=16, title='Homeschool packet for Saxon Math 8/7, an incremental development',
         author='Stephen Hake', year=2002, publisher='Saxon'),
    Book(book_id=17, title='The Man of Numbers', author='Keith J. Devlin',
         year=2011, publisher='Walker & Company'),
    Book(book_id=18, title='Abstract algebra', author='William Paulsen',
         year=2010, publisher='CRC Press LLC'),
    Book(book_id=19, title='Saxon Math', author='Stephen Hake',
         year=2003, publisher='Saxon Pub')
]
poped_ids = []

api = FastAPI()


@api.get("/", response_model=List[Book])
def find_books(q: Annotated[str, Field(min_length=3, max_length=100)]) -> List[Book]:
    q_lower = q.lower()
    fbooks: List[Book] = []
    for book in books:
        if q_lower in book.title.lower() or q_lower in book.author.lower():
            fbooks.append(book)
    return fbooks


@api.put("/update/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookUpdate) -> Book:
    for b in books:
        if b.book_id == book_id:
            if book.title is not None:
                b.title = book.title
            if book.author is not None:
                b.author = book.author
            if book.year is not None:
                b.year = book.year
            if book.publisher is not None:
                b.publisher = book.publisher
            return b
    raise HTTPException(status_code=404, detail="Book not found")


@api.post("/create/", response_model=BookBase)
def create_book(book: BookBase) -> BookBase:
    book_id = len(books) + 1
    for i in poped_ids:
        book_id = min(book_id, i)
    new_book = Book(book_id=book_id, title=book.title,
                    author=book.author, year=book.year, publisher=book.publisher)
    books.append(new_book)
    return new_book
