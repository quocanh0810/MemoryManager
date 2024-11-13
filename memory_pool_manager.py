from chunk import Chunk

class MemoryPoolManager:
    def __init__(self, pool_size, data_size):
        self.pool_size = pool_size
        self.data_size = data_size
        self.pool = []
        self.head = None

        # Khởi tạo các chunk và xâu chuỗi chúng vào danh sách trống
        for _ in range(pool_size // data_size):
            new_chunk = Chunk(self.head)
            self.head = new_chunk
            self.pool.append(new_chunk)

    def allocate(self):
        if self.head is None:
            print("Memory pool out of memory")
            return None

        allocated_chunk = self.head
        self.head = self.head.next  # Lấy chunk từ đầu danh sách trống
        return allocated_chunk

    def free(self, chunk):
        chunk.next = self.head
        self.head = chunk

    def remaining_space(self):
        # Tính và trả về số lượng chunk còn trống trong pool.
        free_chunks = 0
        current_chunk = self.head
        while current_chunk is not None:
            free_chunks += 1
            current_chunk = current_chunk.next
        return free_chunks * self.data_size

    def clear(self):
        # Giải phóng tất cả các chunk
        self.head = None
        for chunk in self.pool:
            chunk.next = self.head
            self.head = chunk
