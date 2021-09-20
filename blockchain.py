from datetime import datetime
import hashlib

class Bloco:
    def __init__(self, index, mensagem, timestamp, previous_hash):
            self.index = index
            self.mensagem = mensagem
            self.timestamp = timestamp
            self.previous_hash = previous_hash
            self.nonce = self.validHash()

    def validHash(self):
        nonce = 1
        while(True):
                string = "" + str(self.index)+ str(self.mensagem) +str(self.timestamp) + str(self.previous_hash) + str(nonce)
                hash = hashlib.sha256(string.encode()).hexdigest()
                if(hash.startswith("000")):
                    break
                nonce += 1
        return nonce

    def getHash(self):
         string = "" + str(self.index)+ str(self.mensagem) +str(self.timestamp) + str(self.previous_hash) + str(self.nonce)
         return hashlib.sha256(string.encode()).hexdigest()

      
      
  


class Blockchain:
    
    def __init__(self, mensagem):
        self.blockchain = [self.addGenesisBlock(mensagem)]

    def addBlock(self, mensagem):
        timestamp = datetime.timestamp(datetime.now())
        self.blockchain.append(Bloco(len(self.blockchain), mensagem, timestamp, self.getPreviousBlockHash()))
        
    def getPreviousBlockHash(self):
        previous_hash = self.blockchain[-1].getHash()
        return previous_hash

    def addGenesisBlock(self, mensagem):
        timestamp = datetime.timestamp(datetime.now())
        return Bloco(0, mensagem, timestamp, 0)

    def isValid(self):
        valid = True
        for x in range(len(self.blockchain) - 1):
            if(self.blockchain[x].getHash() != self.blockchain[x + 1].previous_hash):
                print("Cadeia inválida")
                valid = False
                break
        if(valid):
            print("Cadeia Válida")
        

