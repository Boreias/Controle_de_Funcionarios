import requests
import sys

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.animation import Animation
from kivy.uix.textinput import TextInput


Window.clearcolor = get_color_from_hex('#A5ABB1')


class TelaCadastrarFuncionario(FloatLayout):
    def __init__(self, **kwargs):
        super(TelaCadastrarFuncionario, self).__init__(**kwargs)

        self.animacaoAparecer = Animation(opacity=1, duration=1.5)
        self.animacaoDesaparecer = Animation(opacity=0, duration=1)

        self.logo = Image(source='imagens/logo.png', size_hint=(.2, .2), pos_hint={'x': 0, 'y': .8}, opacity=0)
        self.add_widget(self.logo)

        self.labelNome = Label(text='Nome: ', font_size=30, size_hint=(.2, .1), pos_hint={'right': .28, 'center_y': .75}, color=(0, 0, 0, 1), opacity=0)
        self.animacaoAparecer.start(self.labelNome)
        self.add_widget(self.labelNome)
        self.nome = TextInput(multiline=False, input_type='text', font_size=30, size_hint=(.5, .1), pos_hint={'x': .28, 'center_y': .75}, opacity=0)
        self.animacaoAparecer.start(self.nome)
        self.add_widget(self.nome)

        self.labelCPF = Label(text='CPF: ', font_size=30, size_hint=(.2, .1), pos_hint={'right': .28, 'center_y': .64}, color=(0, 0, 0, 1), opacity=0)
        self.animacaoAparecer.start(self.labelCPF)
        self.add_widget(self.labelCPF)
        self.cpf = TextInput(multiline=False, input_type='number', font_size=30, size_hint=(.5, .1), pos_hint={'x': .28, 'center_y': .64}, opacity=0)
        self.animacaoAparecer.start(self.cpf)
        self.add_widget(self.cpf)

        self.labelIdade = Label(text='Idade: ', font_size=30, size_hint=(.2, .1), pos_hint={'right': .28, 'center_y': .53}, color=(0, 0, 0, 1), opacity=0)
        self.animacaoAparecer.start(self.labelIdade)
        self.add_widget(self.labelIdade)
        self.idade = TextInput(multiline=False, input_type='number', font_size=30, size_hint=(.5, .1), pos_hint={'x': .28, 'center_y': .53}, opacity=0)
        self.animacaoAparecer.start(self.idade)
        self.add_widget(self.idade)

        self.labelTelefone = Label(text='Telefone: ', font_size=30, size_hint=(.2, .1), pos_hint={'right': .28, 'center_y': .42}, color=(0, 0, 0, 1), opacity=0)
        self.animacaoAparecer.start(self.labelTelefone)
        self.add_widget(self.labelTelefone)
        self.telefone = TextInput(multiline=False, input_type='number', font_size=30, size_hint=(.5, .1), pos_hint={'x': .28, 'center_y': .42}, opacity=0)
        self.animacaoAparecer.start(self.telefone)
        self.add_widget(self.telefone)

        self.botaoCadastrar = Button(text='Cadastrar', font_size=14, size_hint=(.35, .1), pos_hint={'center_x': .5, 'y': .15}, color='#FFFFFF', background_color='#00b8f5', opacity=0)
        self.botaoCadastrar.on_press = self.SalvarDados
        self.animacaoAparecer.start(self.botaoCadastrar)
        self.add_widget(self.botaoCadastrar)

        self.botaoVoltar = Button(text='Voltar', font_size=14, size_hint=(.185, .08), pos_hint={'center_x': .85, 'y': .03}, color='#FFFFFF', background_color='#00b8f5', opacity=0)
        self.botaoVoltar.on_press = self.Voltar
        self.animacaoAparecer.start(self.botaoVoltar)
        self.add_widget(self.botaoVoltar)

    def SalvarDados(self):
        if len(self.nome.text) != 0 and len(self.cpf.text) != 0:
            try:
                getTotal = requests.get('http://localhost:8080/Cadastro/')
                if len(self.idade.text) <= 3 and len(self.cpf.text) <= 11 and len(self.telefone.text) <= 9:
                    tamanho = getTotal.json()
                    requests.post('http://localhost:8080/Cadastro/', data={'identificador': str(int(tamanho[-1]['identificador']) + 1),'nome': str(self.nome.text), 'cpf': str(int(self.cpf.text)), 'idade': str(int(self.idade.text)), 'telefone': str(int(self.telefone.text))})
                    popup = Popup(content=Label(text='Funcionario cadastrado\ncom sucesso'), pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.3, .3))
                    popup.open()
                    self.Voltar()
                else:
                    popup = Popup(title='Campos Demasiado Grandes', content=Label(text='Número máximo de caracteres:\nCPF: 11\nIdade: 3\nTelefone: 9\nOBS: Preencher apenas com valores numéricos'), pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.3, .3))
                    popup.open()
            except ValueError:
                popup = Popup(title='Erro de Formato', content=Label(text='Os campos CPF, Idade e Telefone devem ser numéricos'), pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.3, .3))
                popup.open()
            except:
                popup = Popup(title='Servidor Desconectado', content=Label(text='Favor executar o servidor na pasta backend/pessoa com "node pessoa.js"'), pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.3, .3))
                popup.open()
        else:
            popup = Popup(title='Compos obrigatórios vazios', content=Label(text='Os campos Nome e CPF são obrigatórios'), pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.3, .3))
            popup.open()

    def Voltar(self):
        self.animacaoDesaparecer.start(self.labelNome)
        self.animacaoDesaparecer.start(self.nome)
        self.animacaoDesaparecer.start(self.labelCPF)
        self.animacaoDesaparecer.start(self.cpf)
        self.animacaoDesaparecer.start(self.labelIdade)
        self.animacaoDesaparecer.start(self.idade)
        self.animacaoDesaparecer.start(self.labelTelefone)
        self.animacaoDesaparecer.start(self.telefone)
        self.animacaoDesaparecer.start(self.botaoCadastrar)
        self.animacaoDesaparecer.start(self.botaoVoltar)
        self.animacaoDesaparecer.start(self.logo)
        tela.root_window.remove_widget(tela.root)
        tela.root_window.add_widget(TelaOpcoes())

