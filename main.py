import pandas as pd


class Arquivo:
    def __init__(self, nome):
        self.__nome = nome
        self.__tabela = None
        self.__dados = None

    def _le_arq(self):
        self.__tabela = pd.read_csv(self.__nome)

    def gera_dados(self):
        tabela = self.__tabela
        dicionario = tabela.to_dict()

        return dicionario

    def montar_dados(self):
        Arquivo._le_arq(self)
        self.__dados = Arquivo.gera_dados(self)
        for linha in range(299):
            print(self.__dados["MATRICULA"][linha], self.__dados["COD_DISCIPLINA"][linha], self.__dados["NOTA"][linha],
                  self.__dados["CARGA_HORARIA"][linha], self.__dados["ANO_SEMESTRE"][linha])
        return self.__dados


class Aluno:
    def __init__(self):
        self.__matricula = []
        self.__notas_aluno = []

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, mat):
        self.__matricula = mat

    def separa_aluno(self):
        pass


class Nota:
    def __init__(self, nota, ano_semestre):
        self.__nota = nota
        self.__ano_semestre = ano_semestre

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nota):
        self.__nota = nota

    @property
    def ano_semestre(self):
        return self.__ano_semestre

    @ano_semestre.setter
    def ano_semestre(self, ano_semestre):
        self.__ano_semestre = ano_semestre


class Disciplina:
    def __init__(self, cod_disciplina, carga_horaria):
        self.__cod_disciplina = cod_disciplina
        self.__carga_horaria = carga_horaria

    @property
    def cod_disciplina(self):
        return self.__cod_disciplina

    @cod_disciplina.setter
    def cod_disciplina(self, disciplina):
        self.__cod_disciplina = disciplina

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, carga_horaria):
        self.__carga_horaria = carga_horaria


class CodigoCurso:
    def __init__(self, cod_curso):
        self.__cod_curso = cod_curso

    @property
    def cod_curso(self):
        return self.__cod_curso

    @cod_curso.setter
    def cod_curso(self, cod_curso):
        self.__cod_curso = cod_curso


arq = Arquivo('notas.csv')
arq.montar_dados()


