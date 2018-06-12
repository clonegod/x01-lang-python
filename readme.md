## Python2.7 Learning

#### “优雅”、“明确”、“简单”

#### Python提供了非常完善的基础代码库
	网络、文件、GUI、数据库、文本等
	
#### Python还有大量的第三方库
	
#### Python适合开发哪些类型的应用呢？
	首选是网络应用，包括网站、后台服务等等；
	其次是许多日常需要的小工具，包括系统管理员需要的脚本任务等等；	
	
#### Python的缺点
	第一个缺点就是运行速度慢，和C程序相比非常慢，因为Python是解释型语言，代码在执行时会一行一行地翻译成CPU能理解的机器码，这个翻译过程非常耗时，所以很慢。
	python解释执行的编译器：
		CPython。这个解释器是用C语言开发的，所以叫CPython。
	
#### Python 和其它语言的交互
	如果要和Java平台交互，最好的办法不是用Jython将python脚本翻译为字节码，而是通过网络调用来交互，确保各程序之间的独立性。
    而且，如果python中使用到第三方算法库，是无法正常转化为java字节码的。
    因此，可使用python的web框架提供http接口进行交互。
	
	
-----------------------------------------------------------------------
## 运行Python
#### 在命令行模式下，
	可以执行python进入Python交互式环境，在Python交互式环境下，只能输入Python代码执行。
	也可以执行python hello.py运行一个.py文件。

#### 执行python脚本
	python bootstrap.py
	
	
#### python REPL（Read Eval Print Loop）交互式环境
	查看python版本
		python -V
	
	启动REPL环境
		python
	
	退出REPL环境
		exit()  / quit() 
		
-----------------------------------------------------------------------
#### pip 安装模块
	pip install Django
	pip install xxx
	
	
-----------------------------------------------------------------------
#### python语法要求
	注释用"#"
	区分大小写
	当语句以冒号“:”结尾时，后面缩进的语句视为代码块
	严格的缩进格式: 使用4个空格的缩进
	
#### 脚本示例
'''
	print语句也可以跟上多个字符串，用逗号“,”隔开，就可以连成一串输出
	print会依次打印每个字符串，遇到逗号“,”会输出一个空格，因此，输出的字符串是拼起来的
	
	raw_input，可以让用户输入字符串，并存放到一个变量里。
	输入name = raw_input()并按下回车后，Python交互式命令行就在等待你的输入了。这时，你可以输入任意字符，然后按回车后完成输入。
	raw_input可以传入一个字符串，用来提示用户输入
'''

#!/usr/bin/env python

name = raw_input('please enter your name: ')
print 'hello,', name		
	
-----------------------------------------------------------------------
## 数据类型
#### 整数
	整数运算永远是精确的（除法难道也是精确的？是的！），因为整数除法只取结果的整数部分。
	所以Python还提供一个余数运算，可以得到两个整数相除的余数：
		>>> 10 % 3
		1
	无论整数做除法还是取余数，结果永远是整数，所以，整数运算结果永远是精确的。

	十六进制用0x前缀
	八进制用0前缀
	二进制用0b前缀
	
	整数之间的进制转换:
		10进制转16进制: hex(16)  ==>  0x10
		16进制转10进制: int('0x10', 16)  ==>  16
		类似的还有oct()， bin()

	字符串转整数:
		10进制字符串: int('10')  ==>  10
		16进制字符串: int('10', 16)  ==>  16
		16进制字符串: int('0x10', 16)  ==>  16
	
#### 字符串
	r前缀，让转义符失效
		print r'\\\t\\'
		
	多行字符串
		'''
			xxxx
			xxxx
		'''

#### 布尔值
	布尔值只有True、False两种值，要么是True，要么是False

	
#### 空值
	空值是Python里一个特殊的值，用None表示。
	
#### 变量、弱类型
	变量不仅可以是数字，还可以是任意数据类型。
	变量名必须是大小写英文、数字和_的组合，且不能用数字开头
	可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量（弱类型）
	变量本身类型不固定的语言称之为动态语言

#### 常量
	在Python中，通常用全部大写的变量名表示常量：
	PI = 3.14159265359
    
-----------------------------------------------------------------------	
#### 字符串格式化
	在字符串内部 %s表示用字符串替换，%d表示用整数替换，%x表示用16进制替换
	
	10进制转16进制
	>>> print '%x' % 1634
	662
	
	如果只有一个%x，括号可以省略。
	>>> 'Hello, %s' % 'world'
	'Hello, world'
	
	>>> 'Hi, %s, you have $%d.' % ('Alice', 1000000)
	'Hi, Alice, you have $1000000.'	

