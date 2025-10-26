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
def list_tasks():
    if not tasks:
        print("Danh sách công việc trống!")
        return
    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{i}. {status} {task['name']}")
def delete_task(task_index):
    """Xóa công việc theo chỉ số (0-based)."""
    if 0 <= task_index < len(tasks):
        removed = tasks.pop(task_index)
        print(f"Đã xóa công việc: {removed['name']}")
    else:
        print("Chỉ số không hợp lệ!")