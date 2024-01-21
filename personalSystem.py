import os
# 导入 os 模块
from personal import Personal
# 将personal模块中的Personal类导入
from prettytable import PrettyTable
# 将prettytable中的PrettyTable函数导入


class PersonalManager(object):
    # 驼峰命名法命名命名该类
    def __init__(self):
        # 存储数据所用的列表
        self.personal_list = []
        # 定义一个空的列表

    # 程序入口函数， 即启动程序后执行的函数
    def run(self):
        # 1.加载人员信息
        self.load_personal()
# 检查输入的是不是数字
        while True:
            # 2.显示功能菜单
            self.show_menu()
            try:
                # 3.用户输入功能序号
                menu_num = int(input('请输入您需要的功能序号:'))
            except ValueError:
                print('输入有误，请重新输入:')
                continue
            # 4.根据用户输入的功能序号执行不同的功能
            if menu_num == 1:
                # 添加人员
                self.add_personal()
                # 增加新成员
                self.save_personal()
                # 保存
            elif menu_num == 2:
                # 查询人员信息
                self.search_personal()
            elif menu_num == 3:
                # 保存人员信息
                self.save_personal()
            elif menu_num == 4:
                # 显示所有人员信息
                self.show_personal()
            elif menu_num == 5:
                # 删除人员
                self.del_personal()
                # 删除成员信息
                self.save_personal()
                # 保存信息
            elif menu_num == 6:
                # 修改人员信息
                self.modify_personal()
                self.save_personal()
            elif menu_num == 7:
                # 按个人成绩排序
                self.rank_personal()
            elif menu_num == 8:
                # 统计每个组的平均成绩
                self.group_avg()
            elif menu_num == 9:
                # 退出系统
                break
            else:
                print('输入有误，请重新输入:')

    # 添加人员
    def add_personal(self):
        name = input('请输⼊您的姓名:')
        # 定义名字
        age = input('请输⼊您的年龄:')
        # 年龄
        group = input('请输⼊您的组别:')
        scores = {}
        # 定义新增的人的分数的集合
        fusion_score = int(input('请输入Fusion360成绩：'))
        # 定义单项成绩
        arduino_score = int(input('请输入Arduino成绩：'))
        # 定义单项成绩
        python_score = int(input('请输入Python成绩：'))
        # 定义单项成绩
        scores['Fusion360'] = fusion_score
        scores['Arduino'] = arduino_score
        scores['Python'] = python_score
        personal = Personal(name, age, group, scores)
        self.personal_list.append(personal)
        # 自增id
        personal.personal_id = len(self.personal_list)
        print(personal)

    # 打印单个人员信息
    def print_personal(self, personal):
        table = PrettyTable(['ID', '姓名', '年龄', '组别', 'Fusion360', 'Arduino', 'Python', '总成绩'])
        # 创建一个table，用来储存PrettyTable
        table.add_row([personal.personal_id, personal.name, personal.age, personal.group,
                       personal.scores['Fusion360'], personal.scores['Arduino'], personal.scores['Python'],
                       personal.total_score])
        # 新增的内容
        print(table)
        # 打印

    # 查询人员信息
    def search_personal(self):
        search_name = input('请输⼊要查询的人员的姓名:')
        for i in self.personal_list:
            # 遍历整个列表看看有没有该名字
            if i.name == search_name:
                # 如果有该名字，打印
                self.print_personal(i)
                return
        print('查询失败。查无此人!')

    # 保存人员信息
    def save_personal(self):
        f = open('personal.csv', 'w', encoding='utf-8-sig')
        # 写下该人员的信息
        for i in self.personal_list:
            # 在文件中写下该人员的各个信息
            f.write(f'{i.personal_id},{i.name},{i.age},{i.group},'
                    f'{i.scores["Fusion360"]},{i.scores["Arduino"]},{i.scores["Python"]}, {i.total_score}\n')
        f.close()
        # 关闭文件

    # 加载人员信息
    def load_personal(self):
        #  判断文件是否存在
        if not os.path.exists('personal.csv'):
            return
        #  打开文件
        f = open('personal.csv', 'r', encoding='utf-8-sig')
        #  读取数据
        while True:
            # 当达到文件末尾的时候，跳出循环
            line = f.readline()
            if not line:
                break
            # 去除结尾的换行符
            line = line.strip('\n')
            personal_data = line.split(',')
            personal = Personal(personal_data[1], personal_data[2], personal_data[3],
                                {'Fusion360': int(personal_data[4]), 'Arduino': int(personal_data[5]),
                                 'Python': int(personal_data[6])},
                                int(personal_data[7]))
            # 设置id
            personal.personal_id = int(personal_data[0])
            # 添加进列表
            self.personal_list.append(personal)
        # 关闭文件
        f.close()

    # 显示所有学员信息
    def show_personal(self):
        table = PrettyTable(['ID', '姓名', '年龄', '组别', 'Fusion360', 'Arduino', 'Python', '总成绩'])
        # 遍历列表
        for i in self.personal_list:
            # 向表格中增加信息
            table.add_row([i.personal_id, i.name, i.age, i.group, i.scores['Fusion360'], i.scores['Arduino'],
                           i.scores['Python'], i.total_score])
        print(table)

    # 删除人员信息
    def del_personal(self):
        # 输入删除的姓名
        del_name = input('请输⼊要删除的人员的姓名:')
        # 设置一个初始值
        flag = 0
        for i in self.personal_list:
            # 遍历循环，寻找目标姓名
            if i.name == del_name:
                del_group = input('请输入要删除的人员的组别:')
                if i.group == del_group:
                    # 当找到目标姓名
                    self.print_personal(i)
                    flag = 1
                    # 将初始值改了，代表找到目标了
                    result = input('确认删除?(Y/N)')
                    # 再次确认
                    if result == 'Y':
                        # 如果是Y，删除该信息
                        self.personal_list.remove(i)
                        print('删除成功')
                    else:
                        return
        if flag == 0:
            print('查无此人')

    # 修改人员信息
    def modify_personal(self):
        modify_name = input('请输入需要修改的人员姓名：')
        for i in self.personal_list:
            # 在列表中循环遍历
            if i.name == modify_name:
                # 如果存在该人员
                self.print_personal(i)
                # 输出该人员的信息
                modify_group = input('请输入您要修改的人员的组别： ')
                if i.group == modify_group:
                    # 如果找到目标
                    # 输入要修改的信息
                    new_name = input('请输入修改后的名字： ')
                    new_age = input('请输入修改后的年龄：')
                    new_group = input('请输入修改后的组别：')
                    new_fusion_scores = input('请输入修改后的fusion360的成绩： ')
                    new_arduino_scores = input('请输入修改后的arduino的成绩： ')
                    new_python_scores = input('请输入修改后的python的成绩： ')
                    # 新的成绩
                    new_scores = {'Fusion360': int(new_fusion_scores), 'Arduino': int(new_arduino_scores),
                         'Python': int(new_python_scores) }
                    # 将总成绩求和
                    new_total_score = sum(new_scores.values())
                    # 将修改后的信息覆盖掉原来的信息
                    i.name = new_name
                    i.group = new_group
                    i.age = new_age
                    i.scores = new_scores
                    i.total_score = new_total_score
                    print('修改成功')
                    break
        else:
            print('查无此人')

    # 按照个人成绩排序
    def rank_personal(self):
        # 排序
        self.show_personal()
        # 先把所有人的信息输出
        self.personal_list = sorted(self.personal_list, key=lambda x: x.total_score, reverse=True)
        # 降序排序
        self.show_personal()

    # 统计每个组的平均成绩并排序
    def group_avg(self):
        num = [0, 0, 0, 0, 0, 0, 0, 0]
        # 每个组设置初始数量
        avg_score = [0, 0, 0, 0, 0, 0, 0, 0]
        # 给每个组的平均成绩设置初始值
        sum = [0, 0, 0, 0, 0, 0, 0, 0]
        # 给每个总分设置初始值
        for i in self.personal_list:
            # 遍历循环，分类，给name所对应的组数目进行累加
            if i.group == 'AR':
                num[0] += 1
                sum[0] += i.total_score
            elif i.group == 'BR':
                num[1] += 1
                sum[1] += i.total_score
            elif i.group == 'AT':
                num[2] += 1
                sum[2] += i.total_score
            elif i.group == 'IOT':
                num[3] += 1
                sum[3] += i.total_score
            elif i.group == 'WR':
                num[4] += 1
                sum[4] += i.total_score
            elif i.group == 'SF':
                num[5] += 1
                sum[5] += i.total_score
            elif i.group == 'FBM':
                num[6] += 1
                sum[6] += i.total_score
            elif i.group == 'FBM-IOT':
                num[7] += 1
                sum[7] += i.total_score
        for j in range(0, 8):
            # 在0，8之间遍历
            if num[j] != 0:
                #计算平均分
                avg_score[j] = sum[j]/num[j]
        dian = {'AR': avg_score[0], 'BR': avg_score[1], 'AT': avg_score[2], 'IOT': avg_score[3], 'WR': avg_score[4],
                'SF': avg_score[5], 'FBM': avg_score[6], 'FBM-IOT': avg_score[7]}
        table = PrettyTable(['组别', '成绩'])
        # 排序
        for key, value in sorted(dian.items(), key=lambda x: x[1], reverse=True):
            if value != 0:
                table.add_row([key, value])
                # 输出
        print(table)

    # 二.定义功能函数
    # 显示功能菜单
    @staticmethod
    def show_menu():
        print('++++++++++++++++++++++++++')
        print('|        请选择如下功能     |')
        print('|        1:添加人员        |')
        print('|        2:查询人员        |')
        print('|        3:保存人员        |')
        print('|        4:显示所有人      |')
        print('|        5:删除人员        |')
        print('|        6:修改人员        |')
        print('|        7:成绩统计        |')
        print('|        8:每组平均成绩     |')
        print('|        9:退出系统        |')
        print('++++++++++++++++++++++++++')
