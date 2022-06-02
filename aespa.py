class Member:
  def __init__(self, name, posisi,lahir,negara):
    self.nameae = name
    self.posisiae = posisi
    self.lahirae = lahir
    self.negaraae= negara
    
    
  def get_name(self):
    return f"Hi, i'm {self.nameae} ,"
    
  def get_posisi(self):
    return f" I'm {self.posisiae} From Aespa ,"
    
  def get_lahir(self):
    return f"I'm born {self.lahirae} ,"
    
  def get_negara(self):
    return f"I'm life in {self.negaraae} ,"
  
  def get_all_member(self):
    return f"{self.get_name()} {self.get_posisi()} {self.get_lahir()} {self.get_negara()}"
  