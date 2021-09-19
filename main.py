import os
import discord
from discord.ext import commands
from keep_alive import keep_alive

intents = discord.Intents()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print(f'{client.user.name} has joined Discord!')


@client.event
async def on_member_join(member):

    await member.send(f"""Hello {member.name}, Good to see you!:partying_face: 
Me, the Jr.ROCKY
Always ready to help You..!

:thinking:About WIT:
WIT - Women In Tech in association with TinkerHub Foundation is specially dedicated community for enhancing women in the field of technology and offering them training and support for growing.

To verify to #girls channel ask verify in #general.Happy learning!:yum:

:pushpin:Talk sessions :

:sparkles: "Lightning Talk" : Each College Take initiative to conduct a talk on a particular stack for 3 days a week.

:sparkles: "Fireside Chat" : Talking with an expert
"Network Night"

:pushpin:WIT Events :

:sparkles:" Shehacks": Conducted Monthly once for building cool projects along with mentor support.

:sparkles:" foundational courses":      Conducted Monthly Once
One week learning Bootcamp with project submission at the end.

:sparkles:"Mentorship programs":    Conducted Monthly once
Connect with mentors one-on-one.
""")
    await member.send("""\n:loud_sound: Follow these Rules :

:pushpin: Do not send any kind of spam messages

:pushpin: Do not send messages with malicious links attached

:pushpin: Don't sent unwanted content. 

:pushpin: Follow Discord Community Guidelines

:pushpin: Be cordial and respectful to community members, toxic behaviour will not be tolerated!

:pushpin: We will not encourage any acts that cause trouble or hurt others

:pushpin: No cyberbullying

:pushpin: Contact Admins for  support

:pushpin: Any one violating the above rules will be kicked immediately .Report to officials if you find anyone violating these rules."""
                      )

    await member.send("Do you want to be a part of Women In Tech ?")
    await member.send("If Yes, then share a few details:"
                      "\n Name"
                      "\nCampus"
                      "\nLead Name"
                      "\nDiscord ID")


keep_alive()

token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
