from django.db import models
from product.models import Product


# Create your models here.
class Apitest(models.Model):
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)
    # 关联产品id，product是应用名，Product是product应用的表名
    apitestname = models.CharField(verbose_name='流程接口名称', max_length=64)  # 流程接口名称
    apitestdesc = models.CharField(verbose_name='描述', max_length=64, null=True)  # 描述
    apitester = models.CharField(verbose_name='测试人', max_length=16)  # 测试人
    apitestresult = models.BooleanField(verbose_name='测试结果')  # 测试结果
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)  # 创建时间

    class Meta:
        verbose_name = '流程场景接口'
        verbose_name_plural = '流程场景接口'

    def __str__(self):
        return self.apitestname


class Apistep(models.Model):
    Apitest = models.ForeignKey('Apitest', on_delete=models.CASCADE, )  # 关联接口id
    apiname = models.CharField(verbose_name='接口名称', max_length=100)  # 接口标题
    apiurl = models.CharField(verbose_name='url地址', max_length=200)  # 地址
    apiparamvalue = models.CharField(verbose_name='请求参数和值', max_length=800)  # 参数和值
    REQUEST_METHOD = (('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch'))
    apimethod = models.CharField(verbose_name='请求方法', choices=REQUEST_METHOD, default='get', max_length=200,
                                 null=True)  # 请求方法
    apiresult = models.CharField(verbose_name='预期结果', max_length=200)  # 预期结果
    apistatus = models.BooleanField(verbose_name='是否通过')  # 测试结果
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)  # 创建时间
    apiresponse = models.CharField(verbose_name='响应数据', max_length=5000)  # 响应数据
    apistep = models.CharField(verbose_name='步骤', max_length=100)  # 步骤

    def __str__(self):
        return self.apiname
