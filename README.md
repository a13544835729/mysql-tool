## **Mysql 导出入小工具**

#### **步骤:**

1.先将文件放入mysql 搜索目录中

```
以 linux 为例:
mysql>show variables like 'secure_file_priv';
         /var/lib/mysql-files/
   Linux: sudo cp /home/tarena/scoreTable.csv /var/lib/mysql-files/
```



2.在数据库中创建相应的库表

```
例:  
create table scoretab(  
rank int,  
name varchar(20),  
score float(5,2),  
phone char(11),  
class char(7)  
)charset=utf8;
```

3.调用 导入导出小工具,

①实例化对象,导入参数

②调用导入,导出方法