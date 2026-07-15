import csv
class Titanicdataloader:
    def __init__(self, file_path, batch_size=32):
        self.file_path = file_path
        self.batch_size = batch_size
        self.file = None
        self.header = None
    def __enter__(self):
        print(f"opening the file: {self.file_path}")
        self.file = open(self.file_path, mode='r', encoding='utf-8', newline='')
        self.reader = csv.reader(self.file)
        self.header=next(self.reader)
        return self
    def __exit__(self, exc_type, exc_value, tb):
        print(f"closs the file: {self.file}")
        if self.file:
            self.file.close()
        if exc_type is not None:
            print(f"[ERROR]{exc_type.__name__}:{exc_value} ")
        return False
    def batches(self):
        batch = []
        for row in self.reader:
            if not row:
                continue
            batch.append(row)
            if len(batch) == self.batch_size:
                yield batch
                batch = []
        if batch:
            yield batch
    def row(self):
        for row in self.reader:
            if row:
                yield dict(zip(self.header, row))
if __name__ == "__main__":
    file_path = "Titanic-Dataset.csv"
    with Titanicdataloader(file_path, batch_size=16) as loader:
        print("columns: ", loader.header)
        for batch_num, batch in enumerate(loader.batches(),start=1):
            print(f"Batch: {batch_num}: {len(batch)} data loading")
            for i, row in enumerate(batch, start=1):
                print(f"Row {i}: {row}")
            if batch_num == all:
                break
        
