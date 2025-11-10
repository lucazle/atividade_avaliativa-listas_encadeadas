class No:
    def __init__(self, dado):
        self.dado = dado    # pode ser um Ticket ou outro objeto
        self.proximo = None # ponteiro para o próximo nó

class ListaEncadeada:
    def __init__(self):
        self.head = None  # primeiro nó
        self.tail = None  # último nó (facilita inserir no fim em O(1))
        self.tamanho = 0  # opcionalmente mantemos o tamanho

    def esta_vazia(self):
        return self.head is None

    def inserir_no_fim(self, dado):
        """Insere ao final da lista (fila padrão). O(1) com tail."""
        novo = No(dado)
        if self.esta_vazia():
            self.head = novo
            self.tail = novo
        else:
            self.tail.proximo = novo
            self.tail = novo
        self.tamanho += 1

    def remover_inicio(self):
        """Remove e retorna o primeiro elemento. O(1)."""
        if self.esta_vazia():
            return None
        removido = self.head.dado
        self.head = self.head.proximo
        if self.head is None:   # se lista ficou vazia, atualiza tail
            self.tail = None
        self.tamanho -= 1
        return removido

    def mostrar_todos(self):
        """Retorna lista de representações (útil pra exibir em interface)."""
        atual = self.head
        resultado = []
        while atual is not None:
            resultado.append(atual.dado)  # guarda o objeto Ticket
            atual = atual.proximo
        return resultado

    def buscar_por_id(self, id_ticket):
        """Percorre a lista e retorna o ticket com id igual (ou None)."""
        atual = self.head
        while atual:
            t = atual.dado
            if getattr(t, "id", None) == id_ticket:
                return t
            atual = atual.proximo
        return None

    def inserir_por_prioridade(self, dado):
        """
        Insere mantendo a ordem por prioridade (menor número = maior prioridade).
        Ex.: prioridade 1 antes de 2. Complexidade O(n) pois precisa percorrer.
        Útil se quisermos manter a fila sempre ordenada.
        """
        novo = No(dado)
        # caso lista vazia
        if self.esta_vazia():
            self.head = self.tail = novo
            self.tamanho += 1
            return

        # se novo tem maior prioridade que o head -> insere no início
        if dado.prioridade < self.head.dado.prioridade:
            novo.proximo = self.head
            self.head = novo
            self.tamanho += 1
            return

        # percorre para encontrar posição correta
        anterior = None
        atual = self.head
        while atual and atual.dado.prioridade <= dado.prioridade:
            anterior = atual
            atual = atual.proximo

        # insere entre anterior e atual
        anterior.proximo = novo
        novo.proximo = atual
        if atual is None:  # inseriu no fim -> atualizar tail
            self.tail = novo
        self.tamanho += 1