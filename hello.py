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

# def create_db(db):
#     conn = connect()
#     cursor = conn.cursor()
#     cursor.execute("create database if not exists "+db)
#     cursor.execute("use "+db)
#     print("Cơ sở dữ liệu là "+db)
#     cursor.execute('CREATE TABLE IF NOT EXISTS users(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255) NOT NULL,birthdate DATE)')
#     return conn


def insert(con):
    try:
        name = input("Nhập tên của bạn: ")
        birthday = datetime.datetime.strptime(input("Nhập têm của bạn  (YYYY-MM-DD): "),"%d/%m/%Y").date()
        cursor = con.cursor()
        cursor.execute("insert into users(name,birthdate) values(%s, %s)",(name,birthday))
        con.commit()
        print("thêm thành công")
    except mysql.connector.Error as e:
        print(f"Lỗi khi chèn bản ghi: {e}")
    finally:
        cursor.close()

def delete(con):
    try:
        id = int(input("Nhập mã sinh viên muốn xoá: "))
        print(id)
        cursor = con.cursor()
        cursor.execute("select * from users WHERE id=%s",(id,))
        user = cursor.fetchone()
        if user :
            cursor.execute("delete from users WHERE  id=%s",(id,))
            con.commit()
            print("Xoá thành công")
        else :
            print("Mã không tồn tại")
    except mysql.connector.Error as e:
        print(f"Lỗi khi chèn bản ghi: {e}")
        print("Mã không tồn tại")
    finally:
        cursor.close()

def update(con):
    try:
        id = int(input("Nhập mã sinh viên muốn xoá: "))
        print(id)
        cursor = con.cursor()
        cursor.execute("select * from users WHERE id=%s",(id,))
        user = cursor.fetchone()
        if user :
            name = input("Nhập tên của bạn: ")
            birthday = datetime.datetime.strptime(input("Nhập têm của bạn  (YYYY-MM-DD): "),"%d/%m/%Y").date()
            cursor.execute("update users set name=%s,birthdate=%s where id = %s",(name,birthday,id,))
            con.commit()
            print("thành công")
        else :
            print("Mã không tồn tại")
    except mysql.connector.Error as e:
        print(f"Lỗi khi chèn bản ghi: {e}")
        print("Mã không tồn tại")
    finally:
        cursor.close()

def getAll(con):
    try:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM users order by id desc")
        result = cursor.fetchall()
        print("---------DANH SÁCH SINH VIÊN------------")
        for e in result:
            print(e[0],"\t",e[1],"\t",e[2],"\t")
    except mysql.connector.Error as e:
        print(f"Lỗi: {e}")
    finally:
        cursor.close()

    
def show_menu():
    print("===== MENU =====")
    print("1. Xem danh sách")
    print("2. Thêm mục mới")
    print("3. Sửa mục")
    print("4. Xóa mục")
    print("5. Thoát")
    print("================")



def inputExample():
    con = connect();
    while True:
        # Hiển thị menu
        show_menu()
        choice = input("Nhập lựa chọn của bạn: ")
        if choice == '1':
            print("Bạn đã chọn xem danh sách.")
            getAll(con)
        elif choice == '2':
            print("Bạn đã chọn thêm mục mới.")
            insert(con)
        elif choice == '3':
            print("Bạn đã chọn sửa mục.")
            update(con)
        elif choice == '4':
            print("Bạn đã chọn xóa mục.")
            delete(con)
        elif choice == '5':
            print("Bạn đã chọn thoát.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

inputExample()