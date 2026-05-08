
def show(content):
    class Particle:
        def __init__(self, content):
            self._content = content
            

        @property
        def column(self):
            finals = ''
            for response in content:
                finals += str(response) + '\n'
            return finals.strip()
        
        @property
        def line(self):
            finals = ''
            for response in content:
                finals += f'{response} '
            return finals
        
        @property
        def default(self):
            return content
    
    return Particle(content)