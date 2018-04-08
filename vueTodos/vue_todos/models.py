# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Todos(models.Model):
    title = models.CharField(verbose_name=u'标题',max_length=30)
    count = models.IntegerField(verbose_name=u'未完成待办项数目',default=0)
    isdelete = models.BooleanField(verbose_name=u'是否删除')
    locked = models.BooleanField(verbose_name=u'是否锁定')
    def __str__(self):
        return self.titie

    class Meta:
        verbose_name = u'待办事项'
        verbose_name_plural = u'待办事项'
        ordering = ['id']

class Items(models.Model):
    '''
    text: String,  // 文字内容
    isDelete: Boolean, // 是否删除(物理删除)
    checked: Boolean // 是否完成
    '''
    todo = models.ForeignKey(Todos,verbose_name=u'待办事项')
    text = models.CharField(verbose_name=u'文字内容',max_length=100)
    isdelete = models.BooleanField(verbose_name=u'是否删除')
    locked = models.BooleanField(verbose_name=u'是否锁定')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = u'待办单项'
        verbose_name_plural = u'待办单项'
        ordering = ['id']
