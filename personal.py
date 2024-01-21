class Personal(object):
    # 定义人员输出，包含：姓名、年龄、组别、培训成绩、总成绩
    def __init__(self, name, age, group, scores, total_score=None):
        self.personal_id = None
        self.name = name
        self.age = age
        self.group = group
        self.scores = scores
        if total_score is None:
            self.total_score = scores['Fusion360'] + scores['Arduino'] + scores['Python']
        else:
            self.total_score = total_score

    def __str__(self):
        return f'{self.personal_id}, {self.name} {self.age} {self.group} {self.scores} {self.total_score}'