# djangOauth

### 项目介绍

1. 基于 django-rest-framework-jwt 
2. 基于 django-auth-ldap
3. 实现 用户名的统一认证
4. 您可以直接使用该项目，或者基于该项目二次开发。（比如实现运维账号的通知管理）

### 开发环境

Djnago >= 2    
Python >= 3     
Mysql = 5.7.16    

### 工作方式

1. 第三方应用发起带有“用户名、密码”的post请求（/api/login/），djangOauth 验证用户名、密码后，返回jwt token
2. 第三方应用解析 jwt token 验证有效性，并保存至cookies，每页刷新页面 验证一次。
3. 如若token过期，则发起（/api/token-refresh/） token刷新接口，获取新的token。
4. 当启用LDAP验证方式时，将会自动在数据库创建对应用户


### 配置说明

1. **setting.py**：     
1.1 **JWT_EXPIRATION_DELTA** : 控制token过期时间；     
1.2 **JWT_REFRESH_EXPIRATION_DELTA** : token过期多长时间内，可以通过过期token获取新token    
1.3 后端验证方式 设置
	```
	AUTHENTICATION_BACKENDS = [
	    'django_auth_ldap.backend.LDAPBackend',
	    'django.contrib.auth.backends.ModelBackend'
	]
	```
	第一个 **LDAPBackend** 验证失败，则继续使用 **ModelBackend** 进行验证

1.4 ldap 服务器配置
	```
	AUTH_LDAP_SERVER_URI = 'ldap://openldap.com'
	AUTH_LDAP_BIND_DN = 'cn=Manager,dc=xwjrops,dc=cn'
	AUTH_LDAP_BIND_PASSWORD = 'password'
	```
	**ldap 服务器的地址** 以及 **管理员账号密码**

1.5 用户ou路径
	```
	AUTH_LDAP_USER_SEARCH = LDAPSearch(
	    'ou=Technology,dc=xwjrops,dc=cn',
	    ldap.SCOPE_SUBTREE,
	    '(uid=%(user)s)',
	)
	```

1.6 数据库字段对应的ldap字段

	```
	AUTH_LDAP_USER_ATTR_MAP = {
	    'first_name': 'givenName',
	    'last_name': 'sn',
	    'email': 'mail',
	}
	```

### 安装方法

1. 安装mysql，并新建数据库 **djangOauth**（略）
2. 下载代码
```shell
git clone https://github.com/X-Mars/djangOauth.git
```
3. 安装模块
```shell
pip3 install -r requirements.txt
```
4. 启动服务
```shell
python3 djangOauth/manage.py runserver 0.0.0.0 8000
```
5. 后台访问
```url
http://ip:8000/admin
```

### 接口信息

```url
http://ip:8000/api/doc/
```

### 待完善
1. 对接openldap
