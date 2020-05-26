from validate_docbr import CPF
from validate_docbr import CNPJ

class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos incorreta!")

class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CNPJ inválido")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def format(self):
        cpf_mask = CPF()
        return cpf_mask.mask(self.cpf)

class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def format(self):
        cnpj_mask = CNPJ()
        return cnpj_mask.mask(self.cnpj)

class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)

        if self.tipo_documento == "cpf":
            if self.cpf_e_valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CNPJ inválido!")
        elif self.tipo_documento == "cnpj":
            if self.cnpj_e_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ inválido!")
        else:
            raise ValueError("Documento inválido")
