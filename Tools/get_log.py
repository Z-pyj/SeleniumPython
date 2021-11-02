# -*- coding: utf-8 -*-
# @Author : zw
import logging.handlers


class GatLog:
    # 定义类属性
    logger = None

    # 定义类方法
    @classmethod
    def get_log(cls):
        # 判断logger属性是否为空
        if cls.logger is None:
            # 设置日志器
            # 获取日志对象
            cls.logger = logging.getLogger()
            # 设置日志级别
            cls.logger.setLevel(logging.INFO)
            # 获取处理器--控制台
            sh = logging.StreamHandler()
            # 获取处理器--日志文件
            th = logging.handlers.TimedRotatingFileHandler(filename="./Log/log.log",
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=30,
                                                           encoding="utf-8")
            # 设置格式器
            fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s'
            fm = logging.Formatter(fmt)

            # 将格式器添加到处理器--控制台
            sh.setFormatter(fm)
            # 将格式器添加到处理器--日志文件
            th.setFormatter(fm)
            # 将处理器添加到日志器中
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
        return cls.logger
