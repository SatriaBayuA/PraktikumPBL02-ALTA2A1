import sqlite3
#Satri Bayu Ananta (036)
koneksi_ke_DB = sqlite3.connect("cars.db")
k = koneksi_ke_DB.cursor()

k.execute("""
            DELETE FROM TBCars 
            WHERE
                id = 103
    """)

k.execute("SELECT * FROM TBCars")
print(k.fetchall())

koneksi_ke_DB.commit()
koneksi_ke_DB.close()