-----------------------------------------------------------------------	
## 字符编码 
    >>> 字符编码是指，将语言中的字符用计算机中的二进制编码进行表示
	Unicode把所有语言都统一到一套编码里，所有语言的字符都可以准确表示，这样就不会再有乱码问题了。
	在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
		用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件
		浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8在网络上进行传输，最后显示在浏览器上：
	
	如果统一成Unicode编码，乱码问题从此消失了。但是，如果你写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。
	本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。
	UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节
	
	Python 2.x版本虽然支持Unicode，但在语法上需要'xxx'和u'xxx'两种字符串表示方式。
	
	unicode与中文的互转
        >>> unicode(u'中国')
		>>> u'中国'
		u'\u4e2d\u56fd'
		
		>>> print u'\u4e2d\u56fd'
		中国

	unicode编码与UTF-8编码的互转
		>>> u'中国'.encode('UTF-8')
		'\xe4\xb8\xad\xe5\x9b\xbd'

		>>> print '\xe4\xb8\xad\xe5\x9b\xbd'.decode('UTF-8')
		中国

		
#### 设置脚本文件的编码		
    >>> 当源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，将按UTF-8编码读取源代码文件。
        第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
        第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    print u'中国'



	
-----------------------------------------------------------------------		
## 集合
#### list , tuple
    list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。	
    list是一种有序的集合，可以随时添加和删除其中的元素。
        classmates = []	
        增
            classmates.append('Adam')
            classmates.insert(1, 'Jack')
        删
            classmates.pop()
            classmates.pop(1)
        改 
            classmates[1] = 'Sarah'
        查
            classmates[0]
            classmates[-1]
            len(classmates)
        
        
    tuple一旦初始化就不能修改
        >>> t = (1,)
        >>> t = (1, 2)

#### dict , set 
    使用dict和set --- 牢记的第一条就是dict的key必须是不可变对象（可变对象的hashcode值不是固定的）


    dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
        >>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
        >>> d['Michael']
        增
             d['Adam'] = 67
        删
             d.pop('Bob')
        改
             d['Adam'] = 68
        查
            'Thomas' in d		# 判断key是否在dict中存在
            d['Thomas']			
            d.get('Thomas')		# 不存在，返回None
            d.get('Thomas', -1)	# 不存在，返回预设的默认值
            

    set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
        要创建一个set，需要提供一个list作为输入集合：
        >>> s = set()
        
        增
            s.add(4)
        删
            s.remove(4)
            s.pop()
        查
            (4 in s) #访问set值就是判断set中是否存在该值

        交集，并集运算
        >>> s1 = set([1, 2, 3])
        >>> s2 = set([2, 3, 4])
        >>> s1 & s2
        set([2, 3])
        >>> s1 | s2
        set([1, 2, 3, 4])

-----------------------------------------------------------------------		
## 函数
####定义函数
    在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
    如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。
    return None可以简写为return。
    
####空函数
    pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
    def nop():
        pass
        
####参数检查
    def my_abs(x):
        if not isinstance(x, (int, float)):
            raise TypeError('bad operand type')
        if x >= 0:
            return x
        else:
            return -x   
    
####返回多个值
    import math

    def move(x, y, step, angle=0):
        nx = x + step * math.cos(angle)
        ny = y - step * math.sin(angle)
        return nx, ny        
    
    # 返回值是一个tuple
    >>> x, y = move(100, 100, 60, math.pi / 6)
    >>> print x, y 


####函数的参数
    对于函数的调用者来说，只需要知道如何传递正确的参数，以及函数将返回什么样的值就够了
    Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

####必选参数 - 函数运行所必须的参数
    def run(task):
        process(task)
        return '100'
    
####默认参数 - 降低了函数调用的难度。无论是简单调用还是复杂调用，函数只需要定义一个。
    def power(x, n=2):
        s = 1
        while n > 0:
            n = n - 1
            s = s * x
        return s

    def enroll(name, gender, age=6, city='Beijing'):
        print 'name:', name
        print 'gender:', gender
        print 'age:', age
        print 'city:', city
        
    按顺序提供默认参数
        enroll('Bob', 'M', 7)
    
    当不按顺序提供部分默认参数时，需要把参数名写上。
        enroll('Adam', 'M', city='Tianjin')
        

    Python函数在定义的时候，默认参数L的值就被计算出来了，默认参数必须指向不变对象！
    def add_end(L=None):
        if L is None:
            L = []
        L.append('END')
        return L
    

        

####可变参数 - 传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
    def calc(*numbers):
        sum = 0
        for n in numbers:
            sum = sum + n * n
        return sum    

    Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
    可变参数在函数调用时自动组装为一个tuple
    >>> nums = [1, 2, 3]
    >>> calc(*nums)
    14

    
