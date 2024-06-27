from helpbot import HelpBot
import chainlit as cl

bot = HelpBot()

@cl.on_message 
async def main(message: cl.Message):
    """
    Main function.
    """  
    response = bot.respond_to_user(message.content)
    await cl.Message(response).send()
