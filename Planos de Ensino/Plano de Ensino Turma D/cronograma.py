# -*- coding: iso-8859-1 -*-

from schedule import *
from datetime import *

start = date(2017, 3, 6)
schedule = Schedule(start, 2, [0, 2])

schedule.add_event(Event(description = 'Apresentação do curso'))
schedule.add_event(Event(description = 'Ferramentas'))

schedule.add_event(Event(description = 'Introdução ao Python'))
schedule.add_event(Event(description = 'Introdução ao Python científico'))

schedule.add_event(Event(description = 'Zeros de Funções'))
schedule.add_event(Event(description = 'Zeros de Funções'))

schedule.add_event(Event(description = 'Mínimo de funções'))
schedule.add_event(Event(description = 'Mínimo de funções de várias variáveis'))

schedule.add_event(Event(description = 'Interpolação'))
schedule.add_event(Event(description = 'Splines'))

schedule.add_event(Event(description = 'Ajuste de curvas: retas e mínimos quadrados'))
schedule.add_event(Event(description = 'Mínimos quadrados em modelos arbitrários'))

schedule.add_event(Event(description = 'Revisão'))
schedule.add_event(Event(description = 'Prova 01', emphasis=True, code=-1))

schedule.add_event(Event(description = 'Resolução da Prova 01'))
schedule.add_event(Event(description = 'Resolução de sistemas lineares'))

schedule.add_event(Event(description = 'Feriado', emphasis=True, code=-1))
schedule.add_event(Event(description = 'Formas matriciais especiais'))

schedule.add_event(Event(description = 'Métodos iterativos de fatoração'))
schedule.add_event(Event(description = 'Comparação de desempenho'))

schedule.add_event(Event(description = 'Integração numérica'))
schedule.add_event(Event(description = 'Regras avançadas de integração numérica'))

schedule.add_event(Event(description = 'Erro de regras de quadratura'))
schedule.add_event(Event(description = 'Soluções numéricas de EDO'))

schedule.add_event(Event(description = 'Métodos Runge-Kutta'))
schedule.add_event(Event(description = 'Sistemas de EDO'))

schedule.add_event(Event(description = 'Aplicações a sistemas físicos'))
schedule.add_event(Event(description = 'Método das diferenças finitas'))

schedule.add_event(Event(description = 'Fontes de erros'))
schedule.add_event(Event(description = 'Revisão'))

schedule.add_event(Event(description = 'Prova 02', emphasis=True, code=-1))
schedule.add_event(Event(description = 'Resolução da Prova 02'))

schedule.add_event(Event(description = 'Revisão de Provas', code=-1))
schedule.add_event(Event(description = 'Prova Substitutiva', emphasis=True, code=-1))

schedule.add_event(Event(description =
	'Menções Finais.  Revisão de notas', code=-1))
schedule.add_event(Event(description =
	'Submissão das menções finais no sistema acadêmico', code=-1))

schedule.latex()
