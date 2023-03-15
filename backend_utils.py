from mysql import MySQLConnection


def get_user(**kwargs):
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
    return return_dic


def check_login(**kwargs):
    assert {"userid", "password"}.issubset(kwargs.keys())
    userid = kwargs.get("userid")
    password = kwargs.get("password")
    mysql = MySQLConnection()
    res = mysql.execute("select * from wfu_problem.`user` where `userid` = '{}' and `password` = '{}';".format(userid, password))

    return_dic = dict({"result": 0})
    if len(res) > 0:
        return_dic["result"] = 1
    return return_dic


if __name__ == "__main__":
    print(get_user(userid="0001"))
    pass
