from ticket import Ticket
from lista_encadeada import No, ListaEncadeada

import time

class Especialista:
    def __init__(self, nome, area, id_especialista):
        self.nome = nome
        self.area = area  # ex: "comunicacoes", "energia", "navegacao"
        self.id = id_especialista
        self.fila = ListaEncadeada()    # fila própria (lista encadeada)
        self.atendimentos_finalizados = 0
        # opcional: manter histórico de atendimentos finalizados (ids)
        self.historico_finalizados = []

    def receber_ticket(self, ticket):
        """Recebe um ticket encaminhado pela triagem e insere no fim da fila do especialista."""
        # atualiza o status do ticket para indicar que está aguardando atendimento especializado
        ticket.status = f"aguardando_{self.area}"
        # registra qual especialista recebeu (opcional)
        ticket.especialista_designado = self.nome
        # insere ao fim da fila do especialista (FIFO dentro da especialidade)
        self.fila.inserir_no_fim(ticket)

    def ver_proxima(self):
        """Retorna o próximo ticket sem removê-lo (útil pra painel visual)."""
        if self.fila.esta_vazia():
            return None
        return self.fila.head.dado

    def atender_proximo(self, duracao_segundos: float = 0):
        """
        Processa (remove) o próximo ticket da fila do especialista, marca como finalizado.
        duracao_segundos: opcional, simula tempo de atendimento.
        Retorna o ticket finalizado ou None se fila vazia.
        """
        if self.fila.esta_vazia():
            return None

        ticket = self.fila.remover_inicio()
        # simular tempo (opcional)
        if duracao_segundos > 0:
            time.sleep(duracao_segundos)

        # marcar como finalizado e atualizar métricas
        ticket.status = "finalizado"
        ticket.data_finalizacao = time.time()
        self.atendimentos_finalizados += 1
        self.historico_finalizados.append(ticket.id)

        return ticket