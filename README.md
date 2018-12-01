# happytrans_web
测试网址:http://66.42.62.255:8001/
备注:
1.查看防火墙版本号
firewall-cmd --version
centos 7.3是自带firewall防火墙，提示版本号。
2.查看防火墙状态
firewall-cmd --state
3.添加80端口的权限

firewall-cmd --zone=public --add-port=80/tcp --permanent
命令含义：
--zone #作用域
--add-port=80/tcp #添加端口，格式为：端口/通讯协议
--permanent #永久生效，没有此参数重启后失效
4.重启防火墙
systemctl restart firewalld

