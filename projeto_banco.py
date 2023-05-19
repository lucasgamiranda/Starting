import os
from abc import ABC, abstractmethod


class Pessoa():
    def nome(self, nome):
        return nome

    def idade(self, idade):
        return idade


class Cliente(Pessoa):
    def __init__(self, agencia, numero):
        self._conta = agencia, numero

    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, conta):
        self._conta = conta


class Banco():
    def __init__(self):
        self.agencia = 1
        self.conta = [123, 456]
        self.cliente = ['lucas']
        self.poupancas = [123]
        self.correntes = [456]

    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, conta):
        self._conta = conta

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente

    def autentica(self, agencia, conta, cliente):
        if agencia != self.agencia:
            print('Agência incorreta!')
            raise ValueError('Agência incorreta!')
        elif cliente not in self.cliente:
            print('Cliente não cadastrado!')
            raise ValueError('Cliente não cadastrado!')
        elif conta not in self.conta:
            print('Número da conta incorreto!')
            raise ValueError('Número da conta incorreto!')
        else:
            print('Agencia, Conta e Cliente autênticados!')


class Conta(ABC, Banco):
    @abstractmethod
    def sacar(self, saque): ...

    @abstractmethod
    def depositar(self, deposito): ...


class ContaCorrente(Conta, Banco):
    def __init__(self, agencia, numero):
        self.agencia = agencia
        self.numero = numero
        self.saldo = 300
        self.limite = -1501

    def sacar(self, saque):
        self.saldo -= saque
        if self.saldo <= self.limite:
            print('Seu limite é insuficiente!')
        else:
            print(f'Você sacou: R${saque:.2f}')
            print(f'Seu saldo é: R${self.saldo:.2f}')

    def depositar(self, deposito):
        self.saldo += deposito
        print(f'Você depositou: R${deposito:.2f}')
        print(f'Seu saldo é: R${self.saldo:.2f}')


class ContaPoupanca(Conta):
    def __init__(self, agencia, numero):
        self.agencia = agencia
        self.numero = numero
        self.saldo = 300

    def sacar(self, saque):
        if saque > self.saldo:
            print('Seu saldo é insuficiente!')
        else:
            self.saldo -= saque
            print(f'Você sacou: R${saque:.2f}')
            print(f'Seu saldo é: R${self.saldo:.2f}')

    def depositar(self, deposito):
        self.saldo += deposito
        print(f'Você depositou: R${deposito:.2f}')
        print(f'Seu saldo é: R${self.saldo:.2f}')


banco = Banco()

print('Seja bem vindo! Insira seus dados: ')
agencia_usuario = int(input('Agência: '))
numero_usuario = int(input('Número da conta: '))
nome_usuario = input('Nome: ')
banco.autentica(agencia_usuario, numero_usuario, nome_usuario)

conta_poupanca = ContaPoupanca(agencia_usuario, numero_usuario)
conta_corrente = ContaCorrente(agencia_usuario, numero_usuario)

ordem_usuario = input('O que deseja fazer? ')

sacar = ['sacar', 'Sacar', 'SACAR']
depositar = ['depositar', 'Depositar', 'DEPOSITAR']
sair = ['sair', 'Sair', 'SAIR']
consultar_saldo = ['consultar saldo', 'Consultar saldo', 'Consultar Saldo',
                   'consultar Saldo', 'consultar SALDO', 'Consultar SALDO',
                   'CONSULTAR Saldo', 'CONSULTAR saldo', 'CONSULTAR SALDO']

while numero_usuario in banco.poupancas:
    if ordem_usuario in sacar:
        os.system('cls')
        print(f'Seu saldo é: R${conta_poupanca.saldo:,.2f} ')
        saque_usuario = input('Quanto deseja sacar? ')
        conta_poupanca.sacar(int(saque_usuario))
    elif ordem_usuario in depositar:
        os.system('cls')
        print(f'Seu saldo é: R${conta_poupanca.saldo:,.2f} ')
        deposito_usuario = input('Quanto deseja depositar? ')
        conta_poupanca.depositar(int(deposito_usuario))
    elif ordem_usuario in consultar_saldo:
        os.system('cls')
        print(f'Seu saldo é: R${conta_poupanca.saldo:,.2f} ')
    elif ordem_usuario in sair:
        break
    else:
        print('Desculpe, não conheço essa opção.')
        print('Você pode sair, consultar saldo, sacar e depositar!')
    ordem_usuario = input('O que deseja fazer? ')

while numero_usuario in banco.correntes:
    if ordem_usuario in sacar:
        os.system('cls')
        print(f'Seu saldo é: R${conta_corrente.saldo:,.2f} ')
        saque_usuario = input('Quanto deseja sacar? ')
        conta_corrente.sacar(int(saque_usuario))
    elif ordem_usuario in depositar:
        os.system('cls')
        print(f'Seu saldo é: R${conta_corrente.saldo:,.2f} ')
        deposito_usuario = input('Quanto deseja depositar? ')
        conta_corrente.depositar(int(deposito_usuario))
    elif ordem_usuario in consultar_saldo:
        os.system('cls')
        print(f'Seu saldo é: R${conta_corrente.saldo:,.2f} ')
    elif ordem_usuario in sair:
        break
    else:
        print('Desculpe, não conheço essa opção.')
        print('Você pode sair, consultar saldo, sacar e depositar!')

    ordem_usuario = input('O que deseja fazer? ')
