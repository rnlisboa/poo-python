### Classe que vai adicionar funcionalidade em outras classes

class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.log', 'a+', encoding='UTF-8') as file:
            file.write(msg)
            file.write('\n')
    
    def log_info(self,msg):
        self.write(f'INFO: {msg}')
    
    def log_error(self,msg):
        self.write(f'ERROR: {msg}')