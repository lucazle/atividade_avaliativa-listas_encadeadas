from ticket import Ticket
from lista_encadeada import No, ListaEncadeada
from especialista import Especialista

class Operador:
    def __init__(self, nome, id_operador):
        self.nome = nome
        self.id = id_operador
        self.atendimentos_realizados = 0
        # opcional: registrar histórico (lista simples só para auditoria, não para lógica)
        self.historico_ids = []

    def esta_disponivel(self):
        """Indicador simples se o operador está livre (pode ser expandido)."""
        return True  # por enquanto sempre disponível; você pode ligar/desligar

    def triagem_e_encaminhamento(self, fila_geral: "ListaEncadeada", especialista: "Especialista"):
        """
        Operador retira o próximo ticket da fila geral (remover_inicio) e encaminha
        para a fila do especialista especificado.
        Retorna o ticket encaminhado ou None se não tinha ticket.
        """
        if fila_geral.esta_vazia():
            return None

        # Remove o ticket da fila geral (simula pegar o chamado)
        ticket = fila_geral.remover_inicio()
        if ticket is None:
            return None

        # Atualiza informações do ticket
        ticket.status = "encaminhado_para_especialista"
        # Marca qual operador atendeu na triagem (campo extra)
        ticket.operador_triagem = self.nome

        # Enfileira no especialista (usa lista encadeada do especialista)
        especialista.receber_ticket(ticket)

        # Atualiza métricas do operador
        self.atendimentos_realizados += 1
        self.historico_ids.append(ticket.id)

        return ticket
