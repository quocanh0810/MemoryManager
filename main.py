from memory_pool_manager import MemoryPoolManager

def main():
    pool_size = 12 * 4  # 12 phần tử kiểu int (giả sử int là 4 bytes)
    data_size = 4       # Kích thước của int
    memory_manager = MemoryPoolManager(pool_size, data_size)

    print(f"Free remaining space: {memory_manager.remaining_space()}")

    allocated_chunks = []
    for i in range(12):
        chunk = memory_manager.allocate()
        if chunk:
            chunk.get_data().value = i  # Gán giá trị để mô phỏng dữ liệu
            allocated_chunks.append(chunk)
        print(f"Allocated chunk {i}, Free remaining space: {memory_manager.remaining_space()}")

    # Giải phóng một chunk và kiểm tra lại bộ nhớ
    memory_manager.free(allocated_chunks[-1])
    print(f"After freeing one chunk, Free remaining space: {memory_manager.remaining_space()}")

    # Cấp phát lại một chunk để kiểm tra lại chức năng
    chunk = memory_manager.allocate()
    print(f"Reallocated one chunk, Free remaining space: {memory_manager.remaining_space()}")

    # Giải phóng tất cả và kiểm tra lại dung lượng còn lại
    memory_manager.clear()
    print(f"After clearing, Free remaining space: {memory_manager.remaining_space()}")

if __name__ == "__main__":
    main()
