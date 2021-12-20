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
        '''
                for linha in range(299):
            print(self.__dados["MATRICULA"][linha], self.__dados["COD_DISCIPLINA"][linha], self.__dados["NOTA"][linha],
                  self.__dados["CARGA_HORARIA"][linha], self.__dados["ANO_SEMESTRE"][linha])
        '''
        return self.__dados


class Aluno:
    def __init__(self, matricula):
        self.__matricula = matricula
        self.__notas_aluno = []

    def __eq__(self, other):
        if self.__matricula == other.matricula:
            return True
        else:
            return False

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, mat):
        self.__matricula = mat

    @property
    def nota_aluno(self):
        return self.__notas_aluno

    @nota_aluno.setter
    def nota_aluno(self, nota_aluno):
        self.__notas_aluno.append(nota_aluno)

    def calcula_cr(self):
        soma = 0
        total_chr = 0
        for n in self.__notas_aluno:
            soma += n.nota * n.disciplina.carga_horaria
            total_chr += n.disciplina.carga_horaria

        if total_chr == 0:
            return None
        else:
            return soma/total_chr


class Nota:
    def __init__(self, nota, ano_semestre):
        self.__nota = nota
        self.__ano_semestre = ano_semestre
        self.__disciplina = None
        self.__cod_curso = None

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

    @property
    def disciplina(self):
        return self.__disciplina

    @disciplina.setter
    def disciplina(self, disciplina):
        self.__disciplina = disciplina

    @property
    def cod_curso(self):
        return self.__cod_curso

    @cod_curso.setter
    def cod_curso(self, cod_curso):
        self.__cod_curso = cod_curso


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

    def __eq__(self, other):
        if self.__cod_curso == other.__cod_curso:
            return True
        else:
            return False

    @property
    def cod_curso(self):
        return self.__cod_curso


class Turma:
    def __init__(self, codigo_curso):
        self.__lista_alunos = []
        self.__codigo_curso = codigo_curso

    def __eq__(self, other):
        if self.__codigo_curso == other.__codigo_curso:
            return True
        else:
            return False

    @property
    def lista_alunos(self):
        return self.__lista_alunos

    @lista_alunos.setter
    def lista_alunos(self, lista_alunos):
        self.__lista_alunos.append(lista_alunos)

    @property
    def codigo_curso(self):
        return self.__codigo_curso.cod_curso

    def cr_curso(self):
        soma = 0
        qtd_alunos = len(self.__lista_alunos)
        for la in self.__lista_alunos:
            soma += la.calcula_cr()
        if qtd_alunos == 0:
            return None
        else:
            return soma / qtd_alunos


arq = Arquivo('notas.csv')
dados_gerados = arq.montar_dados()


listaAluno = []
listaNota = []
listaDisciplina = []
listaCurso = []
listaTurma = []

for i in range(299):
    matr = dados_gerados["MATRICULA"][i]
    nots = dados_gerados["NOTA"][i]
    ano = dados_gerados["ANO_SEMESTRE"][i]
    disciplin = dados_gerados["COD_DISCIPLINA"][i]
    cargaH = dados_gerados["CARGA_HORARIA"][i]
    curso = dados_gerados["COD_CURSO"][i]

    nt = Nota(nots, ano)
    discipl = Disciplina(disciplin, cargaH)
    curs = CodigoCurso(curso)
    nt.disciplina = discipl
    nt.cod_curso = curs

    turma = Turma(curs)
    existeT = False
    for t in listaTurma:
        if t == turma:
            turma = t
            existeT = True
    if not existeT:
        listaTurma.append(turma)

    existe = False
    aluno = Aluno(matr)
    for a in listaAluno:
        if a == aluno:
            a.nota_aluno = nt
            aluno = a
            existe = True
    if not existe:
        aluno.nota_aluno = nt
        listaAluno.append(aluno)

    if aluno not in turma.lista_alunos:
        turma.lista_alunos = aluno

    listaNota.append(nt)
    listaDisciplina.append(discipl)
    listaCurso.append(curs)

print("------- O CR dos alunos é: --------")
for aluno in listaAluno:
    print(f'{aluno.matricula} - {aluno.calcula_cr():.2f}')
print("-----------------------------------")
print("----- Média de CR dos cursos ------")
for turma in listaTurma:
    print(f'{turma.codigo_curso} - {turma.cr_curso():.2f}')
print("-----------------------------------")

