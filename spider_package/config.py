# coding:utf8
import re

options = {
    'root_url': 'http://www.juooo.com',
    'max_count': 1000,
    'urlReg': {
        'urlRegType': 1,
        'urlFull': '',
        'urlStr': 'http://(\w+).juooo.com/\w+'
    },
    'urlData': []
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
        options['max_count'] = int(max_count)

    print '\n'
    print '================================='
    print '请输入需要收集的url格式'
    print '1. 完整url格式, 默认模式'
    print '2. 域名+部分url格式'

    urlType = raw_input('请选择url格式：')
    print urlType

    urlStr = ''
    urlFull = ''
    urlRe = r'^http(s?)://(\w+.+)\w' 

    if urlType and int(urlType) == 2:
        urlFull = raw_input('请输入带完整域名的urlFull:')
        urlTest = re.match(urlRe, urlFull)

        if not (urlTest) is None:
            options['urlReg']['urlFull'] = urlFull
 
        urlStr = raw_input('请输入需要查找的urlStr:')
        options['urlReg']['urlStr'] = urlStr
        options['urlReg']['urlRegType'] = int(urlType)

    elif urlType and int(urlType) == 1 :
        while True:
            urlStr = raw_input('请输入带完整域名的urlStr:')
            urlTest = re.match(urlRe, urlStr)

            if not (urlTest) is None:
                options['urlReg']['urlStr'] = urlStr
                options['urlReg']['urlRegType'] = int(urlType)
                break

    # 输入需要配置的数据项
    print '请输入配置项，每一个配置项标签名和class名'
    num = 1
    while True:
        itemTag = raw_input('请输入数据项' + num +'的标签名 ')
        itemClass = raw_input('请输入数据项' + num +'的class ')

        options.urlData[num].itemTag = itemTag
        options.urlData[num].itemName = itemClass
        
        if (not (itemTag) is None or not (itemClass) is None) and num != 1:
            break
        num = num + 1
        
    return options
 
