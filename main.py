
from blockchain import Blockchain


if __name__ == "__main__":

    blockchain = Blockchain("Mensagem I")
    blockchain.addBlock("Mensagem II")
    blockchain.addBlock("Mensagem III")
    blockchain.addBlock("Mensagem IV")
    

    #blockchain.blockchain[1].mensagem = "Mensagem XX"

    blockchain.isValid()