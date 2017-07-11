# -*- coding: utf-8 -*-
# @Author: gzliuxin
# @Email:  gzliuxin@corp.netease.com
# @Date:   2017-07-11 14:25:58


class RpcCient(object):
	"""Base Rpc Client"""
	def __init__(self):
		super(RpcCient, self).__init__()

	def get_screen_size(self):
		"""get screen size"""
		raise NotImplementedError

	def getattr(self, nodes, name):
		"""get node attribute"""
		raise NotImplementedError

	def setattr(self, nodes, name, val):
		"""set node attribute"""
		raise NotImplementedError

	def make_selection(self):
		raise NotImplementedError

	def select(self, query, multiple=False):
		raise NotImplementedError