# -*- coding: iso-8859-1 -*-

from datetime import *

class Event:
	def __init__(self, code = 1, date = datetime.now(), description = '', \
		emphasis = False, duration = 1, color = None):

		self.code = code
		self.date = date
		self.description = description
		self.emphasis = emphasis
		self.duration = duration
		self.color = color

	def latex(self):
		# Impressão do cãdigo do evento
		if self.color == None:
			color = ''
		else:
			color = '\\cellcolor[%s]{%s}' % (self.color)

		if self.code > 0:
			code = str(self.code)
		else:
			code = '-'

		text = '& %s%s' % (color, code)

		# Impressão da data
		date = '%02d/%02d' % (self.date.day, self.date.month)

		text = '%s & %s%s' % (text, color, date)

		# Impressão da descriãão do evento
		if self.emphasis:
			emphasis = '\\textbf'
		else:
			emphasis = '\\textit'

		description = '%s{%s}' % (emphasis, self.description)

		text = '%s & %s%s \\\\' % (text, color, description)

		print text

class Schedule:
	def __init__(self, start = datetime.now(), events_per_week = 2, distribution = None):
		self.start = start
		self.events_per_week = events_per_week
		self.code = 1
		self.count = 0
		self.events = []
		self.distribution = distribution

	def add_event(self, event):
		# Atualiza o cãdigo
		if event.code > 0:
			event.code = self.code
			self.code = self.code + 1

		# Define a cor, se necessãrio
		if self.count % 2 == 0:
			event.color = ('gray', '.9')

		# Atualiza a data
		delta = timedelta(7*(self.count / self.events_per_week))
		date = self.start + delta

		if self.distribution != None:
			delta = timedelta(self.distribution[self.count % self.events_per_week])
		else:
			delta = timedelta(2*(self.count % self.events_per_week))

		date = date + delta

		event.date = date

		# Atualiza a contagem
		self.count = self.count + event.duration

		self.events.append(event)

	def latex(self, breaks = None):
		# Imprimindo a seãão
		print '\\section{Cronograma}'

		# Imprimindo o header da tabela
		print '\\begin{tabularx}{0.9\\textwidth}{cccX}'
		print '\\toprule'

		text = '\\textbf{Semana} & \\textbf{Aula} & \\textbf{Data} '
		text = text + '& \\textbf{Conteúdo}\\\\'
		print text

		print '\\toprule'

		# Imprime as entradas da tabela
		count = 0
		week = 1
		new_page = False

		for event in self.events:
			if count % self.events_per_week == 0:
				if breaks != None:
					if week in breaks:
						new_page = True

				if new_page:
					print '\\bottomrule'
					print '\\end{tabularx}'
					print '\n\\pagebreak\n'
					print '\\begin{tabularx}{0.9\\textwidth}{cccX}'
					print '\\toprule'

					text = '\\textbf{Semana} & \\textbf{Aula} & \\textbf{Data} '
					text = text + '& \\textbf{Conteúdo}\\\\'
					print text

					print '\\toprule'
					new_page = False

				text = '\\multirow{%d}*{\\textbf{%02d}}' % \
					(self.events_per_week, week)

				if week != 1:
					text = '\\midrule\n' + text

				print text

				week = week + 1

			event.latex()

			count = count + 1

		# Imprime o trailer da tabela
		print '\\bottomrule'
		print '\\end{tabularx}'