class TelaConsultarFuncionario(FloatLayout):
    def __init__(self, **kwargs):
        super(TelaConsultarFuncionario, self).__init__(**kwargs)

        self.animacaoAparecer = Animation(opacity=1, duration=1.5)
        self.animacaoDesaparecer = Animation(opacity=0, duration=1)

        self.labelNome = Label(text='Nome: ', font_size=30, size_hint=(.2, .1), pos_hint={'right': .28, 'center_y': .75}, color=(0, 0, 0, 1), opacity=0)
        self.animacaoAparecer.start(self.labelNome)
        self.add_widget(self.labelNome)
        self.nome = TextInput(multiline=False, input_type='text', font_size=30, size_hint=(.5, .1), pos_hint={'x': .28, 'center_y': .75}, opacity=0)
        self.animacaoAparecer.start(self.nome)
        self.add_widget(self.nome)

        self.labelCPF = Label(text='CPF: ', font_size=30, size_hint=(.2, .1), pos_hint={'right': .28, 'center_y': .64}, color=(0, 0, 0, 1), opacity=0)
        self.animacaoAparecer.start(self.labelCPF)
        self.add_widget(self.labelCPF)
        self.cpf = TextInput(multiline=False, input_type='number', font_size=30, size_hint=(.5, .1), pos_hint={'x': .28, 'center_y': .64}, opacity=0)
        self.animacaoAparecer.start(self.cpf)
        self.add_widget(self.cpf)

        self.botaoPesquisar = Button(text='Pesquisar', font_size=14, size_hint=(.35, .1), pos_hint={'center_x': .5, 'y': .15}, color='#FFFFFF', background_color='#00b8f5', opacity=0)
        self.botaoPesquisar.on_press = self.PesquisarDados
        self.animacaoAparecer.start(self.botaoPesquisar)
        self.add_widget(self.botaoPesquisar)

        self.botaoVoltar = Button(text='Voltar', font_size=14, size_hint=(.185, .08), pos_hint={'center_x': .85, 'y': .03}, color='#FFFFFF', background_color='#00b8f5', opacity=0)
        self.botaoVoltar.on_press = self.Voltar
        self.animacaoAparecer.start(self.botaoVoltar)
        self.add_widget(self.botaoVoltar)

    def PesquisarDados(self):
        if len(self.nome.text) != 0 or len(self.cpf.text) != 0:
            try:
                getTotal = requests.get('http://localhost:8080/Cadastro/')
                dados = getTotal.json()
                if len(self.nome.text) != 0 and len(self.cpf.text) != 0:
                    for i in range(len(dados)):
                        if dados[i]['cpf'] == self.cpf.text and dados[i]['nome'] == self.nome.text:
                            self.popularTelaPesquisa(dados, i)
                            break
                    else:
                        popup = Popup(content=Label(text='Funcionario não encontrado'), pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.3, .3))
                        popup.open()

                elif len(self.nome.text) != 0:
                    for i in range(len(dados)):
                        if dados[i]['nome'] == self.nome.text:
                            self.popularTelaPesquisa(dados, i)
                            break
                    else:
                        popup = Popup(content=Label(text='Funcionario não encontrado'), pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.3, .3))
                        popup.open()
                else:
                    for i in range(len(dados)):
                        if dados[i]['cpf'] == self.cpf.text:
                            self.popularTelaPesquisa(dados, i)
                            break
                    else:
                        popup = Popup(content=Label(text='Funcionario não encontrado'),pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.3, .3))
                        popup.open()

            except:
                popup = Popup(title='Servidor Desconectado', content=Label(text='Favor executar o servidor na pasta backend/pessoa com "node pessoa.js"'), pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.3, .3))
                popup.open()

        else:
            popup = Popup( content=Label(text='Favor preencher um dos campos'), pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.3, .3))
            popup.open()



    def popularTelaPesquisa(self, dados, i):
        self.animacaoDesaparecer.start(self.cpf)
        self.remove_widget(self.cpf)
        self.animacaoDesaparecer.start(self.nome)
        self.remove_widget(self.nome)

        self.identificador = i
        self.dados = dados

        self.labelDadosNome = Label(text=str(dados[i]['nome']), font_size=30, size_hint=(.2, .1),
                                    pos_hint={'x': .28, 'center_y': .75}, color=(0, 0, 0, 1), opacity=0)
        self.animacaoAparecer.start(self.labelDadosNome)
        self.add_widget(self.labelDadosNome)

        self.labelDadosCPF = Label(text=str(dados[i]['cpf']), font_size=30, size_hint=(.2, .1),
                                   pos_hint={'x': .28, 'center_y': .64}, color=(0, 0, 0, 1), opacity=0)
        self.animacaoAparecer.start(self.labelDadosCPF)
        self.add_widget(self.labelDadosCPF)

        self.labelIdade = Label(text='Idade: ', font_size=30, size_hint=(.2, .1),
                                pos_hint={'right': .28, 'center_y': .53}, color=(0, 0, 0, 1), opacity=0)
        self.animacaoAparecer.start(self.labelIdade)
        self.add_widget(self.labelIdade)
        self.labelDadosIdade = Label(text=str(dados[i]['idade']), font_size=30, size_hint=(.2, .1),
                                     pos_hint={'x': .28, 'center_y': .53}, color=(0, 0, 0, 1), opacity=0)
        self.animacaoAparecer.start(self.labelDadosIdade)
        self.add_widget(self.labelDadosIdade)

        self.labelTelefone = Label(text='Telefone: ', font_size=30, size_hint=(.2, .1),
                                   pos_hint={'right': .28, 'center_y': .42}, color=(0, 0, 0, 1), opacity=0)
        self.animacaoAparecer.start(self.labelTelefone)
        self.add_widget(self.labelTelefone)
        self.labelDadosTelefone = Label(text=str(dados[i]['telefone']), font_size=30, size_hint=(.2, .1),
                                        pos_hint={'x': .28, 'center_y': .42}, color=(0, 0, 0, 1), opacity=0)
        self.animacaoAparecer.start(self.labelDadosTelefone)
        self.add_widget(self.labelDadosTelefone)

        self.animacaoDesaparecer.start(self.botaoPesquisar)
        self.remove_widget(self.botaoPesquisar)

        self.botaoEditar = Button(text='Editar', font_size=14, size_hint=(.35, .1), pos_hint={'center_x': .5, 'y': .25},
                                  color='#FFFFFF', background_color='#00b8f5', opacity=0)
        self.botaoEditar.on_press = self.EditarDados
        self.animacaoAparecer.start(self.botaoEditar)
        self.add_widget(self.botaoEditar)

        self.botaoExcluir = Button(text='Excluir', font_size=14, size_hint=(.35, .1), pos_hint={'center_x': .5, 'y': .15},
                                  color='#FFFFFF', background_color='#00b8f5', opacity=0)
        self.botaoExcluir.on_press = self.ExcluirFuncionario # Ajustar
        self.animacaoAparecer.start(self.botaoExcluir)
        self.add_widget(self.botaoExcluir)

    def ExcluirFuncionario(self):
        try:
            requests.delete('http://localhost:8080/Cadastro/' + str(self.dados[self.identificador]['identificador']))
            popup = Popup(title='Exclução Concluída', content=Label(text='O funcionário foi excluído com sucesso'), pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.3, .3))
            popup.open()
            self.animacaoDesaparecer.start(self.labelDadosNome)
            self.animacaoDesaparecer.start(self.labelNome)
            self.animacaoDesaparecer.start(self.labelDadosCPF)
            self.animacaoDesaparecer.start(self.labelCPF)
            self.animacaoDesaparecer.start(self.labelDadosIdade)
            self.animacaoDesaparecer.start(self.labelIdade)
            self.animacaoDesaparecer.start(self.labelDadosTelefone)
            self.animacaoDesaparecer.start(self.labelTelefone)
            self.animacaoDesaparecer.start(self.botaoEditar)
            self.animacaoDesaparecer.start(self.botaoExcluir)
            self.animacaoDesaparecer.start(self.botaoVoltar)
            tela.root_window.remove_widget(tela.root)
            tela.root_window.add_widget(TelaOpcoes())
        except:
            popup = Popup(title='Servidor Desconectado', content=Label(text='Favor executar o servidor na pasta backend/pessoa com "node pessoa.js"'), pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.7, .3))
            popup.open()

    def Voltar(self):
        self.animacaoDesaparecer.start(self.labelNome)
        self.animacaoDesaparecer.start(self.labelCPF)

        self.animacaoDesaparecer.start(self.nome)
        self.animacaoDesaparecer.start(self.cpf)
        self.animacaoDesaparecer.start(self.botaoPesquisar)
        try:
            self.animacaoDesaparecer.start(self.labelDadosNome)
            self.animacaoDesaparecer.start(self.labelDadosCPF)
            self.animacaoDesaparecer.start(self.labelIdade)
            self.animacaoDesaparecer.start(self.labelDadosIdade)
            self.animacaoDesaparecer.start(self.labelTelefone)
            self.animacaoDesaparecer.start(self.labelDadosTelefone)
            self.animacaoDesaparecer.start(self.botaoEditar)
            self.animacaoDesaparecer.start(self.botaoExcluir)
        except:
            pass
        self.animacaoDesaparecer.start(self.botaoVoltar)
        tela.root_window.remove_widget(tela.root)
        tela.root_window.add_widget(TelaOpcoes())

    def EditarDados(self):
        self.animacaoDesaparecer.start(self.labelNome)
        self.animacaoDesaparecer.start(self.labelDadosNome)
        self.animacaoDesaparecer.start(self.labelCPF)
        self.animacaoDesaparecer.start(self.labelDadosCPF)
        self.animacaoDesaparecer.start(self.labelIdade)
        self.animacaoDesaparecer.start(self.labelDadosIdade)
        self.animacaoDesaparecer.start(self.labelTelefone)
        self.animacaoDesaparecer.start(self.labelDadosTelefone)
        self.animacaoDesaparecer.start(self.botaoEditar)
        self.animacaoDesaparecer.start(self.botaoVoltar)
        tela.root_window.remove_widget(tela.root)
        tela.root_window.add_widget(TelaEditarDados(self.dados, self.identificador))

