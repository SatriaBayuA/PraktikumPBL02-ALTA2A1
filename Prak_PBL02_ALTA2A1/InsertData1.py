import sqlite3

koneksi_ke_DB = sqlite3.connect("cars.db")
k = koneksi_ke_DB.cursor()

k.execute("DELETE FROM TBCars")

k.execute("""
INSERT INTO TBCars (id, name, brand, model, price)
VALUES('101', 'Red Car', 'Honda', 'CRV', 20000)
""")

k.execute("""
INSERT INTO TBCars (id, name, brand, model, price)
VALUES('102', 'Blue Car', 'Toyota', 'Fortuner', 35000)
""")

k.execute("""
INSERT INTO TBCars (id, name, brand, model, price)
VALUES ('103', 'Silver Car', 'Mitsubishi', 'Pejero', 36000)
""")

koneksi_ke_DB.commit()
koneksi_ke_DB.close()
#Satria Bayu Ananta (036)
