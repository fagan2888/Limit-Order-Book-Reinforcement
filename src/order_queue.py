import pandas as pd
import numpy as np
from message_queue import Message_Queue

class Order_Queue(object):
	def __init__(self, path):
		self._df = pd.read_csv(path, header=None)
		self._row_idx = -1

	def create_orderbook_time(self, time, mq):
		mq.jump_to_time(time)
		self._row_idx= mq._row_idx
		row = self._df.iloc[self._row_idx]
		return self._create_orderbook(row)

	def _create_orderbook(self, row):
		len_row= int(len(row)/4)
		ask= np.array([int(row[4*i]) for i in range(len_row)])
		ask_size= np.array([int(row[4*i+1]) for i in range(len_row)])
		bid = np.array([int(row[4*i+2]) for i in range(len_row)])
		bid_size = np.array([int(row[4*i+3]) for i in range(len_row)])
		orderbook = {'ask':ask, 'ask_size':ask_size, 'bid':bid, 'bid_size':bid_size}
		return orderbook