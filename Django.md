
http://bicofino.io/2014/01/16/installing-python-2-dot-7-6-on-centos-6-dot-5/

https://tecadmin.net/install-python-2-7-on-centos-rhel/			

-----------------------
设置代理服务器(内网无法直接访问外网)
	export http_proxy="http://1.241.231.74:8000"
	export https_proxy="https://1.241.231.74:8000"
	
	https://pip.pypa.io/en/latest/installing/#installing-with-get-pip-py

--------------------------------------------------------------------------------------------

Python 
	python -V
		Python 2.6.6

	version: 2.7.15
		https://www.python.org/downloads/release/python-2715/
		
	安装Python 2.7.15
		https://tecadmin.net/install-python-2-7-on-centos-rhel/
		# 浏览器下载，上传到Linux，手动安装
	
		alias python27='/usr/local/bin/python2.7'	
		或者
		alias python=/usr/local/bin/python2.7
		source ~/.bashrc
	
pip
	curl -k -x 43.241.231.74:8000  https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	# get-pip.py下载失败，通过浏览器下载后上传到linux上，然后手动安装（用python2.7执行）： /usr/local/bin/python2.7 get-pip.py
	
	pip -V
		pip 10.0.1 from /usr/local/lib/python2.7/site-packages/pip (python 2.7)

	pip install Django  --proxy 43.241.231.74:8000
		Successfully installed Django-1.11.13 pytz-2018.4

Jango
	version: 1.11
	
	卸载旧版本
	https://docs.djangoproject.com/en/2.0/topics/install/#removing-old-versions-of-django
	
	python与django的版本兼容性
	https://docs.djangoproject.com/en/2.0/faq/install/#faq-python-version-support
	
	验证安装
		# python27
		>>> import django
		>>> print django.get_version()
		1.11.13
	
	# python27 -m django --version
		1.11.13

	初始化项目
		django-admin startproject mysite
	修改配置
		vi settings.py
			注释掉数据库配置：
			允许客户端访问：ALLOWED_HOSTS = ['*']
		禁用csrf
			
	启动项目
		cd mysite
		python27 manage.py runserver 10.141.5.51:8000
		
	
	
	curl -H "Content-Type:application/json" -X POST -d '{"user": "admin", "passwd":"12345678"}' http://10.141.5.51:8000/polls/

-------------------------------------------------------------------------------------------		

ssh -p 2345 root@10.1.2.1

安装Django
	cd /home
	mkdir pyweb && cd pyweb
    # 设置代理服务器
	pip install Django  --proxy 43.241.231.74:8000

验证安装
python -m django --version

创建project
	django-admin startproject creditReport
	
创建app
	python manage.py startapp appV1

编写脚本
	creditReport/appV1/mobile.py

	creditReport/appV1/views.py

	creditReport/appV1/urls.py
			
	creditReport/creditReport/urls.py
	

修改配置
	vi creditReport/creditReport/settings.py
		注释掉数据库配置：
		允许客户端访问：ALLOWED_HOSTS = ['*']
	appV1的views中禁用csrf
		
		
启动项目
	cd /home/pyweb/creditReport
	nohup python manage.py runserver 10.1.2.1:8000 &

停止项目
	ps auxw | grep runserver | grep -v grep | awk '{print $2}' | xargs kill -9


测试接口
	curl -H "Content-Type:application/json" -X POST -d '{"user": "admin", "passwd":"12345678"}' http://10.1.2.1:8000/creditReport/	
	
	
