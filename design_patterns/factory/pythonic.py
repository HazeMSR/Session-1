from typing import Protocol
from abc import abstractmethod

class Handler(Protocol):
	@abstractmethod
	def download(self, path: str) -> bytes:
		raise NotImplementedError

	@abstractmethod
	def upload(self, data: bytes, path: str):
		raise NotImplementedError

class FileHandler(Handler):
	def download(self, path):
		print(f'The file will download to the following path: {path}')
		return bytes('Some random bytes','utf-8')

	def upload(self, data, path):
		print(f'The file will upload to the following path: {path}'+ 
		f'\nWith the data: {data}')

class NewFileHandler(Handler):
	def download(self, path):
		print(f'The file will download to the following path: {path} with the quickest way')
		return bytes('Some quickest random bytes','utf-8')

	def upload(self, data, path):
		print(f'The file will upload to the following path: {path}'+ 
		f'\nWith the data: {data} with the quickest way')

ALL_HANDLERS = {
  'old': FileHandler,
  'new': NewFileHandler,
}

def make_handler(version):
	handler: Handler
	try:
		handler = ALL_HANDLERS[version]()
	except KeyError as err:
		raise NotImplementedError from err
	return handler

if __name__ == '__main__':
	handler = make_handler('new')

	# upload some data
	handler.upload('8=Dmdsdsdandsuldf','C:/Users/some/path')