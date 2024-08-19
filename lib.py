#创建字典库
my_dict = {}
# 创建一个包含初始键值对的字典
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}


#访问字典中的值
print(my_dict["name"])

# 添加新的键值对
my_dict['job'] = 'Engineer'

# 更新现有键的值
my_dict['age'] = 26


# 使用 del 删除键值对
del my_dict['city']

# 使用 pop 删除键值对并获取值
job = my_dict.pop('job')