class TelaEditarDados(FloatLayout):
    def __init__(self, dados, i, **kwargs):
        super(TelaEditarDados, self).__init__(**kwargs)
        
        self.identificador = i + 1

        self.animacaoAparecer = Animation(opacity=1, duration=1.5)
        self.animacaoDesaparecer = Animation(opacity=0, duration=1)

        self.labelNome = Label(text='Nome: ', font_size=30, size_hint=(.2, .1),
                               pos_hint={'right': .28, 'center_y': .75}, color=(0, 0, 0, 1), opacity=0)
        self.animacaoAparecer.start(self.labelNome)
        self.add_widget(self.labelNome)
        self.labelDadosNome = TextInput(text=str(dados[i]['nome']), multiline=False, input_type='text', font_size=30, size_hint=(.2, .1),
                                    pos_hint={'x': .28, 'center_y': .75}, opacity=0)
        self.animacaoAparecer.start(self.labelDadosNome)
        self.add_widget(self.labelDadosNome)

        self.labelCPF = Label(text='CPF: ', font_size=30, size_hint=(.2, .1), pos_hint={'right': .28, 'center_y': .64},
                              color=(0, 0, 0, 1), opacity=0)
        self.animacaoAparecer.start(self.labelCPF)
        self.add_widget(self.labelCPF)
        self.labelDadosCPF = TextInput(text=str(dados[i]['cpf']), multiline=False, input_type='text', font_size=30, size_hint=(.2, .1),
                                   pos_hint={'x': .28, 'center_y': .64}, opacity=0)
        self.animacaoAparecer.start(self.labelDadosCPF)
        self.add_widget(self.labelDadosCPF)

        self.labelIdade = Label(text='Idade: ', font_size=30, size_hint=(.2, .1),
                                pos_hint={'right': .28, 'center_y': .53}, color=(0, 0, 0, 1), opacity=0)
        self.animacaoAparecer.start(self.labelIdade)
        self.add_widget(self.labelIdade)
        self.labelDadosIdade = TextInput(text=str(dados[i]['idade']), multiline=False, input_type='text', font_size=30, size_hint=(.2, .1),
                                     pos_hint={'x': .28, 'center_y': .53}, opacity=0)
        self.animacaoAparecer.start(self.labelDadosIdade)
        self.add_widget(self.labelDadosIdade)

        self.labelTelefone = Label(text='Telefone: ', font_size=30, size_hint=(.2, .1),
                                   pos_hint={'right': .28, 'center_y': .42}, color=(0, 0, 0, 1), opacity=0)
        self.animacaoAparecer.start(self.labelTelefone)
        self.add_widget(self.labelTelefone)
        self.labelDadosTelefone = TextInput(text=str(dados[i]['telefone']), multiline=False, input_type='text', font_size=30, size_hint=(.2, .1),
                                        pos_hint={'x': .28, 'center_y': .42}, opacity=0)
        self.animacaoAparecer.start(self.labelDadosTelefone)
        self.add_widget(self.labelDadosTelefone)

        self.botaoEditar = Button(text='Salvar Alterações', font_size=14, size_hint=(.35, .1), pos_hint={'center_x': .5, 'y': .25},
                                  color='#FFFFFF', background_color='#00b8f5', opacity=0)
        self.botaoEditar.on_press = self.EditarDados  # Ajustar
        self.animacaoAparecer.start(self.botaoEditar)
        self.add_widget(self.botaoEditar)

        self.botaoVoltar = Button(text='Voltar', font_size=14, size_hint=(.185, .08), pos_hint={'center_x': .85, 'y': .03}, color='#FFFFFF', background_color='#00b8f5', opacity=0)
        self.botaoVoltar.on_press = self.Voltar
        self.animacaoAparecer.start(self.botaoVoltar)
        self.add_widget(self.botaoVoltar)
    
    def EditarDados(self):
        if len(self.labelDadosNome.text) != 0 and len(self.labelDadosCPF.text) != 0:
            if len(self.labelDadosIdade.text) <= 3 and len(self.labelDadosCPF.text) <= 11 and len(self.labelDadosTelefone.text) <= 9:
                try:
                    requests.put('http://localhost:8080/Cadastro/' + str(self.identificador),data={'nome': self.labelDadosNome.text, 'cpf': str(int(self.labelDadosCPF.text)), 'idade': str(int(self.labelDadosIdade.text)), 'telefone': str(int(self.labelDadosTelefone.text))})
                    popup = Popup(content=Label(text='Funcionario editado\ncom sucesso'),pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.3, .3))
                    popup.open()
                    self.Voltar()
                except ValueError:
                    popup = Popup(title='Erro de Formato', content=Label(text='Os campos CPF, Idade e Telefone devem ser numéricos'), pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.3, .3))
                    popup.open()
                except:
                    popup = Popup(title='Servidor Desconectado', content=Label(text='Favor executar o servidor na pasta backend/pessoa com "node pessoa.js"'), pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.7, .3))
                    popup.open()
            else:
                popup = Popup(title='Campos Demasiado Grandes', content=Label(text='Número máximo de caracteres:\nCPF: 11\nIdade: 3\nTelefone: 9\nOBS: Preencher apenas com valores numéricos'), pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.3, .3))
                popup.open()
        else:
            popup = Popup(title='Compos obrigatórios vazios', content=Label(text='Os campos Nome e CPF são obrigatórios'), pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.3, .3))
            popup.open()

    def Voltar(self):
        self.animacaoDesaparecer.start(self.labelNome)
        self.animacaoDesaparecer.start(self.labelDadosNome)
        self.animacaoDesaparecer.start(self.labelCPF)
        self.animacaoDesaparecer.start(self.labelDadosCPF)
        self.animacaoDesaparecer.start(self.labelIdade)
        self.animacaoDesaparecer.start(self.labelDadosIdade)
        self.animacaoDesaparecer.start(self.labelTelefone)
        self.animacaoDesaparecer.start(self.labelDadosTelefone)
        self.animacaoDesaparecer.start(self.botaoEditar)
        self.animacaoDesaparecer.start(self.botaoVoltar)
        tela.root_window.remove_widget(tela.root)
        tela.root_window.add_widget(TelaOpcoes())

