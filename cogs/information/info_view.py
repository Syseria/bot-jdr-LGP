import nextcord
import config
from utils.utils import custom_id

VIEW_NAME = "RoleView"


class InfoView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def handle_click(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        role_id = int(button.custom_id.split(':')[-1])
        role = interaction.guild.get_role(role_id)
        assert isinstance(role, nextcord.Role)
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f"Le rôle {role.name} a été retiré.", ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message("Merci et bienvenu sur le discord de l'Espace JdR !",
                                                    ephemeral=True)

    @nextcord.ui.button(label="J'accepte",
                        style=nextcord.ButtonStyle.success,
                        custom_id=custom_id(VIEW_NAME, config.MEMBER_ROLE_ID))
    async def accept_rules(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.handle_click(button, interaction)
