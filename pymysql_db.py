import pymysql

# Inisiasi Database
db = pymysql.connect(host="localhost", user="root", password="")
cursor = db.cursor()

# Buat Database
cursor.execute("CREATE DATABASE IF NOT EXISTS db_pymysql")

# Menggunakan Database
cursor.execute("USE db_pymysql")

# Membuat Tabel
mysql_create_table = "CREATE TABLE IF NOT EXISTS tbl_user (id_user int(11) NOT NULL, nama varchar(20) NOT NULL)"
cursor.execute(mysql_create_table)

# Menggunakan Database
cursor.execute("USE db_pymysql")

# Mengisi Tabel
# mysql_insert_data = "INSERT INTO tbl_user (id_user, nama) VALUES (%s, %s)"
# value_table = (6, "Defan")
# try:
#     cursor.execute(mysql_insert_data, value_table)
#     db.commit()
# except:
#     print("Sesuatu Salah")
#     db.rollback()
# finally:
#     db.close()
#     print("-")

# Hapus Data
# mysql_delete_data = "DELETE FROM tbl_user WHERE %s%s"
# nama_kolom = "id_user="
# value_kolom = 5
# try:
#     cursor.execute(mysql_delete_data % (
#         nama_kolom, value_kolom))
#     db.commit()
# except:
#     print("Sesuatu Salah")
#     db.rollback()
# finally:
#     db.close()
#     print("-")

# Ubah Data
mysql_delete_data = "UPDATE nama_tabel set kolom1/field1 = data_baru1, kolom2/field2 = data_baru2 WHERE [kondisi];"
