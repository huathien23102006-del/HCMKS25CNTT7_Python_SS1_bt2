# print("- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ---")
# name_patient = input("Nhập tên bệnh nhân: ")
# weight = input("Nhập cân nặng bệnh nhân: ")
# print("- KIỂM TRA DỮ LIỆU LƯU TRỮ -")
# print("Bệnh nhân : , name_patient)
# print("Cân nặng dã nhập", weight)
# # Trường nhóm IT viết thêm dòng này để kiểm tra dữ liệu của cân nặng
# print("CẢNH BÁO - Kiểu dữ liệu dang lưu là : , type (weight))

# vốn dĩ input được lập trình sẵn khi lưu trữ sẽ là kiểu dữ liệu chuỗi khi được gán
# các giá trị khác thì giá trị trong input sẽ được thay đổi theo kiểu giá trị được gán vào
# vì không gán giá trị cho biến do đó dẫn đến việc xử lý kiểu dữ liệu không chính xác

print("- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ---")
name_patient = input("Nhập tên bệnh nhân: ")
weight = float(input("Nhập cân nặng bệnh nhân: "))
print("- KIỂM TRA DỮ LIỆU LƯU TRỮ -")
print("Bệnh nhân :" , name_patient)
print("Cân nặng dã nhập", weight)
# Trường nhóm IT viết thêm dòng này để kiểm tra dữ liệu của cân nặng
print("CẢNH BÁO - Kiểu dữ liệu dang lưu là :" , type (weight))