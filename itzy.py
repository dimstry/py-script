class Member:
  def __init__(self, name, posisi,lahir,negara):
    self.name = name
    self.posisi = posisi
    self.lahir = lahir
    self.negara = negara
    
    
  def get_name(self):
    return f"Hi, i'm {self.name} ,"
    
  def get_posisi(self):
    return f" I'm {self.posisi} From Itzy ,"
    
  def get_lahir(self):
    return f"I'm born {self.lahir} ,"
    
  def get_negara(self):
    return f"I'm life in {self.negara} ,"
  
  def get_all_member(self):
    return f"{self.get_name()} {self.get_posisi()} {self.get_lahir()} {self.get_negara()}"
  