import json
import os

class json_Ratna:
    def __init__(self, nama_file):
        self.nama_file = nama_file
    
    def baca(self):
        if os.path.exists(self.nama_file):
            with open(self.nama_file, 'r') as file:
                data = json.load(file)
                return data
        else:
            return {}

    def tulis(self, data):
        with open(self.nama_file, 'w') as file:
            json.dump(data, file, indent=5)
    
    def update(self, key, value):
        data = self.baca()
        data[key] = value
        self.tulis(data)
    
    def delete(self, key):
        data = self.baca()
        if key in data:
            del data[key]
            self.tulis(data)
        else:
            print(f"kata kunci '{key}' tidak di mengerti")

# Program utama 
if __name__ == "__main__":
    # menyimpan lokasi file 
    nama_file = 'data.json'
    json_Ratna = json_Ratna(nama_file)
    # menulis data awal
    data_utama = {
        "Nama Buku": "alvaska",
        "Penulis": "MATCHARAY",
        "No.buku": 25675,
        "Genre": "romance"
    }
    json_Ratna.tulis(data_utama)

    # untuk membaca dan menampilkan data
    print("Data After di tulis:")
    print(json_Ratna.baca())

    # update file
    json_Ratna.update("No.buku", 2223)
    print("\nData After di update:")
    print(json_Ratna.baca())

    # delete 
    json_Ratna.delete("Genre")
    print("\nData After di delete:")
    print(json_Ratna.baca())