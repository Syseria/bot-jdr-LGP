import nextcord


class RuleView(nextcord.ui.View):

    rulesAccepted: bool = False
    member: nextcord.Member = None

    @nextcord.ui.button(label="J'accepte !",
                        style=nextcord.ButtonStyle.success,
                        custom_id="RulesAccepted")
    async def rules_accepted(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("Merci et bienvenu sur le discord de l'Espace JdR !",
                                                ephemeral=True)
        self.rulesAccepted = True
        self.member = interaction.user
        self.stop()


async def set_rules(channel: nextcord.TextChannel):
    embed = nextcord.Embed(
        title=f"Règles",
        colour=nextcord.Color.from_rgb(255, 0, 0),
        description=f"Afin d'accéder à l'intégralité du serveur, veuillez lire les règles ci-dessous et les accepter.\n\
        En acceptant ces règles, vous vous engagez à les respecter et acceptez toute sanction pouvant en découler."
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

    member = nextcord.Member
    guild = nextcord.Guild
    view = RuleView()

    await channel.send(embed=embed, view=view)
    await view.wait()

    if view.rulesAccepted:
        await view.member.add_roles(nextcord.Object(id(1242177867589091338)), reason="Rules Accepted")

async def set_info(channel: nextcord.TextChannel):
    return True


async def set_welcome(channel: nextcord.TextChannel):
    await channel.send("Welcome")

