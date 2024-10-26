def optimize_dorm_allocation(students, dormitories):

    allocation = {}
    
    for student in students:
        # 找到一个合适的宿舍
        for dormitory in dormitories:
            if dormitory.current_occupants < dormitory.capacity:
                allocation[student.id] = dormitory.id
                dormitory.current_occupants += 1  # 更新当前入住人数
                break
                
    return allocation
