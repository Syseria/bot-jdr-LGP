import nextcord
import config
from utils.utils import custom_id

VIEW_NAME = "RoleView"


class RoleView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="J'accepte",
                        style=nextcord.ButtonStyle.success,
                        custom_id=custom_id(VIEW_NAME, config.MEMBER_ROLE_ID))
    async def accept_rules(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("Merci et bienvenu sur le discord de l'Espace JdR !", ephemeral=True)
