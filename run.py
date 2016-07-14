import sys


def ignore_whitespace(lines):
    ret = []
    for line in lines:
        if line == '':
            continue
        line = line.strip()
        ret.append(line)
    return ret


def sql_type(type):
    if type == 'int':
        return 'Integer'
    if type == 'str':
        return 'String()'
    if type == 'float':
        return 'Float'
    return '"ERROR"'


def sql_attr(attr):
    if attr == 'pk':
        return 'primary_key=True'
    if attr == 'u':
        return 'unique=True'
    return '"ERROR"'


def main(argv):
    lenth = len(argv)
    if lenth > 2:
        print('输入太多参数')
        return

    path = argv[1]
    if path[len(path)-3:] != '.tb':
        print('参数应当为.tb结尾的文件')
        return

    try:
        f = open(path, 'r')
    except:
        print('读取文件错误，请检查文件是否存在')
        return

    path_parse = path.split('/')
    name = path_parse[len(path_parse) - 1]
    print('读取配置文件 {} 成功，正在解析...'.format(name))

    all = f.read()

    f.close()

    all_parse = all.split('table')
    tables = []
    for t in all_parse:
        lines = t.split('\n')
        lines = ignore_whitespace(lines)
        if lines != []:
            tables.append(lines)

    for t in tables:
        table_name = t[0]
        seg_num = len(t)
        with open(table_name + '.py', 'w') as f:
            f.write('from . import db\n\n\nclass {}(db.Model):\n'.format(table_name.title()))
            for i in range(1, seg_num):
                line = t[i]
                line_parse = line.split(' ')
                seg_name, seg_type = line_parse[0], line_parse[1]
                arg_len = len(line_parse)
                formatted_string = '    {} = db.Column(db.{}'.format(seg_name, sql_type(seg_type))
                if arg_len > 2:
                    for j in range(2, arg_len):
                        seg_attr = sql_attr(line_parse[j])
                        formatted_string += ', ' + seg_attr
                f.write(formatted_string + ')\n')

    print('解析完成！')

if __name__ == '__main__':
    main(sys.argv)