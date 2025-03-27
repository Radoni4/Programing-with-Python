# 1.	Брой страници в текущата книга – цяло число;
# 2.	Страници, които може да прочита за 1 час – цяло число;
# 3.	Броя на дните, за които трябва да прочете книгата – цяло число;

book_pages = int(input())
pages_for_hour = int(input())
needed_days = int(input())
total_time = book_pages / pages_for_hour
result = total_time / needed_days
print (result)
