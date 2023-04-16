import json
from mysql import MySQLConnection


def get_user(**kwargs):
    """
    :return: example: {'userid': 'U0001', 'username': 'WFU Tester', 'password': '123456', 'email': 'test@wfu.edu', 'phone_number': '336-123-4567', 'skill': ['C++', 'JavaScript', 'PHP', 'Python'], 'interest': ['hiking', 'swimming', 'tennis'], 'group_list': [('G0001', 'WFU Problem'), ('G0002', 'Weekend Yoga'), ('G0003', 'Summer Camp'), ('G0004', 'PIT Menu - Ronald')]}
    """
    assert {"userid"}.issubset(kwargs.keys())
    userid = kwargs.get("userid")
    mysql = MySQLConnection()
    res = mysql.execute("select * from wfu_problem.`user` where `userid` = '{}';".format(userid))
    columns = mysql.execute("describe wfu_problem.`user`;")
    columns = [item[0] for item in columns]
    return_dic = dict()
    if len(res) > 0:
        for i, one_key in enumerate(columns):
            return_dic[one_key] = res[0][i]
    res_skill = mysql.execute("select skill from wfu_problem.`skill` where `userid` = '{}';".format(userid))
    skill_list = [item[0] for item in res_skill]
    return_dic["skill"] = skill_list
    res_interest = mysql.execute("select interest from wfu_problem.`interest` where `userid` = '{}';".format(userid))
    interest_list = [item[0] for item in res_interest]
    return_dic["interest"] = interest_list
    res_group = mysql.execute("select a.groupid, group_name from (wfu_problem.`user_has_group` a join wfu_problem.`group` b on a.groupid=b.groupid) where `userid` = '{}';".format(userid))
    group_list = [item for item in res_group]
    group_list = sorted(group_list, key=lambda x: x[0])
    return_dic["group_list"] = group_list
    return return_dic


def get_group(**kwargs):
    """
    :return: example: {'groupid': 'G0001', 'group_name': 'WFU Problem', 'user_list': [('U0001', 'WFU Tester'), ('U0002', 'Madison Brown'), ('U0003', 'Emma Davis'), ('U0004', 'Emily Thomas')]}
    """
    assert {"groupid"}.issubset(kwargs.keys())
    groupid = kwargs.get("groupid")
    mysql = MySQLConnection()
    res = mysql.execute("select * from wfu_problem.`group` where `groupid` = '{}';".format(groupid))
    columns = mysql.execute("describe wfu_problem.`group`;")
    columns = [item[0] for item in columns]
    return_dic = dict()
    if len(res) > 0:
        for i, one_key in enumerate(columns):
            return_dic[one_key] = res[0][i]
    res_user = mysql.execute("select a.userid, username from (wfu_problem.`user_has_group` a join wfu_problem.`user` b on a.userid=b.userid) where `groupid` = '{}';".format(groupid))
    user_list = [item for item in res_user]
    user_list = sorted(user_list, key=lambda x: x[0])
    return_dic["user_list"] = user_list
    return return_dic


def join_group(**kwargs):
    """
    :return: example: {'result': 1, 'status': 'Success'}
    """
    assert {"userid", "groupid"}.issubset(kwargs.keys())
    userid = kwargs.get("userid")
    groupid = kwargs.get("groupid")
    mysql = MySQLConnection()
    count_user = mysql.execute("select count(*) from wfu_problem.`user` where `userid` = '{}';".format(userid))
    if count_user[0][0] == 0:
        return dict({"result": 0, "status": "User not found"})
    count_group = mysql.execute("select count(*) from wfu_problem.`group` where `groupid` = '{}';".format(groupid))
    if count_group[0][0] == 0:
        return dict({"result": 0, "status": "Group not found"})
    count_use_has_group = mysql.execute("select count(*) from wfu_problem.`user_has_group` where `userid` = '{}' and `groupid` = '{}';".format(userid, groupid))
    if count_use_has_group[0][0] > 0:
        return dict({"result": 0, "status": "User is already in this group"})
    mysql.execute("insert into wfu_problem.`user_has_group` values ('{}', '{}');".format(userid, groupid))
    return dict({"result": 1, "status": "Success"})


def leave_group(**kwargs):
    """
    :return: example: {'result': 1, 'status': 'Success'}
    """
    assert {"userid", "groupid"}.issubset(kwargs.keys())
    userid = kwargs.get("userid")
    groupid = kwargs.get("groupid")
    mysql = MySQLConnection()
    count_use_has_group = mysql.execute("select count(*) from wfu_problem.`user_has_group` where `userid` = '{}' and `groupid` = '{}';".format(userid, groupid))
    if count_use_has_group[0][0] == 0:
        return dict({"result": 0, "status": "User has not joined this group"})
    mysql.execute("delete from wfu_problem.`user_has_group` where `userid` = '{}' and `groupid` = '{}';".format(userid, groupid))
    return dict({"result": 1, "status": "Success"})


def check_login(**kwargs):
    """
    :return: example: {'result': 1}
    """
    assert {"email", "password"}.issubset(kwargs.keys())
    email = kwargs.get("email")
    print("email:", email)
    email = email.replace("%40", "@")
    password = kwargs.get("password")
    mysql = MySQLConnection()
    res = mysql.execute("select * from wfu_problem.`user` where `email` = '{}' and `password` = '{}';".format(email, password))

    columns = mysql.execute("describe wfu_problem.`user`;")
    columns = [item[0] for item in columns]

    return_dic = dict({"result": 0})
    if len(res) > 0:
        return_dic["result"] = 1
        user_info = dict()
        # print(columns)
        # print(res)
        for i, one_key in enumerate(columns):
            user_info[one_key] = res[0][i]
        return_dic["user_info"] = user_info
    return return_dic



def get_all_group_list(**kwargs):
    """
    :return: example: {'result': 1}
    """
    mysql = MySQLConnection()
    res = mysql.execute("select * from wfu_problem.`group`;")
    columns = mysql.execute("describe wfu_problem.`group`;")
    columns = [item[0] for item in columns]

    return_dic = dict({"result": 0})
    if len(res) > 0:
        return_dic["result"] = 1
        return_dic["columns"] = columns
        return_dic["group_list"] = [list(item) for item in res]
    return return_dic


if __name__ == "__main__":
    # print(get_user(userid="U0001"))
    # print(check_login(email="test@wfu.edu", password="123456"))
    # print(join_group(userid="U0001", groupid="G0005"))
    print(get_all_group_list())
    # print(leave_group(userid="U0001", groupid="G0005"))
    # print(get_group(groupid="G0001"))
    pass