class TelaOpcoes(FloatLayout):
    def __init__(self, **kwargs):
        super(TelaOpcoes, self).__init__(**kwargs)

        self.animacaoAparecer = Animation(opacity=1, duration=1.5)
        self.animacaoDesaparecer = Animation(opacity=0, duration=1)
        self.animacaoAjustarLogo = Animation(size_hint=(.2, .2), pos_hint={'x': 0, 'y': .8}, duration=2)

        self.logo = Image(source='imagens/logo.png', size_hint=(.2, .2), pos_hint={'x': 0, 'y': .8}, opacity=0)
        self.animacaoAparecer.start(self.logo)
        self.add_widget(self.logo)

        self.rh = Label(text='RH', font_size=200, size_hint=(.5, .1), pos_hint={'center_x': .5, 'y': .55}, color=(1, 1, 1, 1), opacity=0)
        self.animacaoAparecer.start(self.rh)
        self.add_widget(self.rh)

        self.botao1 = Button(text='Consultar Funcionario', font_size= 14, size_hint=(.35, .1), pos_hint={'center_x': .5, 'y': .25}, color='#FFFFFF', background_color='#00b8f5', opacity=0)
        self.botao1.on_press = self.consultarFuncionario
        self.animacaoAparecer.start(self.botao1)
        self.add_widget(self.botao1)

        self.botao2 = Button(text='Cadastrar Funcionario', font_size= 14, size_hint=(.35, .1), pos_hint={'center_x': .5, 'y': .15}, color='#FFFFFF', background_color='#00b8f5', opacity=0)
        self.botao2.on_press = self.cadastrarFuncionario
        self.animacaoAparecer.start(self.botao2)
        self.add_widget(self.botao2)

        self.botaoSair = Button(text='Sair', font_size=14, size_hint=(.185, .08), pos_hint={'center_x': .85, 'y': .03}, color='#FFFFFF', background_color='#00b8f5', opacity=0)
        self.botaoSair.on_press = self.Sair
        self.animacaoAparecer.start(self.botaoSair)
        self.add_widget(self.botaoSair)


    def consultarFuncionario(self):
        self.animacaoDesaparecer.start(self.botao1)
        self.animacaoDesaparecer.start(self.botao2)
        self.animacaoDesaparecer.start(self.rh)
        self.animacaoDesaparecer.start(self.botaoSair)
        self.animacaoAjustarLogo.start(self.logo)
        tela.root_window.remove_widget(tela.root)
        tela.root_window.add_widget(TelaConsultarFuncionario())


    def cadastrarFuncionario(self):
        self.animacaoDesaparecer.start(self.botao1)
        self.animacaoDesaparecer.start(self.botao2)
        self.animacaoDesaparecer.start(self.rh)
        self.animacaoDesaparecer.start(self.botaoSair)
        self.animacaoAjustarLogo.start(self.logo)
        tela.root_window.remove_widget(tela.root)
        tela.root_window.add_widget(TelaCadastrarFuncionario())

    def Sair(self):
        self.animacaoDesaparecer.start(self.logo)
        self.animacaoDesaparecer.start(self.botao1)
        self.animacaoDesaparecer.start(self.botao2)
        tela.root_window.remove_widget(tela.root)
        sys.exit()


