from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player
from code.Wind import Wind
from code.Tree import Tree


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        """Verifica se a entidade saiu da tela e, se necessário, ajusta sua vida."""
        if isinstance(ent, (Enemy, Wind, Tree)):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        """Verifica colisões entre entidades e aplica efeitos."""
        valid_interaction = False

        # Define interações válidas. Levando em conta que o P1 pode estar como ent1 ou ent2 na lógica de colisão
        if isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_interaction = True

        # se a var q valida a colisão for true, define as 4 perguntas de colisão para garantir q só colida quando uma ent chegar no limite da borda da outra
        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):

                # O player recebe dano do inimigo
                if isinstance(ent1, Player):
                    ent1.take_damage(ent2.damage)
                if isinstance(ent2, Player):
                    ent2.take_damage(ent1.damage)

                # Marca a origem do dano
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        """Atribui score ao jogador responsável pelo dano final."""
        if enemy.last_dmg == 'Player':
            for ent in entity_list:
                if isinstance(ent, Player):
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        """Executa a verificação de colisões para todas as entidades."""
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        """Verifica a vida das entidades e remove aquelas que foram derrotadas."""
        for ent in entity_list:
            if isinstance(ent, Player) and ent.blink_timer > 0 and ent.health <= 0:
                ent.blink_timer -= 1
