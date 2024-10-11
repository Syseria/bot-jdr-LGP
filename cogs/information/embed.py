import nextcord


async def set_info() -> nextcord.Embed:
    embed = nextcord.Embed(
        title=f"Comment ça fonctionne ?",
        colour=nextcord.Color.from_rgb(254, 193, 68),
        description=f"Vous trouverez ici tous les `One Shots` proposés pendant le festival, accompagnées d'un bref "
                    f"aperçu \
                    et aurez la possibilité de vous y inscrire. Si une table est pleine, vous serez mis sur \
                    `liste d'attente` et serez contacté dans le cas d'un désistement."
    )
    embed.add_field(
        name=":large_blue_diamond: One Shots",
        value="Vous trouverez dans cette catégorie différents `channels` portant chacun le nom d'une partie de jeu \
              proposée par nos ${Dungeon Masters} lors du festival. Vous y lirez un bref aperçu de l'aventure que \
              vous pourriez y vivre si vous décidiez de rejoindre cette aventure (ou plus communément appelée: \
              table).\n\n\
              Si la table vous intéresse, vous pourrez vous y inscrire en cliquant sur le bouton `Je m'inscrit !` \
              que vous trouverez au bas du descriptif. Vous serez alors invité à nous donner quelques informations \
              telles que le nombre de personnes que vous inscrivez à la table et vos informations de contact.\n\n\
              NB: Toutes les informations transmises seront effacées une fois le festival terminées.",
        inline=False
    )
    embed.add_field(
        name=":large_blue_diamond: Tables",
        value="Cette catégorie apparaîtra une fois inscrit à une table et vous y retrouverez toutes les \
              tables auxquelles vous êtes inscrit et attendu. Il s'agira aussi du premier moyen de notification \
              utilisé pour vous rappelé de vous présenter 5 minutes avant le début de votre session à l'espace JdR.\n\n\
              NB: Si vous n'avez pas transmis de numéro de téléphone, que nous ne pouvons vous contacter \
              via Discord et que vous ne vous présenté pas à l'espace JdR dans les 5 minutes après l'heure de début \
              convenue, nous réattribuerons votre place.",
        inline=False
    )

    return embed