class TelaLogo(FloatLayout):
    def __init__(self, **kwargs):
        super(TelaLogo, self).__init__(**kwargs)

        self.animacaoAparecer = Animation(opacity=1, duration=1.5)
        self.animacaoDesaparecer = Animation(opacity=0, duration=1)
        self.animacaoAjustarLogo = Animation(size_hint=(.2, .2), pos_hint={'x': 0, 'y': .8}, duration=2)

        self.logo = Image(source='imagens/logo.png', opacity=0, pos_hint={'y': .1})
        self.animacaoAparecer.start(self.logo)
        self.add_widget(self.logo)

        self.botao = Button(text='Entrar', font_size= 14, size_hint=(.35, .1), pos_hint={'center_x': .5, 'y': .25}, color='#FFFFFF', background_color='#00b8f5', opacity=0) #0098AA
        self.botao.on_press = self.botaoPressionado
        self.animacaoAparecer.start(self.botao)
        self.add_widget(self.botao)

    def botaoPressionado(self):
        self.animacaoAjustarLogo.start(self.logo)
        self.animacaoDesaparecer.start(self.botao)
        tela.root_window.remove_widget(tela.root)
        tela.root_window.add_widget(TelaOpcoes())


class SistemaRefrigeracao(App):
    def build(self):
        return TelaLogo()

if __name__ == '__main__':
    tela = SistemaRefrigeracao()
    tela.run()