####关键字参数
    关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

    def person(name, age, **kw):
        print 'name:', name, 'age:', age, 'other:', kw
    
    可以只传入必选参数：
        >>> person('Michael', 30)
        name: Michael age: 30 other: {}
    
    可以传入任意个数的关键字参数：
        >>> person('Bob', 35, city='Beijing')
        name: Bob age: 35 other: {'city': 'Beijing'}
        
        >>> person('Adam', 45, gender='M', job='Engineer')
        name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
        
        >>> kw = {'city': 'Beijing', 'job': 'Engineer'}
        >>> person('Jack', 24, **kw)
        name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

    
####参数组合
    对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
    
    参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。

    def func(a, b, c=0, *args, **kw):
        print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

    >>> func(1, 2, 3, 'a', 'b', x=99)
    a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}

    最神奇的是通过一个tuple和dict，你也可以调用该函数：
    >>> args = (1, 2, 3, 4)
    >>> kw = {'x': 99}
    >>> func(*args, **kw)
    a = 1 b = 2 c = 3 args = (4,) kw = {'x': 99}



-----------------------------------------------------------------------	
## 模块与包
    当一个模块编写完毕，就可以被其他地方引用。比如引用Python内置的模块和来自第三方的模块。
    
    模块 
        - 指的是python脚本文件,一个.py文件就称之为一个模块（Module）。比如app/abc.py模块，它的模块名就是app.abc
        使用模块可以避免函数名和变量名冲突。
        模块可以被其它模块调用。
        代码按功能分离到不同的模块，有利于维护和管理。

    包 
        - 指的是文件目录，要求该目录下必须要有一个__init__.py 
        __init__.py本身就是一个模块，而它的模块名就是它所在的目录名。

        
####使用模块
    第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，
    第2行注释表示.py文件本身使用标准UTF-8编码；
    第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
    第6行使用__author__变量把作者写进去
    

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    ' a test module '

    __author__ = 'Michael Liao'

    import sys  # 导入sys模块

    def test():
        args = sys.argv
        if len(args)==1:
            print 'Hello, world!'
        elif len(args)==2:
            print 'Hello, %s!' % args[1]
        else:
            print 'Too many arguments!'

    # 当在命令行运行该模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该模块，这个if判断将失败。
    if __name__=='__main__':
        test()
        
        
        
####模块别名
   导入模块时，还可以使用别名，这样，可以在运行时根据当前环境选择最合适的模块
    try:
        import cStringIO as StringIO
    except ImportError: # 导入失败会捕获到ImportError
        import StringIO
        
    try:
        import json # python >= 2.6
    except ImportError:
        import simplejson as json # python <= 2.5
    

####函数、变量的可访问性问题

    正常的函数或变量名（public），比如：abc，x123，PI 
    特殊用途的变量，比如：__author__，__name__, __doc__
    私有的函数或变量（private），比如：_abc，__abc等；

    # 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
    def _private_1(name):
        return 'Hello, %s' % name

    def _private_2(name):
        return 'Hi, %s' % name

    def greeting(name):
        if len(name) > 3:
            return _private_1(name)
        else:
            return _private_2(name)    

----------------------------------------------------------------------
## 安装第三方模块
    
    包管理工具
        easy_install和pip。目前官方推荐使用pip。

    安装Python Imaging Library
        pip install PIL
        
        
####模块搜索路径
    默认情况下，Python解释器会搜索
        当前目录
        所有已安装的内置模块
        第三方模块
        
    搜索路径存放在sys模块的path变量中：
    >>> import sys
    >>> print sys.path

    加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错：        
    ImportError: No module named mymodule

    手动在sys.path中追加要搜索的目录：
        import sys
        sys.path.append('C:/Users/Administrator/Desktop/test/scripts')
        import MyUtil


    导入其它包下的类
        # test/sub1/bootstrap.py
            #!/usr/bin/env python
            # -*- coding: utf-8 -*-

            import sys
            sys.path.append('C:/Users/Administrator/Desktop/test/sub2')
            #from Student import Student
            import Student as StuModule

            def invoke():
                for p in sys.path:
                    print p
                #Student('alice', 100).print_score()
                StuModule.Student('alice', 100).print_score()

                
            if __name__=='__main__':
                invoke()
            
        # test/sub2/Student.py
            #!/usr/bin/env python
            # -*- coding: utf-8 -*-

            class Student(object):

                def __init__(self, name, score):
                    self.name = name
                    self.score = score

                def print_score(self):
                    print '%s: %s' % (self.name, self.score)
                    



                    
