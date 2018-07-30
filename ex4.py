# 一共100辆车
cars = 100
# 一辆车四个座位
space_in_a_car = 4
# 一共30位司机
drivers = 30
# 共90名乘客
passengers = 90
# 未运行的车辆数
cars_not_driven = cars - drivers
# 在运行的车辆数
cars_driven = drivers
# 车辆一共可容纳的乘客数量
carpool_capacity = cars_driven * space_in_a_car
# 平均每辆车载客数
average_passengers_per_car = passengers / cars_driven

print("there are", cars, "cars available")
print("there are only", drivers, "drivers available")
print("there will be", cars_not_driven, "emplty cars today")
print("we can teansport", carpool_capacity, "people today")
print("we have", passengers, "to carpool today")
print("we need to put about", average_passengers_per_car, "in each car")

print(cars == drivers)