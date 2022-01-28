from typing import Protocol

class Handler(Protocol):

	def download(self, path: str) -> bytes:
		raise NotImplementedError

	def upload(self, data: bytes, path: str):
		raise NotImplementedError

class FileHandler:
	def download(self, path):
		print(f'The file will download to the following path: {path}')
		return bytes('Some random bytes','utf-8')

	def upload(self, data, path):
		print(f'The file will upload to the following path: {path}'+ 
		f'\nWith the data: {data}')

class NewFileHandler:
	def download(self, path):
		print(f'The file will download to the following path: {path} with the quickest way')
		return bytes('Some quickest random bytes','utf-8')

	def upload(self, data, path):
		print(f'The file will upload to the following path: {path}'+ 
		f'\nWith the data: {data} with the quickest way')

class HandlerFactory:
	def get_handler(self, version) -> Handler:
		handler: Handler 
		if version == 'old':
			handler = FileHandler()
		elif version == 'new':
			handler = NewFileHandler()
		else:
  			raise NotImplementedError
		return handler

if __name__ == '__main__':
	handler = HandlerFactory().get_handler('new')

	# upload some data
	handler.upload('8=Dmdsdsdandsuldf','C:/Users/some/path')