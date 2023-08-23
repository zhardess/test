import os
import datetime

CUR_PATH = os.path.dirname(os.path.abspath(__file__))
OPS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ops")

def test_one_op(op_name:str=None, html_save_dir:str=None):
    save_name = html_save_dir + '/' + "{}_report.html".format(op_name)
    print("-------------------------------\n")
    print("test ops: {}".format(op_name))
    tmp = os.getcwd()
    os.chdir(OPS_PATH)
    os.system("pytest test_{}.py --html {} --self-contained-html".format(op_name, save_name))
    os.chdir(tmp)
    print("ops: {} test finished!!".format(op_name))

def decode_info(info):
    if ',' not in info:
        return info
    else:
        info = info.split(',')
        return info

def test_all_ops(op_name:str=None):
    time_now = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    html_save_dir = os.path.join(CUR_PATH, 'ops_test_report', time_now)
    if not os.path.exists(html_save_dir):
        os.mkdir(html_save_dir)

    path = os.listdir(OPS_PATH)
    if "all" != op_name:
        op_name = decode_info(op_name)
        if isinstance(op_name, list):
            for item in op_name:
                test_one_op(op_name=item, html_save_dir=html_save_dir)
        else:
            test_one_op(op_name=op_name, html_save_dir=html_save_dir)
    else:
        for p in path:
            if p.endswith(".py") and p.startswith("test_"):
                op = p.split(".py")[0].split("test_")[-1]
                test_one_op(op_name=op, html_save_dir=html_save_dir)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--op_name', type=str, default='all', help='which op you want to eval')
    args = parser.parse_args()
    test_all_ops(args.op_name)