#Danh sách để lưu các công việc
tasks = []
def add_task(task_name):
    """Thêm một công việc vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc mới: '{task_name}'")
#---Điểm bắt đầu của chương trình ---
if __name__=="__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài với Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
