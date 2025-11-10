from dataclasses import dataclass
import itertools

@dataclass
class Ticket:
    id: int
    prioridade: int   # 1 = emergência, 2 = alta, 3 = normal
    nome_nave: str
    codigo_missao: str
    setor_orbital: str
    descricao: str
    tripulacao: bool
    status: str = "aguardando_triagem"

    def __repr__(self):
        # representação curta para debug
        pri = {1: "EMERG", 2: "ALTA", 3: "NORMAL"}.get(self.prioridade, str(self.prioridade))
        return f"<Ticket #{self.id} {self.nome_nave} {pri} {self.status}>"