from fastapi import FastAPI
from typing import List

books = [
    {'title': 'Weapons of Math Destruction', 'author': "Cathy O'Neil",
        'year': '2016', 'publisher': 'Penguin Books, Limited'},
    {'title': 'Saxon Math 8/7', 'author': 'Stephen Hake',
        'year': '2003', 'publisher': 'Saxon Publishers, Incorporated'},
    {'title': 'Mathematics for Class 10', 'author': 'R. D. Sharma',
        'year': '2017', 'publisher': 'Dhanpat Rai Publications'},
    {'title': 'A Mind for Numbers', 'author': 'Barbara A. Oakley',
        'year': '2014', 'publisher': 'Jeremy P. Tarcher/Penguin'},
    {'title': 'Naked Statistics', 'author': 'Charles J. Wheelan',
        'year': '2013', 'publisher': 'Brilliance Audio'},
    {'title': 'Everything and more', 'author': 'David Foster Wallace',
        'year': '2003', 'publisher': 'Norton & Company, Incorporated, W. W.'},
    {'title': 'The Boy who Loved Math', 'author': 'Deborah Heiligman',
        'year': '2013', 'publisher': 'Roaring Brook Press'},
    {'title': 'Math for All Seasons', 'author': 'Greg Tang', 'year': '2001',
        'publisher': 'Turtleback Books Distributed by Demco Media'},
    {'title': 'Saxon Math Homeschool 7/6', 'author': 'Hake Saxon',
        'year': '2004', 'publisher': 'Saxon Publishers'},
    {'title': 'The Numberverse', 'author': 'Andrew Day',
        'year': '2014', 'publisher': 'Crown House Publishing LLC'},
    {'title': 'I wish i knew that', 'author': 'Steve Martin',
        'year': '2011', 'publisher': "Reader's Digest Association"},
    {'title': 'Math Fables', 'author': 'Greg Tang',
        'year': '2004', 'publisher': 'Scholastic Press'},
    {'title': 'Saxon Math 1 (Saxon Math Grade 1)', 'author': 'Nancy Larson',
     'year': '2004', 'publisher': 'Saxon, a trademark of Harcourt Achieve'},
    {'title': 'The Indian clerk', 'author': 'David Leavitt',
        'year': '2007', 'publisher': 'Yediʻot aḥaronot'},
    {'title': 'Probability and statistics with R', 'author': 'María Dolores Ugarte',
        'year': '2008', 'publisher': 'Chapman and Hall/CRC'},
    {'title': 'Homeschool packet for Saxon Math 8/7, an incremental development',
        'author': 'Stephen Hake', 'year': '2002', 'publisher': 'Saxon'},
    {'title': 'The Man of Numbers', 'author': 'Keith J. Devlin',
        'year': '2011', 'publisher': 'Walker & Company'},
    {'title': 'Abstract algebra', 'author': 'William Paulsen',
        'year': '2010', 'publisher': 'CRC Press LLC'},
    {'title': 'Saxon Math', 'author': 'Stephen Hake',
        'year': '2003', 'publisher': 'Saxon Pub'},
]

api = FastAPI()


@api.get("/")
def find_books(q: str) -> dict:
    if not q:
        return {"books": books}

    q_lower = q.lower()
    fbooks: List[dict] = []
    for book in books:
        if q_lower in book["title"].lower() or q_lower in book["author"].lower():
            fbooks.append(book)
    return {"books": fbooks}
