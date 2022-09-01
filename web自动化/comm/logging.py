import logging
import os.path
import time
path=os.path.dirname(os.path.realpath(__file__))
cur_path=os.path.join(path,'%s.log'%('logs_'+time.strftime('%Y_%m_%d')))
class Log():
  def __init__(self):
      # self.logname = os.path.join('./log.txt', '%s.log' % time.strftime('%Y_%m_%d'))
      self.logger = logging.getLogger()      #创建日志对象
      self.logger.setLevel(logging.DEBUG)
      self.formatter = logging.Formatter(fmt='[%(asctime)s] - [%(filename)s] - %(levelname)s: %(message)s',datefmt='%Y/%m/%d %H:%M:%S')#日志格式
  def __console(self, level, message):
      fh = logging.FileHandler(cur_path, 'a', encoding='utf-8')  # 日志文件路径
      fh.setLevel(logging.DEBUG)
      fh.setFormatter(self.formatter)
      self.logger.addHandler(fh)
      ch = logging.StreamHandler()
      ch.setLevel(logging.DEBUG)
      ch.setFormatter(self.formatter)
      self.logger.addHandler(ch)
      if level == 'info':
         self.logger.info(message)
      elif level == 'debug':
         self.logger.debug(message)
      elif level == 'warning':
         self.logger.warning(message)
      elif level == 'error':
         self.logger.error(message)
      self.logger.removeHandler(ch)
      self.logger.removeHandler(fh)
      fh.close()
  def debug(self, message):
      self.__console('debug', message)
  def info(self, message):
      self.__console('info', message)
  def warning(self, message):
      self.__console('warning', message)
  def error(self, message):
      self.__console('error', message)
if __name__ == "__main__":
  log = Log()