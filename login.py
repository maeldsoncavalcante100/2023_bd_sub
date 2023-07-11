# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox

#importar o conector
import mysql.connector
#estabelecer a conexao
conexao = mysql.connector.connect(
    host="localhost", user="root",
    password="", database="escola")
#criar o cursor
cursor = conexao.cursor()
print("Conectado ao BD.")

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(358, 114)
        self.centralwidget = QtWidgets.QWidget(parent=Login)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label_usuario = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_usuario.setObjectName("label_usuario")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_usuario)
        self.line_usuario = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.line_usuario.setObjectName("line_usuario")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_usuario)
        self.line_senha = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.line_senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.line_senha.setObjectName("line_senha")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_senha)
        self.botao_entrar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.botao_entrar.setObjectName("botao_entrar")
        self.botao_entrar.clicked.connect(self.login)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.botao_entrar)
        self.label_senha = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_senha.setObjectName("label_senha")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_senha)
        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login do Sistema"))
        self.label_usuario.setText(_translate("Login", "Usuário:"))
        self.botao_entrar.setText(_translate("Login", "ENTRAR"))
        self.label_senha.setText(_translate("Login", "Senha:"))
    

    def login(self):
        nome = self.line_usuario.text()
        senha = self.line_senha.text()


        sql = '''SELECT * FROM usuario WHERE nome = %s AND senha = MD5(%s)'''
        cursor.execute(sql, (nome, senha))
        dados = cursor.fetchall()

        if len(dados) == 0 : #Não encontrou
            msg = QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setText("Acesso negado.")
            msg.exec()

        else : 
            #Importar a classe da tela que sejesa abrir
            from cadaluno import Ui_CadAluno
            #criar uma tela vazio   
            self.tela = QtWidgets.QMainWindow()
            #criar um objeto da tela que deseja exibir
            self.cadastro = Ui_CadAluno()
            # associar a tela vazia com o código da tela a exibir
            self.cadastro.setupUi(self.tela)
            # exibir  a nova tela
            self.tela.show()
            # fechar tela de login 
            Login.close()

            '''
            msg = QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setText("Acesso liberado.")
            msg.exec()
            '''


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec())
