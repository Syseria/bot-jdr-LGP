import nextcord


async def set_new_table() -> nextcord.Embed:
    embed = nextcord.Embed(
        title=f"Outils de création d'une table",
        colour=nextcord.Color.dark_gold()
    )
    embed.add_field(
        name=":large_blue_diamond: Pseudo",
        value="Celui-ci doit correspondre à votre Prénom.\n\
        Ceci afin de faciliter la communication et les échanges entre nous tous.\
        Surement vouer à changer suivant l'implémentation du bot",
        inline=False
    )
    embed.add_field(
        name=":large_blue_diamond: Image de profil",
        value="Celle-ci ne doit pas véhiculer de message offensant.",
        inline=False
    )
    embed.add_field(
        name=":large_blue_diamond: @everyone et @here",
        value="Tout le monde a la possibilité d'utiliser ces tags.\n\
        Utiliser les correctement et n'en abusez pas !",
        inline=False
    )
    embed.add_field(
        name=":red_square: NSFW",
        value="Le contenu NSFW est strictement banni de ce serveur.\n\
        Cette décision est irrévocable et non ouverte à discussion.\n\
        Nous sommes ici pour partager une passion. Que nous soyons suffisament agé ou non,\
        ce type de contenu n'a pas sa place ici.\n\
        NB: Certain JdR pourrait être amené, de part leur univers, à enfreindre cette règle,\
        merci de nous en mettre au courant AVANT de poster du contenu, que nous puissions \
        mettre en place les barrières minimales.\
        Toute infraction volontaire à cette règle entraînera un bannissement immédiat.",
        inline=False
    )

    return embed
