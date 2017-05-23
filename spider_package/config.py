# coding:utf8

options = {
    'root_url': 'http://www.juooo.com',
    'max_count': 1000,
    'urlReg': {
        'urlRegType': 1,
        'urlStr': 'http://(\w+).juooo.com/\w+'
    },
    'urlData': {}
}

def initOptions():
    print '请输入入口url:'
    root_url = raw_input('入口url：')
    if root_url:
        print 'aaa'
        options['root_url'] = root_url

    print '====================================='
    print '请输入最大收集条数，大于0的正整数, 0默认收集%d条' % options['max_count']
    max_count = raw_input('最大收集条数:')
    if max_count and int(max_count) > 1:
        print 'bbbb'
        options['max_count'] = max_count

    print '\n'
    print '================================='
    print '请输入需要收集的url格式'
    print '1. 完整url格式, 默认模式'
    print '2. 域名+部分url格式'

    urlType = raw_input('请选择url格式：')
    print urlType

    urlStr = ''
    urlRe = r'^http(s?)://(\w+.+)\w' 
    if urlType == 2:
        urlStr = raw_input('请输入urlStr:')
        options['urlReg']['urlStr'] = urlStr
        options['urlReg']['urlRegType'] = urlType

    elif urlType == 1 :
        while True:
            urlStr = raw_input('请输入带完整域名的urlStr:')
            urlTest = re.match(urlRe, urlStr)

            if not (urlTest) is None:
                options['urlReg']['urlStr'] = urlStr
                options['urlReg']['urlRegType'] = urlType
                break
    
    return options
 
