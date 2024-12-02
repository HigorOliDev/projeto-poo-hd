from django.shortcuts import render, redirect
from app.models import Aluno, Professor, Disciplina, Turma, Horario
from .forms import Alunoform, Professorform, Turmaform, Disciplinaform, Horarioform
from .models import Aluno, Professor, Disciplina, Turma, Horario

# Create your views here.

def index(request):
    return render(request, 'index.html')
def Gerenciar(request):
    return render(request, 'gerenciar.html')

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
#Edita os Objetos
def editarAlunos(request, id):

    aluno = Aluno.objects.get(id=id)
    
    if request.method == "POST":
        # Atualiza os campos do aluno com os dados enviados
        aluno.nome = request.POST.get("nome")
        aluno.matricula = request.POST.get("matricula")  
        aluno.turma = Turma.objects.get(id=int(request.POST.get("turma")))
        #print(request.POST.get("turma"))
        aluno.data_nascimento = request.POST.get("data_nascimento")  
        
        # Salva as alterações
        aluno.save()
        return redirect("listaAlunos")  # Redireciona após salvar
    else:
        # Renderiza o formulário com os dados do aluno
        return render(request, 'editarAlunos.html', {'dadosAluno': aluno})

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
   
    disciplinas =Disciplina(editarDisciplinas, id=id)
    
    if request.method == "POST":
        # Atualiza os campos do professor com os dados enviados
        disciplinas.nome = request.POST.get("nome")
        disciplinas.codigo_disciplina = request.POST.get("codigo_disciplina")
        disciplinas.professor = request.POST.get("professor")  # Removido o ponto

        # Salva as alterações
        disciplinas.save()
        return redirect("listaDisciplinas")  # Redireciona após salvar
    else:
        # Renderiza o formulário com os dados 
        return render(request, 'editarDisciplinas.html', {'dadosDisciplina': disciplinas})
    
def editarTurmas(request, id):
   
   turmas = Turma.objects.get(id=int(editarTurmas.id))
 
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
        return render(request, 'editarTurmas.html', {'dadosturmas': turmas})

def editarHorarios(request, id):
    horarios =Horario(listaHorarios, id='id')
 
    if request.method == "POST":
       # Atualiza os campos do professor com os dados enviados
        horarios.turma = request.POST.get("turma")
        horarios.disciplina = request.POST.get("disciplina")
        horarios.dia_semana = request.POST.get("dia_semana") 
        horarios.horario_inicio = request.POST.get("horario_inicio")  
        horarios.horario_fim  = request.POST.get("horario_fim ")   

        horarios.save()
        return redirect("listahorarios")  # Redireciona após salvar
   
    else:
        # Renderiza o formulário com os dados do professor
        return render(request, 'editarhorarios.html', {'dadoshoraios': Horario})


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
            return redirect('listaHorario')  # Redireciona para uma página de listagem
    else:
        form = Horarioform()
    
    return render(request, 'adicionarHorario.html', {'form': form})
