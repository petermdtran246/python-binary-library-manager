import struct

RECORD_SIZE = 60 #fixed record size
FILE_NAME = 'library.dat'

def pack_record(book_id, title, author, stock):
    title = title.strip().encode().ljust(30)
    author = author.strip().encode().ljust(20)
    return struct.pack('i30s20si', book_id, title, author, stock)

def unpack_record(record_bytes):
    book_id, title, author, stock = struct.unpack('i30s20si', record_bytes)
    return {
        'Book ID': book_id,
        'Title': title.decode().strip(),
        'Author': author.decode().strip(),
        'Stock': stock
    }

def add_book():
    book_id = int(input('Enter Book ID: '))
    title = input('Enter Title: ')
    author = input('Enter Author: ')
    stock = int(input('Enter Stock'))

    record = pack_record(book_id, title, author, stock)

    with open(FILE_NAME, 'ab') as f:
        f.write(record)
        print('Book added successfully')
    
def view_books():
    with open(FILE_NAME, 'rb') as f:
        print('\n === Book Record ===')
        while True:
            record = f.read(RECORD_SIZE)
            if not record:
                break
            book = unpack_record(record)
            print(book)

def search_book():
    book_id = int(input('Enter Book ID to search: '))

    with open(FILE_NAME, 'rb') as f:
        while True:
            record = f.read(RECORD_SIZE)
            if not record:
                break
            book = unpack_record(record)
            if book['Book ID'] == book_id:
                print('Book Found:', book)
                return
        print('Book not found!')

def delete_book():
    book_id = int(input('Enter Book ID to delete: '))
    found = False

    with open(FILE_NAME, 'r+b') as f:
        index = 0
        
        while True:
            f.seek(index * RECORD_SIZE)
            record = f.read(RECORD_SIZE)
            if not record:
                break
            book = unpack_record(record)
            if book['Book ID'] == book_id:
                f.seek(index * RECORD_SIZE)
                updated_record = pack_record(
                    book['Book ID'],
                    book['Title'],
                    book['Author'],
                    0
                )

                f.write(updated_record)

                found = True
                print('Book deleted successfully (Stock set to 0).')

                break

            index += 1
    if not found:
        print('Book not found!')
    
    




