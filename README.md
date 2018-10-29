# djangOauth

### 项目介绍

1. 基于 django-rest-framework-jwt 
2. 实现 用户名的统一认证

### 开发环境

Djnago >= 2    
Python >= 3     
Mysql = 5.7.16    

### 工作方式

1. 第三方应用发起带有“用户名、密码”的post请求（/api/login/），djangOauth 验证用户名、密码后，返回jwt token
2. 第三方应用解析 jwt token 验证有效性，并保存至cookies，每页刷新页面 验证一次。
3. 如若token过期，则发起（/api/token-refresh/） token刷新接口，获取新的token。

### 配置说明

1. **setting.py**：     
1.1 **JWT_EXPIRATION_DELTA** : 控制token过期时间；     
1.2 **JWT_REFRESH_EXPIRATION_DELTA** : token过期多长时间内，可以通过过期token获取新token

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
