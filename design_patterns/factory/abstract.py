from abc import ABC, abstractmethod

class FileHandlerInterface(ABC):
	@abstractmethod
	def download(self, path):
		raise NotImplementedError

	@abstractmethod
	def upload(self, data, path):
		raise NotImplementedError

class FileHandler(FileHandlerInterface):
	def download(self, path):
		print(f'The file will download to the following path: {path}')

	def upload(self, data, path):
		print(f'The file will upload to the following path: {path}'+ 
		f'\nWith the data: {data}')

class NewFileHandler(FileHandlerInterface):
	def download(self, path):
		print(f'The file will download to the following path: {path} with the quickest way')

	def upload(self, data, path):
		print(f'The file will upload to the following path: {path}'+ 
		f'\nWith the data: {data} with the quickest way')

class HandlerFactory:
	def get_handler(self, version):
		handler = None
		if version == 'old':
			handler = FileHandler()
		elif version == 'new':
			handler = NewFileHandler()
		return handler

if __name__ == '__main__':
	handler = HandlerFactory().get_handler('new')

	# upload some data
	handler.upload('8=Dmdsdsdandsuldf','C:/Users/some/path')