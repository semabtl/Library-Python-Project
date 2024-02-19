class Library:

# Constructor
    def __init__(self):
         self.f = open("books.txt", "a+")

# Tüm kitapları listeleyen metod
    def list_all_books(self):
        # Dosyadaki bilgiler okunarak liste içine kaydedilir.
        self.books = []
        self.f.seek(0)
        lines = self.f.read().splitlines()
        for line in lines:
            current_line = line.strip().split(",")
            book_information = {
                "book_name": current_line[0],
                "author": current_line[1],
                "release_date": current_line[2],
                "number_of_pages": current_line[3]
            }
            self.books.append(book_information)

        # Liste boş değilse kitapların adları ve yazarlarının adları çıktı olarak verilir.
        if self.books:
            for book in self.books:
                print("Book:", book['book_name'], "-" , "Author:", book['author'])
        else:
            print("There are no books to show!")

# Kitap eklemek için metod            
    def add_book(self):
        # Kitabın bilgileri kullanıcıdan alınarak books.txt dosyasına eklenir.
        print("Please complete the following information: ")
        book_name = input("Book name:")
        author = input("Author:")
        release_date = input("Release year:")
        number_of_pages = input("Number of pages:")
        new_book_information = book_name + "," + author + "," + release_date + "," + number_of_pages
        self.books.append(new_book_information)
        self.f.write(new_book_information)

# Kitap silmek için metod    
    def remove_book(self):
        # Silinecek olan kitabın adı kulanıcıdan alınır.
        book_to_delete = input("Enter the name of the book to remove: ")

        # Dosyadaki kitap bilgileri okunarak liste içine kaydedilir.
        self.books = []
        self.f.seek(0)
        lines = self.f.read().splitlines()
        for line in lines:
            current_line = line.strip().split(",")
            book_information = {
                "book_name": current_line[0],
                "author": current_line[1],
                "release_date": current_line[2],
                "number_of_pages": current_line[3]
            }
            self.books.append(book_information)

        # Kitap mevcutsa listeden kaldırılır. Değilse uyarı verilir.
        removed = False
        for book in self.books:
            if book['book_name'].lower() == book_to_delete.lower() :
                self.books.remove(book)
                removed = True
                print("Book removed.")
                break
        if removed == False:
                print("There is no book named", book_to_delete)    
                
        # Dosyanın içindekiler silinerek, güncellenmiş liste tekrar dosyaya yazılır.
        self.f.seek(0)
        self.f.truncate()

        for book in self.books:
            book_information = book['book_name'] + "," + book['author'] + "," + book['release_date'] + "," + book['number_of_pages']
            self.f.write(book_information +"\n")

# Destructor
    def __del__(self):
        self.f.close()

# Library sınıfına ait nesne oluşturulur ve kullanıcı seçimine göre ilgili metod çağrılır.
lib = Library()
while True:
    print("\n***MENU***\n1) List Books\n2) Add Book\n3) Remove Book\nq) Quit")
    choice = input("Please choose an option from the menu: ")
    if choice == "1":
        lib.list_all_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "q":
        break
    else:
        print("Please choose a valid option.")