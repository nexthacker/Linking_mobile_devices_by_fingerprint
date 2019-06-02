from text_formating import text_processing
from db_helper import init


if __name__ == "__main__":
    print('Iniciando tabelas...')
    init()
    print('Pronto!')
    print("processando coletas...")
    text_processing(5)
    print("Analizando dados...")


    while True:
        pass
        # TODO: menu for aplication on consol
