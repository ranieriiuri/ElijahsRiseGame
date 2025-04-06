from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player
from code.Wind import Wind
from code.Tree import Tree
from code.MeatBread import MeatBread  # Importação da classe MeatBread

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

        # Verifica colisões entre Player e Wind
        if isinstance(ent1, Player) and isinstance(ent2, Wind):
            valid_interaction = True
        elif isinstance(ent1, Wind) and isinstance(ent2, Player):
            valid_interaction = True

        # Verifica colisões entre Player e Tree
        if isinstance(ent1, Player) and isinstance(ent2, Tree):
            valid_interaction = True
        elif isinstance(ent1, Tree) and isinstance(ent2, Player):
            valid_interaction = True

        # Verifica colisões entre Player e MeatBread (o que resultará em coleta e acréscimo do score, não dano!)
        if isinstance(ent1, Player) and isinstance(ent2, MeatBread):
            valid_interaction = True
        elif isinstance(ent1, MeatBread) and isinstance(ent2, Player):
            valid_interaction = True

        # se a var q valida a colisão for true, define as 4 perguntas de colisão para garantir q só colida quando uma ent chegar no limite da borda da outra
        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):

                # Colisão entre Player e MeatBread (não causa dano)
                if isinstance(ent1, Player) and isinstance(ent2, MeatBread):
                    ent2.collect(ent1)  # Player coleta MeatBread
                    EntityMediator.update_meat_bread_bar(ent1)  # Atualiza barra de MeatBreads
                if isinstance(ent2, Player) and isinstance(ent1, MeatBread):
                    ent1.collect(ent2)  # Player coleta MeatBread
                    EntityMediator.update_meat_bread_bar(ent2)  # Atualiza barra de MeatBreads

                # Colisão entre Player e Enemy, Tree ou Wind causa dano
                if isinstance(ent1, Player) and isinstance(ent2, (Enemy, Tree, Wind)):
                    damage = ent2.damage  # dano do inimigo, árvore ou vento
                    if isinstance(ent2, Enemy):
                        damage *= 0.8  # Player sofre 20% menos dano de inimigos
                    elif isinstance(ent2, (Tree, Wind)):
                        damage *= 0.5  # Player sofre 50% menos dano de árvores e vento
                    ent1.take_damage(damage)

                # Marca a origem do dano
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name


    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        """
        Executa a verificação de colisões para todas as entidades.
        - Utilizando as lógicas nos métodos criados acima para verificar.

        """
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

    @staticmethod
    def __give_score(player: Player, entity_list: list[Entity]):
        """Atribui score ao jogador por pegar MeatBreads e decrementa por sofrer dano."""
        # Atribuindo score por coletar MeatBreads
        if player.meat_bread_bar > 0:
            player.score += player.meat_bread_bar * 70  # Adiciona 70 pontos por cada MeatBread coletado

        # Penaliza o jogador por sofrer dano de Enemy, Tree ou Wind
        for ent in entity_list:
            if isinstance(ent, (Enemy, Tree, Wind)) and ent.last_dmg == 'Player':
                # Subtrai pontos do jogador com base no dano recebido
                damage = ent.damage
                if isinstance(ent, Enemy):
                    damage *= 0.8  # Dano reduzido para Enemy
                elif isinstance(ent, (Tree, Wind)):
                    damage *= 0.5  # Dano reduzido para Tree e Wind

                # Subtrai pontos do jogador com base no dano
                player.score -= damage * 2  # Multiplicador de penalidade de 2x para o dano

    @staticmethod
    def update_meat_bread_bar(player: Player):
        """Atualiza a barra de MeatBreads e comunica a Level sobre o progresso."""
        if player.meat_bread_bar >= player.meat_bread_target:
            print("Barra de MeatBreads cheia! Fase concluída com sucesso.")
            # Aqui, a comunicação com o Level pode ser feita, por exemplo, chamando um método da Level para finalização
            # Ex: Level.complete_level(player)
            # Ou enviando a informação para o Level se o jogador completou a fase e atingiu a quantidade de MeatBreads
        else:
            print(f"MeatBreads coletados: {player.meat_bread_bar}/{player.meat_bread_target}")
            # Atualize a barra de MeatBreads no jogo (isto pode ser feito em Level, mas a comunicação vem daqui)
