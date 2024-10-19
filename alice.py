from uagents import Agent, Context, Model

class Message(Model):
    message: str

alice = Agent(
    name="alice",
    port=8000,
    seed="01_agent_alice",  # Add this line
    endpoint=["http://127.0.0.1:8000/submit"],
)

@alice.on_event("startup")
async def introduce(ctx: Context):
    ctx.logger.info(f"Alice's address: {ctx.address}")

@alice.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    reply = Message(message=f"Thanks for your message, {sender}! How are you?")
    await ctx.send(sender, reply)

if __name__ == "__main__":
    alice.run()