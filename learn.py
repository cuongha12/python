import mysql.connector
import datetime
def connect():
    connection = mysql.connector.connect(
         host="localhost", 
        user="root",
        port=3306,
        password="Cuongha12@",
        database="hello"
    )
    return connection

def show_menu():
    print("===== MENU =====")
    print("1. Xem danh sách")
    print("2. Thêm mục mới")
    print("3. Sửa mục")
    print("4. Xóa mục")
    print("5. Thoát")
    print("================")

def getId(conn,id):
    try:
        cursor = conn.cursor()
        cursor.execute("select * from users where id = %s",(id,))
        # cursor.execute("SELECT * FROM users WHERE column_name LIKE %s", ('%'+search_term+'%',))

        result = cursor.fetchone()
        return result
    except mysql.connector.Error as e:
        print(e)
    finally:
        cursor.close()
    

def insert(conn):
    try:
        name = input("Nhập tên của bạn: ")
        birthday = datetime.datetime.strptime(input("Nhập ngày sinh của bạn  (YYYY-MM-DD): "),"%d/%m/%Y").date()
        cursor = conn.cursor()
        cursor.execute("insert into users(name,birthdate) values(%s,%s)",(name,birthday))
        conn.commit()
        print("Thêm dữ liệu thành công")
    except mysql.connector.Error as e:
        print(f"Lỗi khi chèn bản ghi: {e}")
    finally:
        cursor.close()

def getAll(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("select * from users order by id desc")
        result = cursor.fetchall()
        print("---------DANH SÁCH SINH VIÊN------------")
        print("{:<15} {:>15} {:>25}".format("Mã sinh viên", "Tên", "Ngày sinh"))
        for e in result:
            print("{:<15} {:>25} {:>25}".format(e[0],e[1],e[2].strftime("%d/%m/%Y")))
    except mysql.connector.Error as e:
         print(f"Lỗi khi chèn bản ghi: {e}")
    finally:
        cursor.close()

def update(conn):
    try:
        id = int(input("Nhập mã sinh viên của bạn: "))
        cursor = conn.cursor()
        user = getId(conn,id)
        if user :
            name = input("Nhập tên của bạn: ")
            birthday = datetime.datetime.strptime(input("Nhập ngày sinh của bạn  (YYYY-MM-DD): "),"%d/%m/%Y").date()
            cursor.execute("update users set name = %s,birthdate = %s WHERE  id=%s",(name,birthday,id))
            conn.commit()
            print("Update thành công")
        else :
            print("Mã không tồn tại")
    except mysql.connector.Error as e:
         print(f"Lỗi khi chèn bản ghi: {e}")
    finally:
        cursor.close()

def delete(conn):
    try:
        id = int(input("Nhập mã sinh viên của bạn: "))
        cursor = conn.cursor()
        user = getId(conn,id)
        if user :
            cursor.execute("delete from users WHERE  id=%s",(id,))
            conn.commit()
            print("Xoá thành công")
        else :
            print("Mã không tồn tại")
    except mysql.connector.Error as e:
         print(f"Lỗi khi chèn bản ghi: {e}")
    finally:
        cursor.close()

def main():
    conn = connect()
    while True:
        show_menu()
        choice = input("Nhập lựa chọn của bạn: ")
        if choice == '1':
            print("Bạn đã chọn xem danh sách.")
            getAll(conn)
        elif choice == '2':
            print("Bạn đã chọn thêm mục mới.")
            insert(conn)
        elif choice == '3':
            print("Bạn đã chọn sửa mục.")
            update(conn)
        elif choice == '4':
            print("Bạn đã chọn xóa mục.")
            delete(conn)
        elif choice == '5':
            print("Bạn đã chọn thoát.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
main()

# pip install mysql-connector-python