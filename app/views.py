from django.shortcuts import render, redirect,get_object_or_404
from app.models import Aluno, Professor, Disciplina, Turma, Horario
from .forms import Alunoform, Professorform, Turmaform, Disciplinaform, Horarioform
from .models import Aluno, Professor, Disciplina, Turma, Horario

# Create your views here.

def index(request):
    return render(request, 'index.html')
def Gerenciar(request):
    return render(request, 'gerenciar.html')
def Detalhar(request): 
    return render(request, 'Detalhar.html')


def index_int(request,valor):
    return render(request,'index.html',{'valor':valor,'tipo':'int'})
def listaAlunos(request):
    return render(request,'listaAlunos.html',{'listaAlunos':Aluno.objects.all()})
def listaProfessores(request):
    return render(request, 'listaProfessores.html',{'listaProfessores':Professor.objects.all()})
def listaDisciplinas(request):
    return render(request, 'listaDisciplinas.html',{'listaDisciplinas':Disciplina.objects.all()})
def listaTurmas(request):
    return render(request, 'listaTurmas.html',{'listaTurmas':Turma.objects.all()})
def listaHorarios(request):
    return render(request, 'listaHorarios.html',{'listaHorarios':Horario.objects.all()})
#Edita os Objetos-----------------------------------------------------------
def editarAlunos(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    turmas = Turma.objects.all()

    if request.method == "POST":
        aluno.nome = request.POST.get("nome")
        aluno.matricula = request.POST.get("matricula")  
        turma_id = request.POST.get("turma")
        aluno.turma = get_object_or_404(Turma, id=turma_id)
        aluno.data_nascimento = request.POST.get("data_nascimento")  
        
        # Salva as alterações
        aluno.save()
        return redirect("listaAlunos")
    else:
        return render(request, 'editarAlunos.html', {'dadosAluno': aluno, 'turmas': turmas})

def editarProfessores(request, id):
   
    professor =Professor.objects.get(id=id)
    
    if request.method == "POST":
        # Atualiza os campos do professor com os dados enviados
        professor.nome = request.POST.get("nome")
        professor.codigo_professor = request.POST.get("codigo_professor")
        professor.especialidade = request.POST.get("especialidade")  # Removido o ponto
        
        # Salva as alterações
        professor.save()
        return redirect("listaProfessores")  # Redireciona após salvar
    else:
        # Renderiza o formulário com os dados do professor
        return render(request, 'editarprofessores.html', {'dadosProfessor': professor})
    
def editarDisciplinas(request, id):
   
    disciplinas =  get_object_or_404(Disciplina,id=id)
    professor = Professor.objects.all
    if request.method == "POST":
        # Atualiza os campos do professor com os dados enviados
        #disciplinas.nome_disciplina = request.POST.get("nome")
        disciplinas.codigo_disciplina = request.POST.get("codigo_disciplina")
        professor_id = request.POST.get("professor")
        disciplinas.professor = get_object_or_404(Professor, id=professor_id)
        

        # Salva as alterações
        disciplinas.save()
        return redirect("listaDisciplinas")  # Redireciona após salvar
    else:
        # Renderiza o formulário com os dados 
        return render(request, 'editarDisciplinas.html', {'dadosDisciplina': disciplinas, 'professor': professor })
    
def editarTurmas(request, id):
   
   turmas = Turma.objects.get(id=id)
 
   if request.method == "POST":
       # Atualiza os campos do professor com os dados enviados
        turmas.nome = request.POST.get("nome")
        turmas.sala = request.POST.get("sala")
        turmas.ano = request.POST.get("ano")  

        # Salva as alterações
        turmas.save()
        return redirect("listaTurmas")  # Redireciona após salvar
   
   else:
        # Renderiza o formulário com os dados do professor
        return render(request, 'editarTurmas.html', {'dadosTurmas': turmas})

def editarHorarios(request, id):
    horarios = get_object_or_404(Horario, id = id)
    turmas = Turma.objects.all()
    disciplina = Disciplina.objects.all()
 
    if request.method == "POST":
       # Atualiza os campos do professor com os dados enviados
        turma_id = request.POST.get("turma")
        horarios.turma = get_object_or_404(Turma, id = turma_id)

        disciplina_id = request.POST.get("disciplinas")
        horarios.disciplina = get_object_or_404(Disciplina, id = disciplina_id)
        horarios.dia_semana = request.POST.get("dia_semana") 
        horarios.horario_inicio = request.POST.get("horario_inicio")  
        horarios.horario_fim  = request.POST.get("horario_fim ")   

        horarios.save()
        return redirect("listaHorarios")  # Redireciona após salvar
   
    else:
        # Renderiza o formulário com os dados do professor
        return render(request, 'editarhorarios.html', {'dadoshorarios': horarios, 'turmas': turmas,'disciplina': disciplina })


# Deleta os objetos -----------   
def deletarAlunos(request, id):
    aluno = Aluno.objects.get(id=id)
    aluno.delete()
    return redirect('listaAlunos')
    
def deletarProfessor(request, id):
    professor = Professor.objects.get(id=id)
    professor.delete()
    return redirect('listaProfessores')

def deletarDisciplinas(request, id):
    disciplinas = Disciplina.objects.get(id=id)
    disciplinas.delete()
    return redirect('listaDisciplinas')

def deletarTurmas(request, id):
    turmas = Turma.objects.get(id=id)
    turmas.delete()
    return redirect('listaTurmas')

def deletarHorarios(request, id):
    horarios = Horario.objects.get(id=id)
    horarios.delete()
    return redirect('listaHorarios')

#Adicona Objetos
def adicionarAluno(request):
    if request.method == 'POST':
        form = Alunoform(request.POST)
        if form.is_valid():
            form.save()  # Salva o objeto no banco de dados
            return redirect('listaAlunos')  # Redireciona para uma página de listagem
    else:
        form = Alunoform()
    
    return render(request, 'adicionarAluno.html', {'form': form})

def adicionarProfessor(request):
    if request.method == 'POST':
        form = Professorform(request.POST)
        if form.is_valid():
            form.save()  # Salva o objeto no banco de dados
            return redirect('listaProfessores')  # Redireciona para uma página de listagem
    else:
        form = Professorform()
    
    return render(request, 'adicionarProfessor.html', {'form': form})

def adicionarTurma(request):
    if request.method == 'POST':
        form = Turmaform(request.POST)
        if form.is_valid():
            form.save()  # Salva o objeto no banco de dados
            return redirect('listaTurmas')  # Redireciona para uma página de listagem
    else:
        form = Turmaform()
    
    return render(request, 'adicionarTurma.html', {'form': form})

def adicionarDisciplina(request):
    if request.method == 'POST':
        form = Disciplinaform(request.POST)
        if form.is_valid():
            form.save()  # Salva o objeto no banco de dados
            return redirect('listaDisciplinas')  # Redireciona para uma página de listagem
    else:
        form = Disciplinaform()
    
    return render(request, 'adicionarDisciplinas.html', {'form': form})

def adicionarHorario(request):
    if request.method == 'POST':
        form = Horarioform(request.POST)
        if form.is_valid():
            form.save()  # Salva o objeto no banco de dados
            return redirect('listaHorarios')  # Redireciona para uma página de listagem
    else:
        form = Horarioform()
    
    return render(request, 'adicionarHorario.html', {'form': form})
