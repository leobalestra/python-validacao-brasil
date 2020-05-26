from datetime import datetime

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_do_ano = [
            "Janeiro", "Fevereiro", "Março", "Abril",
            "Maio", "Junho", "Julho", "Agosto",
            "Setembro", "Outubro", "Novembro", "Dezembro"  ]
        mes = self.momento_cadastro.month - 1
        return meses_do_ano[mes]

    def semana_cadastro(self):
        semana_do_ano = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
        semana = self.momento_cadastro.weekday() +1
        return semana_do_ano[semana]

    def format_data(self):
        data_formtada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formtada

    def __str__(self):
        return self.format_data()