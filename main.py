from collections import deque

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._percolate_up(len(self.heap) - 1)

    def _percolate_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] < self.heap[index]:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break

    def extract_max(self):
        if len(self.heap) == 0:
            return None

        max_item = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]

        self._percolate_down(0)

        return max_item

    def _percolate_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._percolate_down(largest)

    def get_max(self):
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            return None

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursively(data, self.root)

    def _insert_recursively(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = TreeNode(data)
            else:
                self._insert_recursively(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = TreeNode(data)
            else:
                self._insert_recursively(data, current_node.right)
        else:
            print("Data already exists in the tree.")

    def search(self, data):
        return self._search_recursively(data, self.root)

    def _search_recursively(self, data, current_node):
        if current_node is None:
            return False
        elif data == current_node.data:
            return True
        elif data < current_node.data:
            return self._search_recursively(data, current_node.left)
        else:
            return self._search_recursively(data, current_node.right)

    def print_tree(self):
        if self.root:
            self._print_tree_recursively(self.root)

    def _print_tree_recursively(self, current_node):
        if current_node:
            self._print_tree_recursively(current_node.left)
            print(current_node.data, end=" ")
            self._print_tree_recursively(current_node.right)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        current_node = self.head

        if current_node is not None and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev = None
        while current_node is not None and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            print("Data tidak ditemukan dalam linked list")
            return

        prev.next = current_node.next
        current_node = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None

    def size(self):
        return len(self.items)
        
    def print_stack(self):
        if not self.is_empty():
            print("Isi stack:")
            for item in reversed(self.items):
                print(item)
        else:
            print("Stack is empty")

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Mengembalikan indeks pertama di mana target ditemukan
    return -1  # Mengembalikan -1 jika target tidak ditemukan dalam list

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def nilai_siswa():
    nilai_mahasiswa = []

    for i in range(3):
        nomor = i + 1
        print("Mahasiswa nomor ", nomor)
        nama = input("Masukkan nama mahasiswa: ")
        nilai_quis = float(input("Masukkan nilai quis: "))
        nilai_mid = float(input("Masukkan nilai mid: "))
        nilai_semester = float(input("Masukkan nilai semester: "))
        print(f"Berhasil menambahkan data nilai mahasiswa {nama}")
        print("")
        nilai_mahasiswa.append([nomor, nama, nilai_quis, nilai_mid, nilai_semester])

    for data in nilai_mahasiswa:
        total_nilai = data[2] + data[3] + data[4]
        nilai_rata = total_nilai / 3
        data.extend([total_nilai, nilai_rata])

    header = ["Nomor", "Nama", "Nilai Quis", "Nilai Mid", "Nilai Semester", "Total Nilai", "Nilai Rata"]

    print("{:<9} {:<15} {:<11} {:<9} {:<15} {:<11} {:<11}".format(*header))
    for data in nilai_mahasiswa:
        print("{:<9} {:<15} {:<11} {:<9} {:<15} {:<11} {:<11}".format(*data))

def deque_and_queue():
    pilihan_deque_queue = {
        1: "Deque",
        2: "Queue",
        3: "Kembali"
    }

    while True:
        print("\nPilih tipe data struktur:")
        for key, value in pilihan_deque_queue.items():
            print(f"{key}. {value}")

        choice = int(input("Masukkan pilihan (1-3): "))

        if choice == 3:
            print("Kembali ke menu utama.")
            break

        if choice == 1:
            deque_operations()
        elif choice == 2:
            queue_operations()


def deque_operations():
    dq = deque()

    while True:
        print("\nDeque Operations:")
        print("1. Tambahkan elemen di depan")
        print("2. Tambahkan elemen di belakang")
        print("3. Hapus elemen di depan")
        print("4. Hapus elemen di belakang")
        print("5. Tampilkan isi deque")
        print("6. Kembali")

        choice = int(input("Pilih operasi (1-6): "))

        if choice == 1:
            item = input("Masukkan elemen: ")
            dq.appendleft(item)
        elif choice == 2:
            item = input("Masukkan elemen: ")
            dq.append(item)
        elif choice == 3:
            if dq:
                print("Elemen di depan:", dq.popleft())
            else:
                print("Deque kosong.")
        elif choice == 4:
            if dq:
                print("Elemen di belakang:", dq.pop())
            else:
                print("Deque kosong.")
        elif choice == 5:
            print("Isi deque:", list(dq))
        elif choice == 6:
            print("Kembali ke menu utama.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")


def queue_operations():
    q = deque()

    while True:
        print("\nQueue Operations:")
        print("1. Enqueue (Tambahkan elemen)")
        print("2. Dequeue (Hapus elemen)")
        print("3. Tampilkan isi queue")
        print("4. Kembali")

        choice = int(input("Pilih operasi (1-4): "))

        if choice == 1:
            item = input("Masukkan elemen: ")
            q.append(item)
        elif choice == 2:
            if q:
                print("Elemen yang dihapus:", q.popleft())
            else:
                print("Queue kosong.")
        elif choice == 3:
            print("Isi queue:", list(q))
        elif choice == 4:
            print("Kembali ke menu utama.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")


def main():
    pilihan = {
        1: "Data Siswa",
        2: "Liniear Search",
        3: "Binary Search",
        4: "Pengurutan data metode bubble sort",
        5: "Pengurutan data metode selection sort",
        6: "Deque dan Queue",
        7: "Stack",
        8: "Linked List",
        9: "Pohon Tree",
        10: "Heap",
        11: "Keluar"
    }

    while True:
        print("\nPilih perintah:")
        for key, value in pilihan.items():
            print(f"{key}. {value}")

        choice = int(input("Masukkan pilihan (1-11): "))

        if choice == 11:
            print("Program keluar.")
            break

        if choice == 1:
            nilai_siswa()
        elif choice == 2:
            n = int(input("Masukkan jumlah data: "))
            arr = []
            for i in range(n):
                data = int(input(f"Masukkan data ke-{i+1}: "))
                arr.append(data)

            target = int(input("Masukkan data yang ingin dicari: "))

            result = linear_search(arr, target)

            if result != -1:
                print(f"Target {target} ditemukan di indeks {result+1}.")
            else:
                print(f"Target {target} tidak ditemukan dalam list")
        elif choice == 3:
            n = int(input("Masukkan jumlah data: "))
            arr = []
            for i in range(n):
                data = int(input(f"Masukkan data ke-{i+1}: "))
                arr.append(data)
        
            target = int(input("Masukkan data yang ingin dicari: "))
        
            arr.sort()  # Pastikan list sudah terurut sebelum melakukan binary search
        
            result = binary_search(arr, target)
        
            if result != -1:
                print(f"Target {target} ditemukan di indeks {result+1}.")
            else:
                print(f"Target {target} tidak ditemukan dalam list.")
        elif choice == 4:
            n = int(input("Masukkan jumlah data: "))
            arr = []
            for i in range(n):
                data = int(input(f"Masukkan data ke-{i+1}: "))
                arr.append(data)
        
            bubble_sort(arr)
        
            print("Data setelah diurutkan:")
            print(arr)
        elif choice == 5:
            n = int(input("Masukkan jumlah data: "))
            arr = []
            for i in range(n):
                data = int(input(f"Masukkan data ke-{i+1}: "))
                arr.append(data)
        
            selection_sort(arr)
        
            print("Data setelah diurutkan:")
            print(arr)
        elif choice == 6:
            deque_and_queue()
        elif choice == 7:
            stack = Stack()
            while True:
                print("\nMenu:")
                print("1. Push")
                print("2. Pop")
                print("3. Peek")
                print("4. Size")
                print("5. Print stack")
                print("6. Keluar")
        
                choice = input("Masukkan pilihan (1/2/3/4/5): ")
        
                if choice == '1':
                    item = input("Masukkan item yang ingin ditambahkan: ")
                    stack.push(item)
                    print("Item", item, "telah ditambahkan ke dalam stack.")
                elif choice == '2':
                    removed_item = stack.pop()
                    if removed_item:
                        print("Item", removed_item, "telah dihapus dari stack.")
                elif choice == '3':
                    top_item = stack.peek()
                    if top_item:
                        print("Item paling atas di stack:", top_item)
                elif choice == '4':
                    print("Ukuran stack:", stack.size())
                elif choice == '5':
                    stack.print_stack()    
                elif choice == '6':
                    print("Program selesai.")
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
        elif choice == 8:
            linked_list = LinkedList()
            while True:
                print("\nMenu:")
                print("1. Tambahkan node (Append)")
                print("2. Tambahkan node di awal (Prepend)")
                print("3. Hapus node")
                print("4. Cetak linked list")
                print("5. Keluar")
        
                choice = input("Masukkan pilihan (1/2/3/4/5): ")
        
                if choice == '1':
                    data = input("Masukkan data untuk ditambahkan: ")
                    linked_list.append(data)
                    print("Node dengan data", data, "telah ditambahkan ke linked list.")
                elif choice == '2':
                    data = input("Masukkan data untuk ditambahkan di awal: ")
                    linked_list.prepend(data)
                    print("Node dengan data", data, "telah ditambahkan di awal linked list.")
                elif choice == '3':
                    data = input("Masukkan data yang ingin dihapus: ")
                    linked_list.delete_node(data)
                    print("Node dengan data", data, "telah dihapus dari linked list.")
                elif choice == '4':
                    print("Linked list saat ini:")
                    linked_list.print_list()
                elif choice == '5':
                    print("Program selesai.")
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
        elif choice == 9 :
            binary_tree = BinaryTree()
            while True:
                print("\nMenu:")
                print("1. Insert (Masukkan data)")
                print("2. Search (Cari data)")
                print("3. Print Tree (Cetak pohon)")
                print("4. Keluar")
        
                choice = input("Masukkan pilihan (1/2/3/4): ")
        
                if choice == '1':
                    data = int(input("Masukkan data untuk dimasukkan ke dalam pohon: "))
                    binary_tree.insert(data)
                    print("Data", data, "telah dimasukkan ke dalam pohon.")
                elif choice == '2':
                    data = int(input("Masukkan data yang ingin dicari: "))
                    if binary_tree.search(data):
                        print("Data", data, "ditemukan dalam pohon.")
                    else:
                        print("Data", data, "tidak ditemukan dalam pohon.")
                elif choice == '3':
                    print("Pohon saat ini:")
                    binary_tree.print_tree()
                    print()
                elif choice == '4':
                    print("Program selesai.")
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
        elif choice == 10:
                heap = MaxHeap()
                while True:
                    print("\nMenu:")
                    print("1. Insert (Masukkan data)")
                    print("2. Extract Max (Ambil nilai maksimum)")
                    print("3. Get Max (Dapatkan nilai maksimum)")
                    print("4. Size (Ukuran heap)")
                    print("5. Is Empty (Apakah heap kosong)")
                    print("6. Keluar")
            
                    choice = input("Masukkan pilihan (1/2/3/4/5/6): ")
            
                    if choice == '1':
                        data = int(input("Masukkan data untuk dimasukkan ke dalam heap: "))
                        heap.insert(data)
                        print("Data", data, "telah dimasukkan ke dalam heap.")
                    elif choice == '2':
                        max_item = heap.extract_max()
                        if max_item is not None:
                            print("Nilai maksimum yang diambil:", max_item)
                        else:
                            print("Heap kosong.")
                    elif choice == '3':
                        max_item = heap.get_max()
                        if max_item is not None:
                            print("Nilai maksimum dalam heap:", max_item)
                        else:
                            print("Heap kosong.")
                    elif choice == '4':
                        print("Ukuran heap saat ini:", heap.size())
                    elif choice == '5':
                        if heap.is_empty():
                            print("Heap kosong.")
                        else:
                            print("Heap tidak kosong.")
                    elif choice == '6':
                        print("Program selesai.")
                        break
                    else:
                        print("Pilihan tidak valid. Silakan coba lagi.")
if __name__ == "__main__":
    main()