import sys


def check_argv():
    argv = sys.argv
    if len(argv) == 1:
        lang = None
        verb = None
    elif len(argv) == 2:
        lang = '1'
        verb = argv[1]
    else:
        lang = argv[1]
        verb = argv[2]
    return lang, verb


def check_verb(verb, prompt):
    return verb if verb else input(prompt)


## 以下部分创建 set_verb 函数（见下方的注释）（一时兴起，没什么卵用）
li = []
for i in range(3):
    s = '    ' + ('if' if i == 0 else 'elif') + ' lang == \'' + str(i + 1) + '\':\n'
    s += '        verb = check_verb(verb, \'%s\')\n'
    li.append(s)

def formli(li: list, subs: tuple):
    newli = []
    for i in range(len(li)):
        newli.append(li[i] % subs[i])
    return newli

set_verb_li = formli(li, ('请输入一个动词：', 'Please input a verb: ', '動詞を一つ入力してください：'))
set_verb_fun = 'def set_verb(verb, lang):\n' + ''.join(set_verb_li) + '    return verb\n\n'
exec(set_verb_fun)


"""def set_verb(verb, lang):
    if lang == '1':
        verb = check_verb(verb, '请输入一个动词：')
    elif lang == '2':
        verb = check_verb(verb, 'Please input a verb: ')
    elif lang == '3':
        verb = check_verb(verb, '動詞を一つ入力してください：')
    return verb"""
## 创建 set_verb 结束


def foo():
    lang, verb = check_argv()
    lang = input('1 = 简体中文\n2 = English\n') if not lang else lang
    if lang == '1':
        verb = input('请输入一个动词：') if not verb else verb
        if verb == '' or verb is None:
            verb = '打工'
        s = verb + '是不可能' + verb + '的，一辈子都不可能' + verb + '的。'
    elif lang == '2':
        verb = input('Please input a verb: ') if not verb else verb
        if verb == '' or verb is None:
            verb = 'work'
        s = 'It\'s impossible for me to ' + verb + '. Impossible for ever.'
    else:
        verb = input('動詞を一つ入力してください：') if not verb else verb
        if verb == '' or verb is None:
            verb = 'バイトする'
        s = verb + 'のは無理だよ。死ぬまで全然無理だよ。'
    print(s)


def main():
    foo()


if __name__ == '__main__':
    main()
